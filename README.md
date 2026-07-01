# 🌍 Global Agri-Food Intelligence Platform
> **An Independent Data Science & Interactive Simulation Project**

[Live Streamlit App Link](https://global-agrifood-intelligence-3x3c8mujctpycqx8u3oetx.streamlit.app/) | [Jupyter Notebook Pipeline](https://nbviewer.org/github/ShilpaLRAnalyst/global-agrifood-intelligence/blob/main/Global_Agri_Food_Supply_Chains_A_Decadal_Macro_Economic_Archetype_Analysis.ipynb) | [Google Colab Mirror](https://colab.research.google.com/drive/1lGoPeHN7-w1htfgYYUel28KJNbeiYfsY?usp=sharing)

An end-to-end data science project built to analyze greenhouse gas (GHG) emissions across global agrifood supply chains. Using historical data for 165 countries, the pipeline applies unsupervised machine learning to cluster nations into distinct emission profiles and features an interactive Streamlit dashboard for real-time scenario simulation.

 📊 **Data Source:** Primary macro-economic emissions data sourced from the UN Food and Agriculture Organization (FAO), utilized via the global agrifood dataset compiled by Alessandro on Kaggle.

---

## 🛠️ Architecture & Tech Stack

Built with a decoupled architecture separating data processing from the presentation layer to ensure clean modularity and scalability.

* **Data Processing & ML Pipeline:** Python, Pandas, NumPy, Scikit-Learn (K-Means, PCA)
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
* **Strategic Cluster Selection ($K=4$):** Although the Elbow Method and Silhouette Analysis suggested $K = 3$, the final configuration was set to $K = 4$. This adjustment was chosen to better capture distinct macroeconomic variations across the 165 nations, providing a more practical and insightful distribution of global agrifood systems for the simulation dashboard.
* **Variance Explained:** To visualize the high-dimensional supply chain data, **Principal Component Analysis (PCA)** was applied. **99.2% of total variance** was successfully captured by the primary components, proving the structural distinctions are highly robust.

### 3. Cluster Structural Archetypes
The K-Means algorithm segmented the 165 nations into four distinct emission profiles based on their agrifood supply chain characteristics:

| Cluster | Archetype Name | Core Characteristics |
| :---: | :--- | :--- |
| **0** | Industrialized & Supply Chain Input-Dominant Systems | High agro-industrial footprint; heavily driven by synthetic inputs (fertilizers) and modernized supply chain logistics. |
| **1** | Diversified Agribusiness & Emerging Market Powerhouses |High primary production volumes mixed with rapidly expanding food processing industries. |
| **2** | Primary Production & Traditional Agrarian Economies |Emissions are heavily dominated by Farm Gate (on-farm) activities, reflecting localized, traditional agricultural practices. |
| **3** | Advanced High-Tech & Post-Industrial Agrifood Systems | Driven by downstream processing, manufacturing, and mature retail distribution and stable primary farm production. |

---

## 📂 Project Directory Structure

To keep the repository clean, the codebase is separated into data processing and application layers:

```text
global-agrifood-intelligence/
├── data/
│   └── final_food_system_clusters.csv          # Processed dataset with calculated cluster badges
|              
├── agrifood_app.py                            # Interactive Streamlit application code
├── requirements.txt                           # Libraries required to run the dashboard
└── Global_Agri_Food_Supply_Chains_A_Decadal_Macro_Economic_Archetype_Analysis.ipynb # Core ML pipeline
