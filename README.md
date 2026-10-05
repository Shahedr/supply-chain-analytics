# Supply Chain Analytics

An end-to-end portfolio project focused on using data to understand supply chain performance, identify operational risks, and support better business decisions.

> **Status:** In development. This project is being built in public as part of my progression from analytics into data science, machine learning, and data engineering.

## Project Goals

This project will analyze supply chain data across products, suppliers, inventory, fulfillment, shipping, and quality. The goal is to move beyond isolated exercises and build a realistic analytics workflow from raw data to business recommendations.

## Business Questions

The analysis will explore questions such as:

- Which products and suppliers contribute the most revenue?
- Which suppliers have the longest lead times or weakest delivery performance?
- Where are inventory levels most likely to create stockout or overstock risk?
- How do shipping methods compare on cost and delivery performance?
- Which products or suppliers show the highest defect or quality risk?
- What operational patterns could be improved through better planning?

## Planned Tech Stack

- **Python:** NumPy, pandas, Matplotlib
- **SQL:** PostgreSQL
- **Statistics:** descriptive analysis, distributions, relationships, and hypothesis-driven analysis where appropriate
- **Visualization:** Tableau or Power BI
- **Version Control:** Git & GitHub

Later versions may extend the project with ETL, dbt, workflow orchestration, and machine learning where they add genuine value.

## Repository Structure

```text
supply-chain-analytics/
├── data/          # Data documentation and project datasets
├── notebooks/     # Exploration, cleaning, and analysis notebooks
├── src/           # Reusable Python code
├── sql/           # SQL queries and database work
├── dashboards/    # Dashboard files, exports, and screenshots
├── docs/          # Project planning and supporting documentation
└── README.md      # Project overview and final findings
```

## Project Roadmap

- [ ] Select and document a suitable public or synthetic dataset
- [ ] Understand the dataset and define business questions
- [ ] Clean and validate the data with Python
- [ ] Perform exploratory data analysis
- [ ] Load relevant data into PostgreSQL
- [ ] Answer business questions with SQL
- [ ] Apply appropriate statistical analysis
- [ ] Build a business-facing dashboard
- [ ] Summarize findings and recommendations
- [ ] Refactor reusable code and polish the repository

## Current Milestone

**Project setup and data selection.**

The next step is to choose a dataset, understand its columns and limitations, and begin the first real Python data-analysis workflow.
