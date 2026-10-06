# Supply Chain Findings

I used the SCMS delivery-history data to look at shipment mix, delivery timing, freight/weight quality, and where simple summary statistics can be misleading.

## 1. Most records are air shipments

| Shipment mode | Records | Share |
|---|---:|---:|
| Air | 6,113 | 59.21% |
| Truck | 2,830 | 27.41% |
| Air Charter | 650 | 6.30% |
| Ocean | 371 | 3.59% |
| Missing | 360 | 3.49% |

Air accounts for the majority of rows in the dataset. That matters because an overall average can end up describing air shipments more than the other modes. I would compare modes separately before using an overall freight or delivery KPI.

## 2. The median delivery difference is more useful than the mean by itself

- Mean delivered-minus-scheduled difference: **-6.02 days**
- Median: **0 days**
- 25th percentile: **-3 days**
- 75th percentile: **0 days**
- Minimum: **-372 days**
- Maximum: **192 days**
- Records outside ±100 days: **216 (2.09%)**

The typical record is close to its scheduled date, but there are large early and late values in the tails. Because of that, I would report the median and distribution by shipment mode alongside the mean rather than using one average as the delivery-performance story.

I kept the extreme rows and flagged them instead of deleting them. They may be data-entry problems, but they may also represent unusual operational situations that deserve separate review.

## 3. “Missing” freight and weight are not always missing in the usual sense

- Numeric shipment weight available: **6,372 records (61.72%)**
- Numeric freight cost available: **6,198 records (60.03%)**

Some source values contain text such as freight being included in commodity cost, invoiced separately, or weight being captured separately. Replacing those entries with zero would change their meaning.

For analysis, I created separate numeric fields and left the original source columns intact.

## How I would use these findings

- report median delivery difference and late rate by shipment mode, not only an overall average
- compare freight cost within similar shipment modes and weight ranges
- keep operational text that explains why a numeric value is unavailable
- review the 216 extreme delivery differences separately before deciding whether any are data-quality errors
- avoid treating correlations in this observational dataset as causal relationships

## Additional analysis in the repo

The Python and SQL files also cover:

- top destination countries and vendors
- mean and median freight cost by shipment mode
- delivery timing and late rate by mode
- freight per kilogram where both fields are numeric
- Spearman correlation between shipment weight and freight cost
- Kruskal-Wallis comparison of freight distributions across shipment modes
- chi-square association between shipment mode and delivery status

Those outputs are calculated from the cleaned dataset when the pipeline runs rather than copied into the repo as fixed conclusions.

## Dataset scope

The source should not be interpreted as a complete view of all PEPFAR purchases or total landed cost. Some orders may also appear across multiple shipment records, so order-level and shipment-level questions should not be mixed without checking the grain first.
