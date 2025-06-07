import pandas as pd
import numpy as np

def add_new_column_to_df(df, current_service_name):
    """
    Adds a standard 'Service' column to the DataFrame using the specified column name.
    This ensures consistency across different vendor schemas.
    
    Parameters:
    - df (DataFrame): Input DataFrame from a vendor.
    - current_service_name (str): Column name to copy as the universal 'Service' column.
    
    Returns:
    - DataFrame with the new 'Service' column added.
    """
    df['Service'] = df[current_service_name]
    return df

def main():
    # Load data
    GCP_df = pd.read_csv('GCP_AI_data.csv')
    Amazon_df = pd.read_csv('Amazon_AI_data.csv')
    Azure_df = pd.read_csv('Azure_AI_data.csv')

    # Standardize column names
    GCP_df = add_new_column_to_df(GCP_df, 'Service Name')
    Amazon_df = add_new_column_to_df(Amazon_df, 'Product Name')
    Azure_df = add_new_column_to_df(Azure_df, 'Usage Type')

    # Combine all vendors into one DataFrame
    all_data_df = pd.concat([GCP_df, Azure_df, Amazon_df], ignore_index=True)

    # Fill missing costs with 0
    all_data_df['Cost Before Uplifts ($)'].fillna(0, inplace=True)

    # Format date column
    all_data_df['invoice_date'] = pd.to_datetime(all_data_df['invoice_date'], format='%m/%d/%Y')
    all_data_df['invoice_date'] = all_data_df['invoice_date'].dt.strftime('%m/%d/%Y')

    # Add uplifted cost
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
    all_data_df['Cost After Uplifts ($)'] = np.select(conditions, uplifts, default=np.nan).round(2)

    # Export processed data
    all_data_df.to_csv('all_test.csv', index=False)

if __name__ == "__main__":
    main()
