{{
  config({    
    "materialized": "ephemeral",
    "database": "qa_team",
    "schema": "qa_orchestration"
  })
}}

WITH raw_payments AS (

  SELECT * 
  
  FROM {{ ref('raw_payments')}}

),

raw_customers AS (

  SELECT * 
  
  FROM {{ ref('raw_customers')}}

),

payment_details AS (

  {#Compiles payment details by merging raw and staged payment data.#}
  SELECT 
    in0.id AS id,
    in0.order_id AS order_id,
    in0.payment_method AS payment_method,
    in0.amount AS amount
  
  FROM raw_payments AS in0
  INNER JOIN raw_customers AS in1
     ON true

)

SELECT *

FROM payment_details
