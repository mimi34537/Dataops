
  
    

  create  table "oltp"."public_marts"."mart_orders_by_country__dbt_tmp"
  
  
    as
  
  (
    select
    country,
    segment,
    count(order_id) as total_orders
from "oltp"."public_intermediate"."int_orders_customers"
group by country, segment
  );
  