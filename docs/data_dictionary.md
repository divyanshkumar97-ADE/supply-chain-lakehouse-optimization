# Data dictionary

## Shipment events
| Field | Meaning | Example |
|---|---|---|
| event_id | Stable source event identifier | EVT-00000001-1 |
| shipment_id | Shipment business key | SHP-00000001 |
| order_id | Related order | ORD-00000001 |
| event_type | Lifecycle state | IN_TRANSIT |
| event_timestamp | Time event occurred | ISO-8601 timestamp |
| warehouse_id | Warehouse code | WH-004 |
| source_system | Origin system | TMS_B |
| source_batch_id | Batch identifier | BATCH-00001 |

## Inventory
| Field | Meaning |
|---|---|
| inventory_id | Source snapshot row identifier |
| product_id | Product / SKU |
| warehouse_id | Warehouse |
| on_hand_quantity | Quantity physically available; must be non-negative |
| reorder_threshold | Reorder threshold; must be non-negative |
| snapshot_timestamp | Snapshot effective time |

## Gold KPI definitions (to implement)
- **Delivery duration hours** = delivered timestamp − shipped timestamp.
- **Late delivery flag** = actual delivered timestamp > promised delivery timestamp. Add promised delivery time to the source contract before implementing this KPI.
- **Inventory risk flag** = on-hand quantity <= reorder threshold.
- **Stockout flag** = on-hand quantity = 0.
