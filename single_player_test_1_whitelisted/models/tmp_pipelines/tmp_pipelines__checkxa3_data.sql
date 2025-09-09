{{
  config({    
    "materialized": "table",
    "alias": "sftp_to_table",
    "database": "qa_prakhar_database",
    "schema": "qa_schema"
  })
}}

WITH checkxa3_csv_1 AS (

  SELECT *
  
  FROM {{ prophecy_tmp_source('tmp_pipelines', 'checkxa3_csv_1') }}

),

checkxa3_data AS (

  SELECT *
  
  FROM checkxa3_csv_1
  
  WHERE id == 1

)

SELECT *

FROM checkxa3_data
