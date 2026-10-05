# Supply Chain Analytics

I'm building this project to practice a realistic supply chain analysis workflow while strengthening my Python, SQL, statistics, and data visualization skills.

The project is still in progress, and I'll keep updating this README as I work through the data and learn new tools.

## Dataset

For this project, I'm using the **USAID Supply Chain Shipment Pricing / SCMS Delivery History dataset**. I chose it because it contains real public shipment data rather than a small synthetic example, while still being manageable enough to explore step by step.

The dataset includes information such as shipment mode, destination country, vendor, freight cost, shipment weight, product details, and delivery dates.

## What I want to analyze

My first questions are:

- Which shipment modes are used most often, and how do their costs compare?
- Which countries and vendors account for the most shipments?
- What factors appear to be associated with higher freight costs?
- How closely do scheduled and actual delivery dates line up?
- Are there patterns in delays by shipment mode, vendor, country, or product group?

These questions may change as I understand the dataset better.

## Tools I plan to use

- Python
- NumPy and pandas
- Matplotlib
- SQL and PostgreSQL
- Statistics
- Tableau or Power BI
- Git and GitHub

As I get further into data engineering and machine learning, I may extend this project into a small ETL workflow and a prediction problem if the data supports it.

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

## What I'm working on now

The dataset is selected. My next step is to inspect the file before doing any analysis: number of rows and columns, column names, data types, missing values, and a few sample records.

I want to understand what the data actually contains before deciding which questions are worth pursuing.
