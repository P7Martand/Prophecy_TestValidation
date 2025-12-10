{{
  config({    
    "materialized": "ephemeral",
    "database": "qa_team",
    "schema": "qa_orchestration"
  })
}}

WITH raw_orders AS (

  SELECT * 
  
  FROM {{ ref('raw_orders')}}

),

raw_customers AS (

  SELECT * 
  
  FROM {{ ref('raw_customers')}}

),

orders_customers_join AS (

  SELECT 
    raw_orders.id AS ORDER_ID,
    raw_orders.user_id AS USER_ID,
    raw_orders.order_date AS ORDER_DATE,
    raw_orders.status AS STATUS,
    raw_customers.id AS CUSTOMER_ID,
    raw_customers.first_name AS FIRST_NAME,
    raw_customers.last_name AS LAST_NAME
  
  FROM raw_orders
  INNER JOIN raw_customers
     ON raw_orders.user_id = raw_customers.id

)

SELECT *

FROM orders_customers_join
