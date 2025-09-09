{{
  config({    
    "materialized": "table",
    "alias": "s3_to_table",
    "database": "qa_prakhar_database",
    "schema": "main"
  })
}}

WITH complex2_csv_1 AS (

  SELECT *
  
  FROM {{ prophecy_tmp_source('tmp_pipelines', 'complex2_csv_1') }}

),

Reformat_3 AS (

  SELECT * 
  
  FROM complex2_csv_1 AS in0

)

SELECT *

FROM Reformat_3
