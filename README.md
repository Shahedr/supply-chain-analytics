# Supply Chain Analytics

This is a practice supply chain analytics project focused on shipment cost, delivery performance, vendors, countries, products, and logistics patterns using real public data.

The project is in progress, and I’ll continue updating the analysis, code, SQL, and visualizations as each stage is completed.

## Dataset

For this project, I’m using the **USAID Supply Chain Shipment Pricing / SCMS Delivery History dataset**. I chose it because it contains real public shipment data and gives me enough detail to explore freight cost, delivery timing, vendors, countries, shipment modes, products, and order-level information.

The dataset includes information such as shipment mode, destination country, vendor, freight cost, shipment weight, product details, and delivery dates.

## What I want to analyze

My first questions are:

- Which shipment modes are used most often, and how do their costs compare?
- Which countries and vendors account for the most shipments?
- What factors appear to be associated with higher freight costs?
- How closely do scheduled and actual delivery dates line up?
- Are there patterns in delays by shipment mode, vendor, country, or product group?

These questions may change as I explore the dataset and identify which patterns are most useful to investigate.

## Tools used in this project

- Python
- NumPy and pandas
- Matplotlib
- SQL and PostgreSQL
- Statistics
- Tableau or Power BI
- Git and GitHub

If the data supports it, I may later extend the project with a small ETL workflow and a prediction problem.

## Repository structure

```text
supply-chain-analytics/
├── data/          # Dataset and data notes
├── notebooks/     # Exploration, cleaning, and analysis
├── src/           # Reusable Python code
├── sql/           # SQL queries and database work
├── dashboards/    # Dashboard files and screenshots
├── docs/          # Project notes and planning
└── README.md      # Project overview and findings
```

## Project progress

- [x] Choose and document a public dataset
- [ ] Understand the columns and data types
- [ ] Check data quality and clean the dataset
- [ ] Explore the data with Python
- [ ] Use SQL to answer business questions
- [ ] Add statistical analysis where useful
- [ ] Build a dashboard
- [ ] Summarize the main findings and recommendations

## Current work

The dataset is selected. The next step is to inspect the file before doing any analysis: number of rows and columns, column names, data types, missing values, and a few sample records.

This first inspection will help determine which business questions are best supported by the data.
