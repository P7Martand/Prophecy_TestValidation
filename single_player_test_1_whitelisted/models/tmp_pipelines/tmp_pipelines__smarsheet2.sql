{{
  config({    
    "materialized": "table",
    "alias": "sharepoint1_to_tables",
    "database": "qa_prakhar_database",
    "schema": "qa_schema"
  })
}}

WITH sharepoint_to_tables AS (

  SELECT * 
  
  FROM {{ source('qa_prakhar_database.qa_schema', 'sharepoint_to_tables') }}

)

SELECT *

FROM sharepoint_to_tables
