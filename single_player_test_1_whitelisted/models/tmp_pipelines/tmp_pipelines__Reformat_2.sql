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

Reformat_2 AS (

  SELECT * 
  
  FROM checkxa3_csv_1 AS in0

)

SELECT *

FROM Reformat_2
