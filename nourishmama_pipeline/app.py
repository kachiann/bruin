import duckdb
import pandas as pd
import streamlit as st

DB_PATH = "nourishmama.duckdb"

st.set_page_config(page_title="NourishMama Dashboard", layout="wide")

st.title("NourishMama")
st.subheader("Nutrition insights for first-time mums and nursing mothers")

@st.cache_data
def load_data():
    con = duckdb.connect(DB_PATH, read_only=True)

    nutrient_category_distribution = con.execute("""
        SELECT *
        FROM reports.nutrient_category_distribution
    """).df()

    top_foods_by_nutrient = con.execute("""
        SELECT *
        FROM reports.top_foods_by_nutrient
    """).df()

    con.close()
    return nutrient_category_distribution, top_foods_by_nutrient


dist_df, top_df = load_data()

st.markdown("Explore nutrient-rich foods by category and discover top foods for key nutrients.")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Nutrient distribution by category")

    nutrient_options = sorted(dist_df["nutrient"].unique())
    selected_nutrient = st.selectbox(
        "Select a nutrient",
        nutrient_options,
        index=0,
        key="dist_nutrient"
    )

    filtered_dist = dist_df[dist_df["nutrient"] == selected_nutrient].copy()
    filtered_dist = filtered_dist.sort_values("avg_value_per_100g", ascending=False)

    st.bar_chart(
        filtered_dist.set_index("category")["avg_value_per_100g"]
    )

    st.dataframe(filtered_dist, use_container_width=True)

with col2:
    st.markdown("### Top foods by nutrient")

    nutrient_options_top = sorted(top_df["nutrient"].unique())
    selected_top_nutrient = st.selectbox(
        "Select a nutrient for top foods",
        nutrient_options_top,
        index=0,
        key="top_nutrient"
    )

    filtered_top = top_df[top_df["nutrient"] == selected_top_nutrient].copy()
    filtered_top = filtered_top.sort_values("nutrient_rank", ascending=True)

    chart_df = filtered_top[["food_name", "value_per_100g"]].set_index("food_name")
    st.bar_chart(chart_df["value_per_100g"])

    st.dataframe(filtered_top, use_container_width=True)

st.markdown("---")
st.caption("Built with Bruin + DuckDB + Streamlit")
