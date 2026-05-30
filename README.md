# 🌍 Global Agri-Food Intelligence Platform
> **An Independent Data Science & Interactive Simulation Project**

[Live Streamlit App Link](https://global-agrifood-intelligence-3x3c8mujctpycqx8u3oetx.streamlit.app/) | [Jupyter Notebook Pipeline](https://nbviewer.org/github/ShilpaLRAnalyst/global-agrifood-intelligence/blob/main/Global_Agri_Food_Supply_Chains_A_Decadal_Macro_Economic_Archetype_Analysis.ipynb)

This repository contains an end-to-end data project designed to analyze greenhouse gas (GHG) emissions across global agrifood supply chains. Using historical data for 165 countries, the project uses unsupervised machine learning to group nations into different structural archetypes and features an interactive web dashboard for real-time scenario simulation.

---

## 🛠️ Architecture & Tech Stack

This project decouples data processing from the presentation layer to ensure modularity and scalability.

* **Data Processing & ML Pipeline:** Python, Pandas, NumPy, Scikit-Learn (K-Means, PCA)
* **Model Serialization:** Joblib
* **Deployment & UI:** Streamlit (Python-based interactive dashboard)
* **Data Visualization:** Plotly, Matplotlib, Seaborn

---

## 🧠 Methodology & Machine Learning Insights

To group 165 countries into structural archetypes, an unsupervised machine learning pipeline was constructed using K-Means Clustering, validated by Principal Component Analysis (PCA).

### 1. Feature Engineering & Inputs
The model evaluates greenhouse gas (GHG) emissions across the entire four-sector agricultural supply chain:
1. **Farm Gate** (On-farm production activities)
2. **Agro-Industrial** (Fertilizer manufacturing, machinery, pesticide production)
3. **Logistics & Processing** (Transport, cold chains, packaging)
4. **Consumer & Retail** (Waste management, household consumption, retail footprint)

### 2. Hyperparameter Tuning & Dimensionality Reduction
* **Choosing $K$:** Initial inertia screening via the **Elbow Method** indicated an optimal inflection point at $K = 4$, which was rigorously validated using **Silhouette Analysis** to ensure maximum intra-cluster density.
* **Variance Explained:** To visualize the high-dimensional supply chain data, **Principal Component Analysis (PCA)** was applied. **99.2% of total variance** was successfully captured by the primary components, proving the structural distinctions are highly robust.

### 3. Cluster Structural Archetypes
The algorithm successfully segmented the 165 nations into four distinct global archetypes, driven heavily by variances in **Farm Gate** and **Agro-Industrial** emissions:

| Cluster | Archetype Name | Core Characteristics |
| :---: | :--- | :--- |
| **0** | Industrialized & Supply Chain Input-Dominant Systems | High agro-industrial footprint; heavily reliant on intensive synthetic inputs and modernized supply chain logistics. |
| **1** | Diversified Agribusiness & Emerging Market Powerhouses | Rapidly scaling agricultural sectors blending massive primary production volumes with evolving processing industries. |
| **2** | Primary Production & Traditional Agrarian Economies | Emissions heavily dominated by Farm Gate activities; characteristic of localized, production-heavy, and traditional agricultural practices. |
| **3** | Advanced High-Tech & Post-Industrial Agrifood Systems | Decoupled primary production emissions with highly optimized, service-and-retail-heavy food system profiles. |

---

## 📂 Project Directory Structure

To keep the repository clean, the codebase is separated into data processing and application layers:

```text
global-agrifood-intelligence/
├── data/
│   └── final_food_system_clusters.csv          # Processed dataset with calculated cluster badges
├── models/
│   └── trained_kmeans_model.joblib            # Pre-trained K-Means model object
├── agrifood_app.py                            # Interactive Streamlit application code
├── requirements.txt                           # Libraries required to run the dashboard
└── Global_Agri_Food_Supply_Chains_A_Decadal_Macro_Economic_Archetype_Analysis.ipynb # Core ML pipeline
