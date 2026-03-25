/* @bruin
name: marts.nutrient_rankings
type: duckdb.sql
materialization:
  type: table
depends:
  - staging.stg_mother_nutrition
@bruin */

select
    food_id,
    food_name,
    category,
    nutrient,
    value_per_100g,
    unit,
    rank() over (
        partition by nutrient
        order by value_per_100g desc
    ) as nutrient_rank,
    rank() over (
        partition by nutrient, category
        order by value_per_100g desc
    ) as category_nutrient_rank
from staging.stg_mother_nutrition