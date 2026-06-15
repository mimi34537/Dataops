
  create view "oltp"."public_staging"."stg_customers__dbt_tmp"
    
    
  as (
    select
    customer_id,
    country,
    signup_date,
    segment
from public.customers
  );