import streamlit as st
import pandas as pd
import plotly.express as px
import joblib

# ==========================================
# 1. PAGE SETUP & GLOBAL THEMING
# ==========================================
st.set_page_config(
    page_title="Global Agrifood Intelligence Platform",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# 2. EXECUTIVE CLUSTER DICTIONARY MAPPING
# ==========================================
# This maps the raw cluster numbers from your notebook to our professional executive titles
CLUSTER_MAP = {
    0: "Industrialized & Supply Chain Input-Dominant Systems",
    1: "Diversified Agribusiness & Emerging Market Powerhouses",
    2: "Primary Production & Traditional Agrarian Economies",
    3: "Advanced High-Tech & Post-Industrial Agrifood Systems"
}

# Add your Colab cluster profile percentage averages here
ARCHETYPE_PROFILES = {
    0: {"Farm_Gate_Share": 8.90, "Industrial_Share": 75.65, "Consumer_Retail_Share": 8.33, "Logistics_Processing_Share": 7.13},
    1: {"Farm_Gate_Share": 32.91, "Industrial_Share": 21.65, "Consumer_Retail_Share": 34.77, "Logistics_Processing_Share": 10.67},
    2: {"Farm_Gate_Share": 67.97, "Industrial_Share": 11.62, "Consumer_Retail_Share": 14.41, "Logistics_Processing_Share": 6.00},
    3: {"Farm_Gate_Share": 22.88, "Industrial_Share": 44.59, "Consumer_Retail_Share": 19.17, "Logistics_Processing_Share": 13.36}
}

# ==========================================
# 3. SIDEBAR NAVIGATION & INTERFACE
# ==========================================
with st.sidebar:
    st.title("🌍 Agrifood Intelligence")
    st.subheader("Decadal Macroeconomic Analysis")
    st.markdown("---")
    
    # Recruiter Briefing Info Box
    st.info(
        "This enterprise platform utilizes unsupervised machine learning (K-Means) "
        "to profile and stress-test global agrifood supply chain carbon risk "
        "across 165 nations using decade-averaged UN FAO data."
    )
    
    st.markdown("---")
    st.subheader("Navigation")
    # This radio button controller lets us seamlessly switch between tabs
    app_mode = st.radio(
        "Go to page:",
        ["📍 Tab 1: Macroeconomic Archetypes", "🛞 Tab 2: Supply Chain Simulator"]
    )
    st.markdown("---")

# ==========================================
# 4. HIGH-PERFORMANCE DATA LOADING LAYER
# ==========================================
@st.cache_data # Tells Streamlit to store data in memory so the app stays ultra-fast
def load_data():
    df = pd.read_csv("final_food_system_clusters.csv")
    # Create a nice human-readable column right away by mapping our dictionary
    df['Archetype_Name'] = df['Cluster_Labels'].map(CLUSTER_MAP)
    return df

try:
    df_app = load_data()
except FileNotFoundError:
    st.error("⚠️ Data asset 'final_food_system_clusters.csv' not found. Please ensure it is saved inside this exact same directory folder.")
    st.stop()

# ==========================================
# 5. APP CONTROLLER (TAB ROUTING) - MASTER TAB 1
# ==========================================
if app_mode == "📍 Tab 1: Macroeconomic Archetypes":
    st.title("📍 Global Macroeconomic Archetypes")
    st.markdown("An interactive spatial audit of global food supply chain structures independent of population scale.")
    st.write("---")
    
    # ─── PART 2: INTERACTIVE MAP ───
    st.subheader("🗺️ Global Archetype Distribution Map")
    
    fig_map = px.choropleth(
        df_app,
        locations="Area", 
        locationmode="country names",
        color="Archetype_Name",            
        hover_name="Area",                 
        projection="natural earth",
        color_discrete_sequence=px.colors.qualitative.Safe
    )
    
    fig_map.update_layout(
        margin={"r":0,"t":10,"l":0,"b":0},
        legend=dict(
            title="Supply Chain Structural Archetypes",
            orientation="h",
            yanchor="top",
            y=-0.05,
            xanchor="center",
            x=0.5
        )
    )
    
    st.plotly_chart(fig_map, use_container_width=True)
    st.write("---")
    
    # ─── PART 3: COUNTRY DEEP-DIVE EXPLORER ───
    st.subheader("🔍 Country Executive Profile Explorer")
    
    country_list = sorted(df_app['Area'].unique())
    selected_country = st.selectbox("Select a Country for an Executive Audit:", country_list)
    
    country_data = df_app[df_app['Area'] == selected_country].iloc[0]
    
    st.markdown(f"""
    <div style="background-color:#1E1E1E; padding:15px; border-radius:10px; border-left: 5px solid #FF4B4B;">
        <h4 style="margin:0; color:#FFFFFF;">🎯 Assigned Archetype Profile:</h4>
        <p style="margin:5px 0 0 0; color:#FF4B4B; font-size:18px; font-weight:bold;">{country_data['Archetype_Name']}</p>
    </div>
    """, unsafe_allow_html=True)
    st.write("") 
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(
            label="🌍 Total Food System Emissions (Baseline)", 
            value=f"{country_data['Total_Food_System_Emissions']:,.2f} kt CO2eq"
        )
    with col2:
        st.metric(
            label="👤 Total Footprint Per Capita", 
            value=f"{country_data['Total_Food_System_Per_Capita']:,.2f} Tonnes / Person"
        )
        
    st.write("") 
    
    breakdown_data = {
        "Supply Chain Segment": [
            "🌾 Farm Gate Emissions", 
            "🚛 Logistics & Processing", 
            "🛒 Consumer Retail", 
            "🏭 Industrial Emissions"
        ],
        "Sector Raw Volume": [
            f"{country_data['Farm_Gate_Emissions']:,.2f} kt",
            f"{country_data['Logistics_Processing_Emissions']:,.2f} kt",
            f"{country_data['Consumer_Retail_Emissions']:,.2f} kt",
            f"{country_data['Industrial_Emissions']:,.2f} kt"
        ],
        "Sector Per Capita Footprint": [
            f"{country_data['Farm_Gate_Per_Capita']:,.2f} t/Person",
            f"{country_data['Logistics_Processing_Per_Capita']:,.2f} t/Person",
            f"{country_data['Consumer_Retail_Per_Capita']:,.2f} t/Person",
            f"{country_data['Industrial_Per_Capita']:,.2f} t/Person"
        ]
    }
    
    df_breakdown = pd.DataFrame(breakdown_data)
    st.markdown("##### 📊 Functional Sector Breakdown")
    st.dataframe(df_breakdown, use_container_width=True, hide_index=True)
    st.write("---")
    
    # ─── VISUAL DATA INSIGHTS LAYER ───
    st.write("") 
    st.markdown("##### 📊 Structural Profile Visualizations")
    
    chart_df = pd.DataFrame({
        "Sector": ["🌾 Farm Gate", "🚛 Logistics & Proc.", "🛒 Consumer Retail", "🏭 Industrial"],
        "Raw Volume (kt)": [
            country_data['Farm_Gate_Emissions'],
            country_data['Logistics_Processing_Emissions'],
            country_data['Consumer_Retail_Emissions'],
            country_data['Industrial_Emissions']
        ],
        "Per Capita (t/Person)": [
            country_data['Farm_Gate_Per_Capita'],
            country_data['Logistics_Processing_Per_Capita'],
            country_data['Consumer_Retail_Per_Capita'],
            country_data['Industrial_Per_Capita']
        ]
    })
    
    fig_pie = px.pie(
        chart_df, 
        values="Raw Volume (kt)", 
        names="Sector", 
        title="Composition of Raw Volume (kt)", 
        color_discrete_sequence=px.colors.qualitative.Safe
    )
    fig_pie.update_layout(showlegend=True, margin=dict(t=30, b=10, l=10, r=10),
                          legend=dict(orientation="h",yanchor="top",y=-0.1,xanchor="center",
                                      x=0.5)
                         )
    fig_pie.update_traces(textinfo='percent',textfont=dict(size=14,color='white',family='sans-serif'))
    
    fig_bar = px.bar(
        chart_df, 
        x="Per Capita (t/Person)", 
        y="Sector", 
        orientation="h", 
        title="Intensity Per Capita (t/Person)", 
        color="Sector", 
        color_discrete_sequence=px.colors.qualitative.Safe
    )
    fig_bar.update_layout(showlegend=False, yaxis_title=None, margin=dict(t=30, b=10, l=10, r=10))
    
    col_chart1, col_chart2 = st.columns(2)
    with col_chart1:
        st.plotly_chart(fig_pie, use_container_width=True)
    with col_chart2:
        st.plotly_chart(fig_bar, use_container_width=True)
        
    st.write("---")

elif app_mode == "🛞 Tab 2: Supply Chain Simulator":
    st.title("🛞 Supply Chain Stress-Test Simulator")
    st.markdown("Live infrastructure optimization simulation and machine learning cluster re-classification.")
    st.write("---")
    
    # ─── STEP 1: TARGET COUNTRY SELECTION & METADATA LEDGER ───
    # Safely extract unique territories available within the loaded dataframe asset
    sim_country_list = sorted(df_app['Area'].unique())
    sim_country = st.selectbox("Select Target Country for Policy Simulation:", sim_country_list, key="sim_country_select")
    
    # Isolate the original row vector for mathematical baseline manipulation
    sim_data = df_app[df_app['Area'] == sim_country].iloc[0]
    
    # Replicating your branded Tab 1 HTML Container Box layout pattern
    st.markdown(f"""
    <div style="background-color:#1E1E1E; padding:15px; border-radius:10px; border-left: 5px solid #FF4B4B;">
        <h4 style="margin:0; color:#FFFFFF;">🎯 Active Simulation Base Profile:</h4>
        <p style="margin:5px 0 0 0; color:#FF4B4B; font-size:18px; font-weight:bold;">{sim_data['Archetype_Name']}</p>
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    
    # Extract Cluster ID and Fetch Peer Group Profile Percentages
    current_cluster_id = int(sim_data['Cluster_Labels'])
    current_peer_profile = ARCHETYPE_PROFILES[current_cluster_id]
    # Dynamic Cohort Benchmark Table Display
    st.markdown(f"##### 📊 {sim_country} Structural Share vs. Archetype Peer Average")
    st.caption(
        "This benchmark matrix evaluates how your selected country's baseline emission distribution "
        "compares to its global structural peers before policy overrides are applied."
    )
    st.markdown(f"""
| Supply Chain Sector | **{sim_country} Baseline Share** | **Archetype Peer Avg** |
| :--- | :---: | :---: |
| 🌾 Farm Gate | {sim_data['Farm_Gate_Share']:.1f}% | {current_peer_profile['Farm_Gate_Share']:.1f}% |
| 🧪 Industrial Inputs | {sim_data['Industrial_Share']:.1f}% | {current_peer_profile['Industrial_Share']:.1f}% |
| 🛒 Consumer Retail | {sim_data['Consumer_Retail_Share']:.1f}% | {current_peer_profile['Consumer_Retail_Share']:.1f}% |
| 🚛 Logistics & Proc. | {sim_data['Logistics_Processing_Share']:.1f}% | {current_peer_profile['Logistics_Processing_Share']:.1f}% |
""")
    st.markdown("---")
    
    # ─── STEP 2: INTERACTIVE POLICY INTERVENTION CONTROL PANEL ───
    st.markdown("### 🎛️ Policy Intervention Sliders")
    st.info("💡 Scale sectors below. Dragging to the left (e.g., 80%) simulates a reduction; dragging right simulates growth.")
    
    col_slide1, col_slide2 = st.columns(2)
    
    with col_slide1:
        farm_gate_pct = st.slider(
            "🌾 Farm Gate Optimization (% of Baseline)", 
            min_value=10, max_value=150, value=100, step=5,
            help="Simulates field-level interventions like methane-reducing feed or optimized rice paddies."
        )
        logistics_pct = st.slider(
            "🚛 Logistics & Processing Optimization (% of Baseline)", 
            min_value=10, max_value=150, value=100, step=5,
            help="Simulates cold-chain solar conversion, transit fuel switches, and manufacturing waste cuts."
        )
        
    with col_slide2:
        retail_pct = st.slider(
            "🛒 Consumer Retail Optimization (% of Baseline)", 
            min_value=10, max_value=150, value=100, step=5,
            help="Simulates commercial cooling efficiency, grocery grid choices, and household waste drops."
        )
        industrial_pct = st.slider(
            "🏭 Industrial Inputs Optimization (% of Baseline)", 
            min_value=10, max_value=150, value=100, step=5,
            help="Simulates alternative green fertilizer adoption and chemical production constraints."
        )
        
    st.write("---")
    
    # ─── STEP 3: DYNAMIC SIMULATION MATH ENGINE ───
    # Multiplies baseline values by slider percentages using the exact dataset columns verified in Colab
    sim_farm = sim_data['Farm_Gate_Emissions'] * (farm_gate_pct / 100.0)
    sim_log = sim_data['Logistics_Processing_Emissions'] * (logistics_pct / 100.0)
    sim_ret = sim_data['Consumer_Retail_Emissions'] * (retail_pct / 100.0)
    sim_ind = sim_data['Industrial_Emissions'] * (industrial_pct / 100.0)
    
    # Aggregate dynamic values inside local memory
    sim_total_emissions = sim_farm + sim_log + sim_ret + sim_ind
    base_total_emissions = sim_data['Total_Food_System_Emissions']
    
    # Compute relative and absolute variances between baseline and simulation profiles
    net_change = sim_total_emissions - base_total_emissions
    pct_change = (net_change / base_total_emissions) * 100.0
    
    # ─── STEP 4: EXECUTIVE LIVE SCENARIO METRICS ───
    st.markdown("### 🎯 Live Simulated Scenario Impact")
    col_met1, col_met2, col_met3 = st.columns(3)
    
    with col_met1:
        st.metric(
            label="📋 Baseline Total Emissions",
            value=f"{base_total_emissions:,.2f} kt"
        )
    with col_met2:
        st.metric(
            label="🚀 Simulated New Total",
            value=f"{sim_total_emissions:,.2f} kt"
        )
    with col_met3:
        st.metric(
            label="📉 Net Carbon Variance",
            value=f"{net_change:,.2f} kt",
            delta=f"{pct_change:,.2f}%",
            delta_color="inverse"  # Keeps styling intuitive: carbon decreases show green, increases show red
        )
        
    st.write("---")
    
    # ─── STEP 5: COMPARATIVE VISUAL SCENARIO LEDGER ───
    st.markdown("##### 🏛️ Structural Baseline vs. Policy Optimization Scenario")
    
    comparison_df = pd.DataFrame({
        "Supply Chain Segment": ["🌾 Farm Gate", "🚛 Logistics & Proc.", "🛒 Consumer Retail", "🏭 Industrial"],
        "Baseline Profile (kt)": [
            sim_data['Farm_Gate_Emissions'],
            sim_data['Logistics_Processing_Emissions'],
            sim_data['Consumer_Retail_Emissions'],
            sim_data['Industrial_Emissions']
        ],
        "Simulated Scenario (kt)": [sim_farm, sim_log, sim_ret, sim_ind]
    })
    
    st.dataframe(comparison_df, use_container_width=True, hide_index=True)
    
    # ─── STEP 6: BACK-TO-BACK DELTA HISTOGRAM GRAPHICS ───
    melted_df = comparison_df.melt(
        id_vars="Supply Chain Segment",
        value_vars=["Baseline Profile (kt)", "Simulated Scenario (kt)"],
        var_name="Scenario Type",
        value_name="Emissions Volume (kt)"
    )
    
    fig_sim_bar = px.bar(
        melted_df,
        x="Supply Chain Segment",
        y="Emissions Volume (kt)",
        color="Scenario Type",
        barmode="group",
        title="Side-by-Side Impact Matrix Comparison (kt CO2eq)",
        color_discrete_sequence=["#1F77B4", "#FF7F0E"]  # Deep Blue vs Actionable Mitigation Orange
    )
    
    fig_sim_bar.update_layout(
        margin=dict(t=40, b=20, l=20, r=20), 
        legend=dict(orientation="h", y=1.1, x=0.3)
    )
    st.plotly_chart(fig_sim_bar, use_container_width=True)

























