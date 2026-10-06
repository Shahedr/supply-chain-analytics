-- SUPPLY CHAIN ANALYTICS: BUSINESS SQL
-- Run after: python src/load_postgres.py

-- 1) Executive KPI overview
SELECT
    COUNT(*) AS shipments,
    COUNT(DISTINCT country) AS countries,
    COUNT(DISTINCT vendor) AS vendors,
    ROUND(AVG(delivery_delay_days), 2) AS avg_delivery_difference_days,
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY delivery_delay_days) AS median_delivery_difference_days,
    ROUND(100.0 * AVG(extreme_delay_flag::int), 2) AS extreme_delay_pct
FROM shipments;

-- 2) Shipment mode mix
SELECT
    COALESCE(shipment_mode, 'Missing') AS shipment_mode,
    COUNT(*) AS shipments,
    ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 2) AS share_pct
FROM shipments
GROUP BY 1
ORDER BY shipments DESC;

-- 3) Freight cost by shipment mode
SELECT
    shipment_mode,
    COUNT(freight_cost_usd) AS shipments_with_numeric_freight,
    ROUND(AVG(freight_cost_usd), 2) AS avg_freight_usd,
    ROUND((PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY freight_cost_usd))::numeric, 2) AS median_freight_usd
FROM shipments
WHERE freight_cost_usd IS NOT NULL
GROUP BY shipment_mode
ORDER BY median_freight_usd DESC NULLS LAST;

-- 4) Delivery reliability by shipment mode
SELECT
    shipment_mode,
    COUNT(*) AS shipments,
    ROUND(AVG(delivery_delay_days), 2) AS avg_delivery_difference_days,
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY delivery_delay_days) AS median_delivery_difference_days,
    ROUND(100.0 * AVG((delivery_status = 'Late')::int), 2) AS late_rate_pct
FROM shipments
WHERE delivery_delay_days IS NOT NULL
GROUP BY shipment_mode
ORDER BY late_rate_pct DESC NULLS LAST;

-- 5) Top destination countries by shipment volume
SELECT
    country,
    COUNT(*) AS shipments,
    ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 2) AS share_pct
FROM shipments
GROUP BY country
ORDER BY shipments DESC
LIMIT 15;

-- 6) Top vendors by shipment volume
SELECT
    vendor,
    COUNT(*) AS shipments,
    ROUND(SUM(line_item_value), 2) AS line_item_value_usd
FROM shipments
GROUP BY vendor
ORDER BY shipments DESC
LIMIT 15;

-- 7) Freight efficiency where both weight and freight are numeric
SELECT
    shipment_mode,
    COUNT(*) AS usable_shipments,
    ROUND(AVG(freight_cost_usd / NULLIF(weight_kg, 0)), 2) AS avg_freight_per_kg,
    ROUND((PERCENTILE_CONT(0.5) WITHIN GROUP (
        ORDER BY freight_cost_usd / NULLIF(weight_kg, 0)
    ))::numeric, 2) AS median_freight_per_kg
FROM shipments
WHERE freight_cost_usd > 0 AND weight_kg > 0
GROUP BY shipment_mode
ORDER BY median_freight_per_kg DESC NULLS LAST;

-- 8) Review extreme delivery-date differences rather than deleting them
SELECT
    shipment_id,
    country,
    vendor,
    shipment_mode,
    scheduled_delivery_date,
    delivered_date,
    delivery_delay_days
FROM shipments
WHERE extreme_delay_flag = TRUE
ORDER BY ABS(delivery_delay_days) DESC;

-- 9) Delivery status mix by year
SELECT
    EXTRACT(YEAR FROM delivered_date)::int AS delivery_year,
    delivery_status,
    COUNT(*) AS shipments
FROM shipments
WHERE delivered_date IS NOT NULL
GROUP BY 1, 2
ORDER BY 1, 2;

-- 10) Product groups with the largest line-item value
SELECT
    product_group,
    COUNT(*) AS shipments,
    ROUND(SUM(line_item_value), 2) AS total_line_item_value_usd,
    ROUND(AVG(line_item_value), 2) AS avg_line_item_value_usd
FROM shipments
GROUP BY product_group
ORDER BY total_line_item_value_usd DESC NULLS LAST;
