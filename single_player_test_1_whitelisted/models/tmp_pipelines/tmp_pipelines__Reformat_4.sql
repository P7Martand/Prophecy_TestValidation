{{
  config({    
    "materialized": "table",
    "alias": "sharepoint_to_tables",
    "database": "qa_prakhar_database",
    "schema": "qa_schema"
  })
}}

WITH testresults_csv_1 AS (

  SELECT *
  
  FROM {{ prophecy_tmp_source('tmp_pipelines', 'testresults_csv_1') }}

),

Reformat_4 AS (

  SELECT *
  
  FROM testresults_csv_1 AS in0

)

SELECT *

FROM Reformat_4
