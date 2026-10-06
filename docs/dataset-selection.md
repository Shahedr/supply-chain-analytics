# Dataset Selection Notes

## Dataset

**USAID Supply Chain Shipment Pricing / SCMS Delivery History**

Official Data.gov listing: https://catalog.data.gov/dataset/supply-chain-shipment-pricing-data

Common CSV filename: `SCMS_Delivery_History_Dataset.csv`

## Why I chose it

I wanted a public dataset that looked more like an operational supply-chain file than a small classroom table. It includes shipment mode, vendor, destination country, product information, delivery dates, freight cost, and shipment weight, which gave me enough range to ask both data-quality and business questions.

The final dataset used in the project contains **10,324 shipment records**.

## What made the dataset useful

The most useful part was not just its size. Several fields require judgment:

- freight and weight contain both numeric values and operational text
- scheduled vs. delivered dates create a measurable delivery-timing field
- shipment modes have very different record counts
- some delivery differences are extreme enough to require review
- shipment and order grain should not be assumed to be identical

Those issues made the dataset a better fit for a full analytics case study than a perfectly clean example dataset.

## How I used it

The project now includes:

- raw-data inspection
- date and numeric-field cleaning
- shipment-mode, country, vendor, freight, and delivery analysis
- statistical checks
- PostgreSQL/SQL analysis
- a static summary dashboard
- business findings and limitations

I decided not to add a predictive model to this repo without a stronger target/use case; the analysis is intentionally focused on descriptive and diagnostic questions.
