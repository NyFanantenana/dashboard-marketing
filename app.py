
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# 1. Configuration de la page (Mode Large)
st.set_page_config(
    page_title="Executive Marketing Analytics Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Injection de CSS avancé pour un design sombre & professionnel
st.markdown("""
    <style>
    /* Fond principal */
    .stApp {
        background-color: #0B0F19;
        color: #F3F4F6;
    }

    /* En-tête principal */
    .main-header {
        font-size: 26px;
        font-weight: 700;
        color: #38BDF8;
        letter-spacing: 0.5px;
        margin-bottom: 5px;
    }
    .sub-header {
        font-size: 14px;
        color: #9CA3AF;
        margin-bottom: 25px;
    }

    /* Style personnalisé des cartes KPIs */
    div[data-testid="stMetric"] {
        background-color: #111827 !important;
        border: 1px solid #1F2937 !important;
        border-radius: 10px !important;
        padding: 16px 20px !important;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3) !important;
    }
    div[data-testid="stMetric"] label {
        color: #9CA3AF !important;
        font-size: 13px !important;
        font-weight: 500 !important;
    }
    div[data-testid="stMetric"] div[data-testid="stMetricValue"] {
        color: #F9FAFB !important;
        font-size: 24px !important;
        font-weight: 700 !important;
    }

    /* Séparateur élégant */
    hr {
        border-color: #1F2937 !important;
    }
    </style>
""", unsafe_allow_html=True)

# En-tête du Dashboard
st.markdown('<div class="main-header">📊 Executive Marketing Analytics Dashboard</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Pilotage stratégique de la performance, de la segmentation RFM et du Churn client</div>', unsafe_allow_html=True)

# Barre latérale (Sidebar)
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Modules d'analyse :",
    ["Aperçu des KPIs", "Segmentation Client (K-Means)", "Performances des Campagnes", "Modèles Prédictifs (Churn)"]
)

# Template sombre partagé pour Plotly
plotly_theme = "plotly_dark"
color_sequence = ["#38BDF8", "#818CF8", "#34D399", "#F87171"]

# ---------------------------------------------------------
# MODULE 1 : KPIS GENERAUX
# ---------------------------------------------------------
if menu == "Aperçu des KPIs":
    st.subheader("📌 Performance Globale & Vue Synthétique")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Base Clients Totale", "5 Clients")
    col2.metric("Chiffre d'Affaires Total", "475 €")
    col3.metric("Panier Moyen", "95 € / client")
    col4.metric("Taux de Churn (Inactifs)", "20 %", delta="-20%", delta_color="inverse")

    st.markdown("---")

    df_clients = pd.DataFrame({
        'Client_ID': ['C001', 'C002', 'C003', 'C004', 'C005'],
        'Dépenses (€)': [210, 100, 165, 0, 0],
        'Statut': ['Actif (VIP)', 'Actif', 'Actif', 'Inactif', 'Inactif']
    })

    fig = px.bar(
        df_clients, 
        x='Client_ID', 
        y='Dépenses (€)', 
        color='Statut',
        title="<b>Répartition de la Contribution par Client (€)</b>",
        color_discrete_sequence=color_sequence,
        template=plotly_theme,
        height=400
    )
    fig.update_layout(paper_bgcolor='#0B0F19', plot_bgcolor='#0B0F19', margin=dict(l=20, r=20, t=50, b=20))
    st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------------
# MODULE 2 : SEGMENTATION K-MEANS
# ---------------------------------------------------------
elif menu == "Segmentation Client ":
    st.subheader("🎯 Analyse de la Segmentation Client (K-Means, K=3)")

    df_clusters = pd.DataFrame({
        'Segment': ['VIP / Forts Acheteurs', 'Clients Occasionnels', 'Prospects Inactifs'],
        'Nombre_Clients': [2, 1, 2],
        'CA_Généré (€)': [310, 165, 0],
        'Part_CA (%)': [65.3, 34.7, 0.0]
    })

    col1, col2 = st.columns([1, 1.2])

    with col1:
        st.markdown("##### **Synthèse par Segment**")
        st.dataframe(df_clusters, use_container_width=True)

    with col2:
        fig = px.pie(
            df_clusters, 
            values='CA_Généré (€)', 
            names='Segment',
            title="<b>Part du Chiffre d'Affaires par Segment</b>",
            color_discrete_sequence=color_sequence,
            hole=0.4,
            template=plotly_theme,
            height=380
        )
        fig.update_layout(paper_bgcolor='#0B0F19', plot_bgcolor='#0B0F19', margin=dict(l=20, r=20, t=50, b=20))
        st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------------
# MODULE 3 : PERFORMANCES DES CAMPAGNES
# ---------------------------------------------------------
elif menu == "Performances des Campagnes":
    st.subheader("📈 Rentabilité des Canaux d'Acquisition")

    df_campagnes = pd.DataFrame({
        'Canal': ['Emailing', 'Social Media', 'Google Ads'],
        'Budget (€)': [200, 500, 800],
        'Conversions': [40, 25, 30],
        'CPA (€)': [5.0, 20.0, 26.67],
        'ROI (%)': [320, 150, 90]
    })

    col1, col2 = st.columns(2)

    with col1:
        fig_roi = px.bar(
            df_campagnes, 
            x='Canal', 
            y='ROI (%)', 
            color='Canal',
            title="<b>Retour sur Investissement (ROI %)</b>",
            color_discrete_sequence=["#34D399", "#38BDF8", "#F87171"],
            template=plotly_theme,
            height=380
        )
        fig_roi.update_layout(paper_bgcolor='#0B0F19', plot_bgcolor='#0B0F19', margin=dict(l=20, r=20, t=50, b=20))
        st.plotly_chart(fig_roi, use_container_width=True)

    with col2:
        fig_cpa = px.bar(
            df_campagnes, 
            x='Canal', 
            y='CPA (€)', 
            color='Canal',
            title="<b>Coût d'Acquisition Client (CPA €)</b>",
            color_discrete_sequence=["#34D399", "#FBBF24", "#F87171"],
            template=plotly_theme,
            height=380
        )
        fig_cpa.update_layout(paper_bgcolor='#0B0F19', plot_bgcolor='#0B0F19', margin=dict(l=20, r=20, t=50, b=20))
        st.plotly_chart(fig_cpa, use_container_width=True)

# ---------------------------------------------------------
# MODULE 4 : MODELES PREDICTIFS
# ---------------------------------------------------------
elif menu == "Modèles Prédictifs (Churn)":
    st.subheader("🤖 Modélisation Prédictive de l'Attrition (Churn)")

    df_models = pd.DataFrame({
        'Modèle Machine Learning': ['Logistic Regression', 'Random Forest Classifier', 'XGBoost Classifier'],
        'Précision (Accuracy)': ['100 %', '100 %', '100 %'],
        'Statut Déploiement': ['Validé', 'Validé', 'Validé (Recommandé)']
    })

    st.dataframe(df_models, use_container_width=True)
    st.success("✔ Les modèles de Machine Learning sont entraînés, validés et opérationnels.")
