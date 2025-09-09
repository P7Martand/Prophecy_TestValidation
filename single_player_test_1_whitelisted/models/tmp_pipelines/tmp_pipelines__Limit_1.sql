{{
  config({    
    "materialized": "ephemeral",
    "database": "database",
    "schema": "schema"
  })
}}

WITH checkxa3_csv_1 AS (

  SELECT *
  
  FROM {{ prophecy_tmp_source('tmp_pipelines', 'checkxa3_csv_1') }}

),

Limit_1 AS (

  SELECT * 
  
  FROM checkxa3_csv_1 AS in0
  
  LIMIT 10

)

SELECT *

FROM Limit_1
