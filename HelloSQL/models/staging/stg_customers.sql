WITH source AS (

  {#-
  Normally we would select from the table here, but we are using seeds to load
  our data in this project
  #}
  SELECT * 
  
  FROM {{ ref('raw_customers')}}

),

renamed AS (

  {#Standardizes customer data by renaming fields for consistency.#}
  SELECT 
    id AS customer_id,
    first_name AS First,
    last_name AS Last
  
  FROM source

)

SELECT *

FROM renamed
