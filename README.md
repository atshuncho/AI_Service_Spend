# AI Service Spend Dashboard

## Overview

This project visualises AI Cloud Spend across major vendors (Amazon, Azure, and GCP) for a global bank. It reflects a real-world task I was assigned at work, aimed at improving transparency and decision-making around AI service costs. All data has been anonymised, and figures adjusted for confidentiality.

## Problem Statement
As the bank adopted AI services across cloud platforms, leadership needed visibility into:
•	Total spend on AI-related services
•	Differences in spend between classical and generative AI
•	Opportunities for cost optimisation

## Project Files
| File                  | Description                                                  |
|---------------------  |-------------                                                 |
| `Amazon_AI_Spend.csv` | Anonymised spend data from AWS AI services                   |
| `Azure_AI_Spend.csv`  | Anonymised spend data from Azure AI services                 |
| `GCP_AI_Spend.csv`    | Anonymised spend data from GCP (e.g. Vertex AI)              |
| `AI_Type.xlsx`        | Mapping of each service to either Generative or Classical AI |
| `AI_Spend.pbix`       | Power BI dashboard for interactive spend exploration         |
| `main.py`             | Python script used for data manipulation                     |


## Technologies Used
•	Python (Pandas) – for data preparation
•	Excel– for manual classification of services
•	Power BI Desktop – for report building and visualisation
•	GitHub – for version control and documentation

## Key Outputs
•	Visual breakdown of AI spend by cloud vendor
•	Split between Generative AI and Classical AI service usage
•	Identification of high-cost services and trends over time
•	Reusable dashboard for business stakeholders

## How to Use
1.	Clone this repository to your machine
2.	Open `AI_Spend.pbix` in Power BI Desktop
3.	Interact with the filters (e.g., vendor, AI type, service) to explore trends
4.	Use the classification in `AI_Type.xlsx` to segment services
> Note: If you want to reprocess or modify data, refer to the `main.py` script.

## Disclaimer
All company specific information has been removed. Spend figures and account identifiers are fictional or anonymised. This project is for demonstration and educational purposes only.

## Author
Ashraf Sanni– Cloud FinOps Data Engineer  
[LinkedIn](www.linkedin.com/in/ashraf-tobi-sanni-14769521a) | [GitHub]( atshuncho)
