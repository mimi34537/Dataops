select
    o.order_id,
    o.customer_id,
    c.country,
    c.segment,
    o.store_id,
    o.order_date,
    o.status
from {{ ref('stg_orders') }} o
left join {{ ref('stg_customers') }} c
    on o.customer_id = c.customer_id
