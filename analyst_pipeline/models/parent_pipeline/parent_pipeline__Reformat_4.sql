{{
  config({    
    "materialized": "ephemeral",
    "database": "qa_team",
    "schema": "qa_database"
  })
}}

WITH customer_data_with_details AS (

  SELECT *
  
  FROM {{ ref('parent_pipeline__customer_data_with_details')}}

),

Reformat_4 AS (

  SELECT 
    Name AS Name,
    Age AS Age,
    City AS City,
    Salary AS Salary,
    c_int AS c_int,
    c_boolean AS c_boolean,
    c_tinyint AS c_tinyint,
    c_smallint AS c_smallint,
    c_bigint AS c_bigint,
    c_double AS c_double,
    c_array AS c_array,
    c_struct AS c_struct,
    c_struct_state AS c_struct_state,
    c_struct_pin AS c_struct_pin,
    c_struct_city AS c_struct_city
  
  FROM customer_data_with_details AS in0

)

SELECT *

FROM Reformat_4
