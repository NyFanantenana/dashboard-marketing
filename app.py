import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# ==========================================
# 1. PAGE CONFIGURATION & CUSTOM ENTERPRISE CSS
# ==========================================
st.set_page_config(
    page_title="Executive Analytics Dashboard | Marketing & Data Science",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Injection de CSS pour un rendu UI/UX haut de gamme
st.markdown("""
    <style>
    /* Style général du fond et de la typographie */
    .main {
        background-color: #F8FAFC;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* Titres professionnels */
    h1 {
        color: #0F172A;
        font-weight: 800;
        letter-spacing: -0.5px;
    }
    h2, h3 {
        color: #1E293B;
        font-weight: 600;
    }
    
    /* Cartes de métriques personnalisées (KPI Cards) */
    .kpi-card {
        background-color: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .kpi-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
    }
    .kpi-title {
        color: #64748B;
        font-size: 0.85rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    .kpi-value {
        color: #0F172A;
        font-size: 1.8rem;
        font-weight: 700;
        margin-top: 4px;
    }
    .kpi-badge {
        display: inline-block;
        padding: 4px 8px;
        border-radius: 6px;
        font-size: 0.75rem;
        font-weight: 600;
        margin-top: 8px;
    }
    .badge-green { background-color: #DCFCE7; color: #166534; }
    .badge-blue { background-color: #DBEAFE; color: #1E40AF; }
    
    /* Modernisation des onglets */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        border-bottom: 2px solid #E2E8F0;
    }
    .stTabs [data-baseweb="tab"] {
        padding: 12px 20px;
        font-weight: 600;
        border-radius: 8px 8px 0 0;
        color: #64748B;
    }
    .stTabs [aria-selected="true"] {
        background-color: #1E293B !important;
        color: #FFFFFF !important;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. CHARGEMENT & STRUCTURATION DES DONNÉES
# ==========================================
@st.cache_data
def load_data():
    sales_cat = pd.DataFrame({
        'Catégorie': ['Clothing', 'Outerwear', 'Accessories', 'Footwear'],
        'Chiffre_Affaires': [175.0, 120.0, 90.0, 90.0]
    })
    
    clusters = pd.DataFrame({
        'Cluster_ID': [0, 1, 2],
        'Segment': ['VIP / Forts Acheteurs', 'Clients Occasionnels', 'Prospects Inactifs'],
        'Nombre_Clients': [2, 2, 1],
        'Age_Moyen': [25.0, 32.5, 27.0],
        'Achats_Moyens': [1.5, 1.0, 0.0],
        'Depense_Moyenne': [155.00, 82.50, 0.00],
        'CA_Total': [310.00, 165.00, 0.00]
    })
    
    marketing = pd.DataFrame({
        'Canal': ['Online', 'In-Store', 'Social', 'Email', 'TV'],
        'Budget': [1000.0, 1500.0, 2000.0, 500.0, 3000.0],
        'CTR': [4.00, 2.67, 3.75, 5.00, 5.00],
        'Taux_Conversion': [7.50, 20.00, 13.33, 5.00, 8.33],
        'CPA': [6.67, 15.00, 10.00, 10.00, 12.00]
    })
    
    ml_perf = pd.DataFrame({
        'Modèle': ['Logistic Regression', 'Random Forest', 'XGBoost'],
        'Accuracy': [100.0, 100.0, 80.0],
        'Precision': [1.00, 1.00, 0.64],
        'Recall': [1.00, 1.00, 0.80],
        'F1_Score': [1.00, 1.00, 0.71]
    })
    
    return sales_cat, clusters, marketing, ml_perf

df_sales_cat, df_clusters, df_marketing, df_ml = load_data()

# ==========================================
# 3. SIDEBAR DE CONTROL & FILTRES
# ==========================================
with st.sidebar:
    st.image("https://img.icons8.com/color/96/dashboard--v1.png", width=60)
    st.title("Filtres Exécutifs")
    st.markdown("---")
    
    segment_filter = st.multiselect(
        "Segments Clients :",
        options=df_clusters['Segment'].unique(),
        default=df_clusters['Segment'].unique()
    )
    
    canal_filter = st.multiselect(
        "Canaux Marketing :",
        options=df_marketing['Canal'].unique(),
        default=df_marketing['Canal'].unique()
    )
    
    st.markdown("---")
    st.caption("Projet Pédagogique SMD, IA & PRSD")
    st.caption("Auteur : DATA GOVERNANCE TEAM")

# Application des filtres
filtered_clusters = df_clusters[df_clusters['Segment'].isin(segment_filter)]
filtered_marketing = df_marketing[df_marketing['Canal'].isin(canal_filter)]

# ==========================================
# 4. EN-TÊTE DU DASHBOARD
# ==========================================
st.title("📈 Executive Marketing & Analytics Dashboard")
st.markdown("Analyse croisée de la performance commerciale, de la segmentation K-Means et de l'efficacité media.")
st.markdown("<br>", unsafe_allow_html=True)

# Rangée des KPIs principaux
kpi1, kpi2, kpi3, kpi4 = st.columns(4)

with kpi1:
    st.markdown("""
        <div class="kpi-card">
            <div class="kpi-title">Chiffre d'Affaires Total</div>
            <div class="kpi-value">475.00 €</div>
            <span class="kpi-badge badge-green">↑ Objectif Atteint</span>
        </div>
    """, unsafe_allow_html=True)

with kpi2:
    st.markdown("""
        <div class="kpi-card">
            <div class="kpi-title">Panier Moyen Global</div>
            <div class="kpi-value">95.00 €</div>
            <span class="kpi-badge badge-green">↑ +26.7% vs target</span>
        </div>
    """, unsafe_allow_html=True)

with kpi3:
    st.markdown("""
        <div class="kpi-card">
            <div class="kpi-title">Top Canal Conversion</div>
            <div class="kpi-value">In-Store (20%)</div>
            <span class="kpi-badge badge-blue">Performance Max</span>
        </div>
    """, unsafe_allow_html=True)

with kpi4:
    st.markdown("""
        <div class="kpi-card">
            <div class="kpi-title">CPA Minimal (Efficience)</div>
            <div class="kpi-value">6.67 € (Online)</div>
            <span class="kpi-badge badge-green">Coût Optimisé</span>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ==========================================
# 5. ONGLETS STRATÉGIQUES MULTI-DIMENSIONNELS
# ==========================================
tab_exec, tab_seg, tab_mkt, tab_ai = st.tabs([
    "📊 Synthèse Ventes", 
    "👥 Segmentation K-Means", 
    "📢 Efficacité Marketing", 
    "🤖 Modèles IA & Stratégie"
])

# ------------------------------------------
# TAB 1 : SYNTHÈSE VENTES
# ------------------------------------------
with tab_exec:
    st.subheader("Distribution des Ventes par Catégorie de Produits")
    
    col_chart, col_details = st.columns([2, 1])
    
    with col_chart:
        fig_sales = px.bar(
            df_sales_cat, 
            x='Catégorie', 
            y='Chiffre_Affaires',
            text='Chiffre_Affaires',
            color='Catégorie',
            color_discrete_sequence=['#0F172A', '#2563EB', '#059669', '#D97706'],
            title="Chiffre d'Affaires par Catégorie (€)"
        )
        fig_sales.update_traces(texttemplate='%{text:.2f} €', textposition='outside')
        fig_sales.update_layout(showlegend=False, yaxis_range=[0, 210], plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_sales, use_container_width=True)
        
    with col_details:
        st.markdown("### Insights Commercial")
        st.info("""
        * **Top Ventes** : La catégorie **Clothing** génère **175.00 €** (36.8% du CA Total).
        * **Panier Elevé** : La catégorie **Outerwear** présente un potentiel élevé avec **120.00 €**.
        * **Accessoires & Chaussures** : Contribution stable à **90.00 €** chacune.
        """)
        
        # Export des données
        csv_sales = df_sales_cat.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Exporter le rapport Ventes (CSV)", csv_sales, "ventes_categorie.csv", "text/csv")

# ------------------------------------------
# TAB 2 : SEGMENTATION K-MEANS
# ------------------------------------------
with tab_seg:
    st.subheader("Profilage & Structure des Clusters Clients (K-Means)")
    
    col_pie, col_bar_cluster = st.columns(2)
    
    with col_pie:
        fig_pie = px.pie(
            filtered_clusters,
            names='Segment',
            values='CA_Total',
            hole=0.45,
            color='Segment',
            color_discrete_map={
                'VIP / Forts Acheteurs': '#059669',
                'Clients Occasionnels': '#2563EB',
                'Prospects Inactifs': '#DC2626'
            },
            title="Répartition du CA par Segment Client"
        )
        st.plotly_chart(fig_pie, use_container_width=True)
        
    with col_bar_cluster:
        fig_dep = px.bar(
            filtered_clusters,
            x='Segment',
            y='Depense_Moyenne',
            color='Segment',
            text='Depense_Moyenne',
            color_discrete_map={
                'VIP / Forts Acheteurs': '#059669',
                'Clients Occasionnels': '#2563EB',
                'Prospects Inactifs': '#DC2626'
            },
            title="Dépense Moyenne par Segment (€)"
        )
        fig_dep.update_traces(texttemplate='%{text:.2f} €', textposition='outside')
        fig_dep.update_layout(showlegend=False, plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_dep, use_container_width=True)

    st.markdown("### Tableau de Synthèse des Segments")
    st.dataframe(filtered_clusters, use_container_width=True)

# ------------------------------------------
# TAB 3 : EFFICACITÉ MARKETING
# ------------------------------------------
with tab_mkt:
    st.subheader("Performance des Canaux de Communication & Acquisition")
    
    mkt_col1, mkt_col2 = st.columns(2)
    
    with mkt_col1:
        fig_conv = px.bar(
            filtered_marketing,
            x='Canal',
            y='Taux_Conversion',
            color='Canal',
            text='Taux_Conversion',
            title="Taux de Conversion par Canal (%)",
            color_discrete_sequence=px.colors.qualitative.Bold
        )
        fig_conv.update_traces(texttemplate='%{text:.2f} %', textposition='outside')
        fig_conv.update_layout(showlegend=False, plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_conv, use_container_width=True)
        
    with mkt_col2:
        fig_cpa = px.bar(
            filtered_marketing,
            x='Canal',
            y='CPA',
            color='Canal',
            text='CPA',
            title="Coût d'Acquisition Client - CPA (€)",
            color_discrete_sequence=px.colors.qualitative.Safe
        )
        fig_cpa.update_traces(texttemplate='%{text:.2f} €', textposition='outside')
        fig_cpa.update_layout(showlegend=False, plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_cpa, use_container_width=True)

# ------------------------------------------
# TAB 4 : MODELISATION IA & BUDGET (M6/M7)
# ------------------------------------------
with tab_ai:
    st.subheader("Évaluation des Modèles IA & Recommandation d'Allocation")
    
    ai_col1, ai_col2 = st.columns(2)
    
    with ai_col1:
        st.markdown("#### Comparaison de l'Accuracy (Prédiction Churn)")
        fig_ml = px.bar(
            df_ml,
            x='Modèle',
            y='Accuracy',
            color='Modèle',
            text='Accuracy',
            color_discrete_sequence=['#059669', '#2563EB', '#D97706']
        )
        fig_ml.update_traces(texttemplate='%{text:.1f} %', textposition='outside')
        fig_ml.update_layout(showlegend=False, yaxis_range=[0, 115], plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_ml, use_container_width=True)
        
    with ai_col2:
        st.markdown("#### Plan Mix-Budget Marketing Stratégique (M7)")
        budget_data = pd.DataFrame({
            'Segment Target': ['VIP / Forts Acheteurs', 'Clients Occasionnels', 'Prospects Inactifs'],
            'Part_Budget': [40, 35, 25]
        })
        fig_budget = px.pie(
            budget_data,
            names='Segment Target',
            values='Part_Budget',
            color='Segment Target',
            color_discrete_map={
                'VIP / Forts Acheteurs': '#059669',
                'Clients Occasionnels': '#2563EB',
                'Prospects Inactifs': '#D97706'
            },
            hole=0.4
        )
        st.plotly_chart(fig_budget, use_container_width=True)

    st.success("✅ **Recommandation Stratégique Générale** : Allouer **40% du budget media** sur le segment VIP pour maximiser la valeur vie client (CLV), tout en automatisant le scoring de Churn via le modèle **Logistic Regression**.")






   
