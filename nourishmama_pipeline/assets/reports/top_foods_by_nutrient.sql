/* @bruin
name: reports.top_foods_by_nutrient
type: duckdb.sql
materialization:
  type: table
depends:
  - marts.nutrient_rankings
@bruin */

select
    nutrient,
    food_name,
    category,
    value_per_100g,
    unit,
    nutrient_rank
from marts.nutrient_rankings
where nutrient_rank <= 5
order by nutrient, nutrient_rank