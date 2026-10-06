# Business Findings and Recommendations

## Executive summary

This case study analyzes **10,324 shipment records** from the USAID / PEPFAR SCMS Delivery History dataset. The goal is to understand shipment mix, freight-data quality, delivery timing, and the analytical trade-offs that matter when using operational supply-chain data.

## Verified findings

### 1. Air is the dominant recorded shipment mode

| Shipment mode | Records | Share |
|---|---:|---:|
| Air | 6,113 | 59.21% |
| Truck | 2,830 | 27.41% |
| Air Charter | 650 | 6.30% |
| Ocean | 371 | 3.59% |
| Missing | 360 | 3.49% |

**Implication:** mode-level analysis should be weighted by shipment volume. Air represents the majority of records, while conclusions about Ocean and Air Charter are based on much smaller groups.

### 2. Typical delivery timing is close to the scheduled date, but the distribution contains large extremes

- Mean delivered-minus-scheduled difference: **-6.02 days**
- Median: **0 days**
- 25th percentile: **-3 days**
- 75th percentile: **0 days**
- Minimum: **-372 days**
- Maximum: **192 days**
- Extreme observations outside +/-100 days: **216 records (2.09%)**

**Implication:** the mean alone is not a good summary of delivery performance. The median and segmented distributions are more robust, while extreme records should be investigated separately instead of automatically deleted.

### 3. Freight and weight require careful missing-value treatment

- Numeric shipment weight available: **6,372 records (61.72%)**
- Numeric freight cost available: **6,198 records (60.03%)**

The source columns also contain meaningful operational text such as freight being included in commodity cost, invoiced separately, or weight being captured separately.

**Implication:** replacing non-numeric freight or weight values with zero would create false information. The project preserves the original source fields and creates separate numeric analysis fields.

## Recommendations

1. **Use robust delivery KPIs.** Report median delivery difference and late-rate by shipment mode alongside the mean.
2. **Segment before comparing cost.** Freight comparisons should control for shipment mode and weight where numeric data is available.
3. **Treat missingness as information.** Keep source text that explains why freight or weight is not numeric.
4. **Review extremes separately.** Investigate the 216 extreme date differences for data-entry issues, exceptional orders, or legitimate operational events.
5. **Avoid causal claims.** This is observational shipment data; associations between mode, weight, freight, country, vendor, and timing do not prove causation.
6. **Respect dataset scope.** The source should not be interpreted as a complete view of all PEPFAR purchases or total landed cost. Order-level records may also represent split shipments with different freight components or delivery dates.

## Reproducible next-level analysis

The repository includes scripts that calculate the following directly from the cleaned dataset:

- top destination countries and vendors
- median and mean freight cost by shipment mode
- late-rate and delivery timing by shipment mode
- freight-per-kilogram comparisons where both fields are numeric
- Spearman correlation between shipment weight and freight cost
- Kruskal-Wallis comparison of freight distributions across modes
- chi-square association between shipment mode and delivery status

These outputs are generated locally rather than hard-coded so the analysis remains auditable and reproducible.
