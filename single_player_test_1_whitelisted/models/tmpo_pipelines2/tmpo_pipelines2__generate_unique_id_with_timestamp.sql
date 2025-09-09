{{
  config({    
    "materialized": "ephemeral",
    "database": "database",
    "schema": "schema"
  })
}}

WITH Table_0 AS (

  SELECT * 
  
  FROM {{ ref('seedraw')}}

),

generate_unique_id_with_timestamp AS (

  SELECT 
    uuid() AS unique_id,
    current_localtimestamp() AS current_time;

)

SELECT *

FROM generate_unique_id_with_timestamp
