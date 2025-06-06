import pandas as pd
import numpy as np

def add_new_column_to_df(df, current_service_name):
    df['Service'] = df[current_service_name]
    return df


GCP_df = pd.read_csv('GCP_AI_data.csv')
Amazon_df = pd.read_csv('Amazon_AI_data.csv')
Azure_df = pd.read_csv('Azure_AI_data.csv')

# services are under different columns for each vendor.
# Amazon uses Product Name, GCP uses Service Name and Azure uses Usage Type
# Below I have created a universal column called service that will be used for all three vendors

GCP_df = add_new_column_to_df(GCP_df, 'Service Name')
Amazon_df = add_new_column_to_df(Amazon_df, 'Product Name')
Azure_df = add_new_column_to_df(Azure_df, 'Usage Type')

# concat the vendors to 1 df so we can change the data on 1 df

all_data_df = pd.concat([GCP_df, Azure_df, Amazon_df], ignore_index=True)

# There are currently some empty values under the cost column 'Cost Before Uplifts ($)'.
# They are empty as a cost had not occurred.
# We will fill these with 0's so further issue do not occur when we visualise the costs

all_data_df['Cost Before Uplifts ($)'].fillna(0, inplace=True)

# The date column is in the format month, day, year, but it is shown as day, month, year so this is changed below

# changing the format
all_data_df['invoice_date'] = pd.to_datetime(all_data_df['invoice_date'], format='%m/%d/%Y')
all_data_df['invoice_date'] = all_data_df['invoice_date'].dt.strftime('%m/%d/%Y')

# We need to add the percentage uplift to the costs to get the cost that is charged back to the company
# GCP uplift = 12.5%
# AWS uplift = 8.94%
# Azure uplift = 6.74%

conditions = [
    all_data_df['vendor'] == 'GCP',
    all_data_df['vendor'] == 'Azure',
    all_data_df['vendor'] == 'Amazon'
]

uplifts = [
    all_data_df['Cost Before Uplifts ($)'] * 1.125,
    all_data_df['Cost Before Uplifts ($)'] * 1.0674,
    all_data_df['Cost Before Uplifts ($)'] * 1.0894
]

all_data_df['Cost After Uplifts ($)'] = np.select(conditions, uplifts, default=np.nan)

# I am working with cost data so below I change the data to 2 decimal places
all_data_df['Cost After Uplifts ($)'] = all_data_df['Cost After Uplifts ($)'].round(2)
all_data_df.to_csv('all_test.csv', index=False)