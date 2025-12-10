{{
  config({    
    "materialized": "ephemeral",
    "database": "qa_team",
    "schema": "qa_orchestration"
  })
}}

WITH stg_payments_1 AS (

  SELECT * 
  
  FROM {{ ref('stg_payments')}}

),

raw_payments AS (

  SELECT * 
  
  FROM {{ ref('raw_payments')}}

),

payment_details AS (

  {#Compiles payment details by merging raw and staged payment data.#}
  SELECT 
    in0.id AS id,
    in0.order_id AS order_id,
    in0.payment_method AS payment_method,
    in0.amount AS amount
  
  FROM raw_payments AS in0
  INNER JOIN stg_payments_1 AS in1
     ON true

)

SELECT *

FROM payment_details
