
  create view "oltp"."public_intermediate"."int_orders_customers__dbt_tmp"
    
    
  as (
    select
    o.order_id,
    o.customer_id,
    c.country,
    c.segment,
    o.store_id,
    o.order_date,
    o.status
from "oltp"."public_staging"."stg_orders" o
left join "oltp"."public_staging"."stg_customers" c
    on o.customer_id = c.customer_id
  );