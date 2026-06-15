
    
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select country
from "oltp"."public_marts"."mart_orders_by_country"
where country is null



  
  
      
    ) dbt_internal_test