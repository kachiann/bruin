# 🌱 NourishMama

**A Bruin-powered data pipeline and dashboard for nutrition insights for first-time mums and nursing mothers**

Built from a real-life need as a first-time mum, NourishMama transforms nutrition data into simple, actionable insights to support recovery, breastfeeding, and healthy baby feeding choices.

---

## 💡 Problem

As a first-time mum, I wanted a simple way to understand which foods provide the nutrients needed for recovery, breastfeeding, and baby development.

However, nutrition data is often scattered and not easy to explore in a structured way.

**NourishMama** solves this by building an end-to-end data pipeline that transforms nutrition data into actionable insights.

---

## 🚀 Project Overview

This project builds a complete data platform using **Bruin** to:

- Ingest nutrition data
- Transform and model it into analytics-ready tables
- Generate insights on nutrient-rich foods
- Visualize results in an interactive dashboard

---

## ⚙️ Tech Stack

- **Data Platform:** Bruin  
- **Processing & Storage:** DuckDB  
- **Transformations:** SQL (Bruin assets)  
- **Orchestration:** Bruin pipeline  
- **Dashboard:** Streamlit  
- **Language:** Python  

---

## 📦 Data Pipeline

### 🔹 Ingestion
- `ingestion.mother_nutrition`
- `ingestion.foods_seed` (demo)

### 🔹 Staging
- `staging.stg_mother_nutrition`

### 🔹 Marts
- `marts.nutrient_rankings`

### 🔹 Reports
- `reports.nutrient_category_distribution`
- `reports.top_foods_by_nutrient`

---

## 📊 Dashboard

The dashboard provides two key insights:

### 1️⃣ Nutrient Distribution by Category
- Shows how nutrients (e.g., calcium, iron) are distributed across food categories

### 2️⃣ Top Foods by Nutrient
- Highlights the top foods for each nutrient
- Helps identify nutrient-dense foods quickly

---

## ▶️ How to Run

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/nourishmama.git
cd nourishmama/bruin
```

### 2. Run the pipeline
```bash
bruin run nourishmama_pipeline
```

### 3. Launch the dashboard
```bash
cd nourishmama_pipeline
streamlit run app.py
```