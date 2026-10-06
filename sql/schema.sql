-- Analytical PostgreSQL table used by the portfolio case study.
-- src/load_postgres.py creates/replaces this table from the cleaned CSV.

CREATE TABLE IF NOT EXISTS shipments (
    shipment_id BIGINT,
    country TEXT,
    vendor TEXT,
    shipment_mode TEXT,
    fulfill_via TEXT,
    vendor_inco_term TEXT,
    product_group TEXT,
    sub_classification TEXT,
    line_item_quantity NUMERIC,
    line_item_value NUMERIC,
    pack_price NUMERIC,
    unit_price NUMERIC,
    manufacturing_site TEXT,
    scheduled_delivery_date DATE,
    delivered_date DATE,
    weight_kg NUMERIC,
    freight_cost_usd NUMERIC,
    delivery_delay_days INTEGER,
    extreme_delay_flag BOOLEAN,
    delivery_status TEXT
);

CREATE INDEX IF NOT EXISTS idx_shipments_mode ON shipments (shipment_mode);
CREATE INDEX IF NOT EXISTS idx_shipments_country ON shipments (country);
CREATE INDEX IF NOT EXISTS idx_shipments_vendor ON shipments (vendor);
CREATE INDEX IF NOT EXISTS idx_shipments_delivery_status ON shipments (delivery_status);
