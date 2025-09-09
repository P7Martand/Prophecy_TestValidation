{{
  config({    
    "materialized": "ephemeral",
    "database": "database",
    "schema": "schema"
  })
}}

WITH anything4_csv_1 AS (

  SELECT *
  
  FROM {{ prophecy_tmp_source('tmpo_pipelines2', 'anything4_csv_1') }}

),

Reformat_2 AS (

  SELECT * 
  
  FROM anything4_csv_1 AS in0

)

SELECT *

FROM Reformat_2
