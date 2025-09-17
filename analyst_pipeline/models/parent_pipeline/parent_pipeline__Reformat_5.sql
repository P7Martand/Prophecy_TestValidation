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

emptyDategen AS (

  SELECT * 
  
  FROM customer_data_with_details AS in0
  
  WHERE (Name LIKE '%Amrendra%' or Name LIKE '%Baahubali%')

),

Union_1 AS (

  SELECT * 
  
  FROM emptyDategen AS in0
  
  UNION
  
  SELECT * 
  
  FROM emptyDategen AS in1

),

Intersect_1 AS (

  SELECT * 
  
  FROM Union_1 AS in0
  
  INTERSECT
  
  SELECT * 
  
  FROM emptyDategen AS in1

),

Limit_1 AS (

  SELECT * 
  
  FROM emptyDategen AS in0
  
  LIMIT 1

),

Except_1 AS (

  SELECT * 
  
  FROM Intersect_1 AS in0
  
  EXCEPT
  
  SELECT * 
  
  FROM Limit_1 AS in1

),

Reformat_5 AS (

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
  
  FROM Except_1 AS in0

)

SELECT *

FROM Reformat_5
