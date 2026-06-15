select
    country,
    segment,
    count(order_id) as total_orders
from {{ ref('int_orders_customers') }}
group by country, segment
