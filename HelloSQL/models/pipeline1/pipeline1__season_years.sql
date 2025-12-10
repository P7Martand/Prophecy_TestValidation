{{
  config({    
    "materialized": "ephemeral",
    "database": "qa_team",
    "schema": "qa_orchestration"
  })
}}

WITH nba_games AS (

  SELECT * 
  
  FROM {{ source('qa_team_qa_orchestration', 'nba_games') }}

),

nba_games_season_scores AS (

  SELECT 
    season_year,
    home_team_score
  
  FROM nba_games

),

max_home_team_score AS (

  SELECT MAX(home_team_score) AS MAX_home_team_score_
  
  FROM nba_games

),

season_scores_with_max AS (

  SELECT 
    nba_games_season_scores.season_year,
    nba_games_season_scores.home_team_score,
    max_home_team_score.MAX_home_team_score_ AS MAX_home_team_score_
  
  FROM nba_games_season_scores
  LEFT JOIN max_home_team_score
     ON TRUE

),

max_score_games AS (

  SELECT * 
  
  FROM season_scores_with_max
  
  WHERE home_team_score = MAX_home_team_score_

),

season_scores AS (

  SELECT 
    season_year,
    home_team_score
  
  FROM max_score_games

),

season_years AS (

  SELECT season_year AS SEASON_YEAR
  
  FROM season_scores

)

SELECT *

FROM season_years
