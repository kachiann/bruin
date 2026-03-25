/* @bruin
name: staging.stg_mother_nutrition
type: duckdb.sql
materialization:
  type: table
depends:
  - ingestion.mother_nutrition
@bruin */

select
    cast(food_id as integer) as food_id,
    trim(food_name) as food_name,
    trim(category) as category,
    trim(nutrient) as nutrient,
    cast(value_per_100g as double) as value_per_100g,
    trim(unit) as unit
from ingestion.mother_nutrition
where food_name is not null
  and nutrient is not null
  and value_per_100g is not null