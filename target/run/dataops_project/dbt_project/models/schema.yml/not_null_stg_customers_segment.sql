
    
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select segment
from "oltp"."public_staging"."stg_customers"
where segment is null



  
  
      
    ) dbt_internal_test