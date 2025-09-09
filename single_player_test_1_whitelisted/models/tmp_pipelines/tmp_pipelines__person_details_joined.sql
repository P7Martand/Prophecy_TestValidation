{{
  config({    
    "materialized": "table",
    "alias": "tables_to_tables",
    "database": "qa_prakhar_database",
    "schema": "main"
  })
}}

WITH Table_0 AS (

  SELECT * 
  
  FROM {{ ref('seedraw')}}

),

Reformat_1 AS (

  SELECT * 
  
  FROM Table_0 AS in0

),

person_details_joined AS (

  SELECT 
    in1.id AS id,
    in1.first_name AS first_name,
    in1.lastname AS lastname,
    in1.address AS address
  
  FROM Table_0 AS in0
  INNER JOIN Reformat_1 AS in1
     ON true

)

SELECT *

FROM person_details_joined
