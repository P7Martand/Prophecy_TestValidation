{{
  config({    
    "materialized": "ephemeral",
    "database": "database",
    "schema": "schema"
  })
}}

WITH complex2_csv_1 AS (

  SELECT *
  
  FROM {{ prophecy_tmp_source('tmpo_pipelines2', 'complex2_csv_1') }}

),

Reformat_3 AS (

  SELECT * 
  
  FROM complex2_csv_1 AS in0

)

SELECT *

FROM Reformat_3
