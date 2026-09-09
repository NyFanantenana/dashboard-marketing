import streamlit as st
import pandas as pd
import plotly.express as px

# Configuration de la page
st.set_page_config(page_title="Marketing & Customer Analytics Dashboard", layout="wide")

st.title("📊 Dashboard Marketing Interactif & Segmentation Client")
st.markdown("---")

# Données synthétisées issues des analyses M1 à M7
@st.cache_data
def load_summary_data():
    # Données des segments
    segments_df = pd.DataFrame({
        'Segment': ['VIP / Forts Acheteurs', 'Clients Occasionnels', 'Prospects Inactifs'],
        'Nombre_Clients': [1, 2, 2],
        'Age_Moyen': [25.0, 32.5, 27.0],
        'Depense_Moyenne': [155.0, 82.5, 0.0],
        'CA_Total': [310.0, 165.0, 0.0],
        'Budget_Allocations': [40, 35, 25]
    })
    
    # Données des canaux marketing
    marketing_df = pd.DataFrame({
        'Channel': ['Online', 'In-Store', 'Social', 'Email', 'TV'],
        'Budget': [1000.0, 1540.0, 2000.0, 500.0, 3000.0],
        'Taux_Conversion': [7.5, 20.0, 13.33, 5.0, 8.33],
        'CPA': [6.67, 15.0, 10.0, 10.0, 12.0]
    })
    
    # Performances modèles de prédiction
    models_df = pd.DataFrame({
        'Modele': ['Logistic Regression', 'Random Forest', 'XGBoost'],
        'Accuracy': [100.0, 100.0, 80.0]
    })
    
    return segments_df, marketing_df, models_df

df_seg, df_mkt, df_models = load_summary_data()

# Barre latérale - Filtres interactifs
st.sidebar.header("🎯 Filtres d'Analyse")
selected_segment = st.sidebar.multiselect(
    "Filtrer par Segment Client :",
    options=df_seg['Segment'].unique(),
    default=df_seg['Segment'].unique()
)

filtered_seg = df_seg[df_seg['Segment'].isin(selected_segment)]

# MÉTROLOGIE & KPIS GLOBAUX
st.subheader("💡 Indicateurs Clés de Performance (KPIs)")
kpi1, kpi2, kpi3, kpi4 = st.columns(4)

kpi1.metric("Chiffre d'Affaires Total", "475.00 €")
kpi2.metric("Panier Moyen Global", "95.00 €")
kpi3.metric("Taux de Conversion Max", f"{df_mkt['Taux_Conversion'].max()}%", "In-Store")
kpi4.metric("CPA Moyen", f"{df_mkt['CPA'].mean():.2f} €")

st.markdown("---")

# ONGLETS DE NAVIGATION
tab1, tab2, tab3 = st.tabs(["👥 Segmentation Client", "📣 Performance Marketing", "🤖 Modèles IA & Budget"])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        st.write("### Contribution au Chiffre d'Affaires par Segment")
        fig_ca = px.bar(
            filtered_seg, 
            x='Segment', 
            y='CA_Total', 
            color='Segment',
            labels={'CA_Total': "Chiffre d'Affaires Cumulé (€)"},
            text_auto=True
        )
        st.plotly_chart(fig_ca, use_container_width=True)
        
    with col2:
        st.write("### Profil Moyen des Segments")
        st.dataframe(filtered_seg[['Segment', 'Age_Moyen', 'Depense_Moyenne', 'CA_Total']], use_container_width=True)

with tab2:
    col1, col2 = st.columns(2)
    with col1:
        st.write("### Taux de Conversion par Canal Marketing (%)")
        fig_conv = px.bar(
            df_mkt, 
            x='Channel', 
            y='Taux_Conversion', 
            color='Channel',
            labels={'Taux_Conversion': 'Taux de Conversion (%)'}
        )
        st.plotly_chart(fig_conv, use_container_width=True)
        
    with col2:
        st.write("### Coût d'Acquisition Client (CPA) par Canal")
        fig_cpa = px.bar(
            df_mkt, 
            x='Channel', 
            y='CPA', 
            color='Channel',
            labels={'CPA': 'CPA (€)'}
        )
        st.plotly_chart(fig_cpa, use_container_width=True)

with tab3:
    col1, col2 = st.columns(2)
    with col1:
        st.write("### Précision des Modèles Prédictifs de Churn")
        fig_acc = px.bar(
            df_models, 
            x='Modele', 
            y='Accuracy', 
            color='Modele',
            range_y=[0, 110],
            text_auto=True
        )
        st.plotly_chart(fig_acc, use_container_width=True)
        
    with col2:
        st.write("### Répartition Stratégique du Budget Marketing")
        fig_pie = px.pie(
            df_seg, 
            values='Budget_Allocations', 
            names='Segment',
            hole=0.4
        )
        st.plotly_chart(fig_pie, use_container_width=True)

   
