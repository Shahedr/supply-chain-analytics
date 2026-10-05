# Dataset Selection Notes

## Dataset chosen

**USAID Supply Chain Shipment Pricing / SCMS Delivery History**

## Why I chose it

I wanted a dataset that felt closer to a real supply chain problem than a small synthetic example. This dataset gives the project enough depth to analyze shipment cost, delivery timing, vendors, countries, shipment modes, products, and order details.

It is also large enough to support multiple stages of the project, including Python analysis, SQL queries, visualization, and potentially a prediction problem later.

## Source

- U.S. Agency for International Development (USAID) public supply chain data
- Data.gov listing: https://catalog.data.gov/dataset/supply-chain-shipment-pricing-data
- Common file name: `SCMS_Delivery_History_Dataset.csv`

## Project scope

This dataset will be used to:

- inspect and validate raw CSV data
- clean dates, numeric fields, and missing values
- compare shipment cost and delivery performance
- analyze vendors, countries, shipment modes, and products
- write SQL queries against cleaned data
- build supply chain KPIs and visualizations
- evaluate whether the data supports a useful prediction problem later

## Notes

The dataset has not been analyzed yet. The next step is to inspect the file and confirm what each column contains before finalizing the analysis questions.
