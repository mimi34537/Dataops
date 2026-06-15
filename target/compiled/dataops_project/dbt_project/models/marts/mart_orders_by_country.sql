select
    country,
    segment,
    count(order_id) as total_orders
from "oltp"."public_intermediate"."int_orders_customers"
group by country, segment