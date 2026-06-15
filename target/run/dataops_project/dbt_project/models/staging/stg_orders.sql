
  create view "oltp"."public_staging"."stg_orders__dbt_tmp"
    
    
  as (
    select
    order_id,
    customer_id,
    store_id,
    order_date,
    status
from public.orders
  );