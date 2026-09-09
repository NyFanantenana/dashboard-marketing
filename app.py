import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Configuration globale
st.set_page_config(
    page_title="Executive Marketing Dashboard",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Thème Plotly sombre par défaut
px.defaults.template = "plotly_dark"
px.defaults.color_continuous_scale = px.colors.sequential.Purples

# Palette de couleurs Neon / Premium
NEON_PURPLE = "#8B5CF6"
NEON_BLUE = "#3B82F6"
NEON_GREEN = "#10B981"
NEON_ORANGE = "#F59E0B"
BG_CARD = "#1E293B"

# 2. Styles CSS Personnalisés
st.markdown("""
<style>
    /* Fond global */
    .stApp {
        background-color: #0F172A;
        color: #F8FAFC;
    }
    
    /* Cartes KPI Glassmorphism */
    .kpi-card {
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.7), rgba(15, 23, 42, 0.8));
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 20px;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3);
        backdrop-filter: blur(12px);
        transition: transform 0.2s ease, border-color 0.2s ease;
    }
    .kpi-card:hover {
        border-color: rgba(139, 92, 246, 0.4);
        transform: translateY(-2px);
    }
    .kpi-title {
        font-size: 0.8rem;
        font-weight: 600;
        color: #94A3B8;
        text-transform: uppercase;
        letter-spacing: 0.08em;
    }
    .kpi-value {
        font-size: 2rem;
        font-weight: 800;
        background: linear-gradient(90deg, #A78BFA, #60A5FA);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 8px 0 4px 0;
    }
    .kpi-sub {
        font-size: 0.85rem;
        color: #10B981;
        font-weight: 500;
    }

    /* Onglets Modernes */
    .stTabs [data-baseweb="tab-list"] {
        gap: 12px;
        background-color: transparent;
    }
    .stTabs [data-baseweb="tab"] {
        border-radius: 10px;
        padding: 10px 24px;
        background-color: #1E293B;
        color: #94A3B8;
        border: 1px solid rgba(255, 255, 255, 0.05);
        font-weight: 600;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(90deg, #6366F1, #8B5CF6) !important;
        color: #FFFFFF !important;
        border: none !important;
        box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3);
    }
    
    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        background-color: #1E293B;
        border-right: 1px solid rgba(255, 255, 255, 0.05);
    }
</style>
""", unsafe_allow_html=True)

# 3. Chargement des données
@st.cache_data
def load_data():
    df_seg = pd.DataFrame({
        'Segment': ['VIP / Forts Acheteurs', 'Clients Occasionnels', 'Prospects Inactifs'],
        'Nombre_Clients': [1, 2, 2],
        'Age_Moyen': [25.0, 32.5, 27.0],
        'Depense_Moyenne': [155.0, 82.5, 0.0],
        'CA_Total': [310.0, 165.0, 0.0],
        'Budget_Allocations': [40, 35, 25]
    })
    
    df_mkt = pd.DataFrame({
        'Channel': ['In-Store', 'Social', 'TV', 'Online', 'Email'],
        'Budget': [1540.0, 2000.0, 3000.0, 1000.0, 500.0],
        'Taux_Conversion': [20.0, 13.33, 8.33, 7.5, 5.0],
        'CPA': [15.0, 10.0, 12.0, 6.67, 10.0]
    })
    
    df_models = pd.DataFrame({
        'Modele': ['Logistic Regression', 'Random Forest', 'XGBoost'],
        'Accuracy': [100.0, 100.0, 80.0]
    })
    
    return df_seg, df_mkt, df_models

df_seg, df_mkt, df_models = load_data()

# 4. En-tête Principal
st.markdown("<h1 style='font-size: 2.4rem; font-weight: 800; margin-bottom: 0px;'>📊 Marketing & Customer Analytics</h1>", unsafe_allow_html=True)
st.markdown("<p style='color: #64748B; font-size: 1rem; margin-bottom: 25px;'>Vue d'ensemble stratégique et segmentation avancée des clients</p>", unsafe_allow_html=True)

# 5. Sidebar
with st.sidebar:
    st.markdown("### 🎛️ Filtres")
    selected_segment = st.multiselect(
        "Segment Client :",
        options=df_seg['Segment'].unique(),
        default=df_seg['Segment'].unique()
    )
    st.markdown("---")
    st.caption("Projet Data Analytics • Module 8")

filtered_seg = df_seg[df_seg['Segment'].isin(selected_segment)]

# 6. Cartes KPI Personnalisées
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown("""
        <div class="kpi-card">
            <div class="kpi-title">Chiffre d'Affaires</div>
            <div class="kpi-value">475.00 €</div>
            <div class="kpi-sub">▲ +12% ce mois</div>
        </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
        <div class="kpi-card">
            <div class="kpi-title">Panier Moyen</div>
            <div class="kpi-value">95.00 €</div>
            <div class="kpi-sub">🎯 Objectif atteint</div>
        </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
        <div class="kpi-card">
            <div class="kpi-title">Top Canal Conversion</div>
            <div class="kpi-value">20.0 %</div>
            <div class="kpi-sub" style="color: #60A5FA;">🏬 In-Store</div>
        </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
        <div class="kpi-card">
            <div class="kpi-title">CPA Moyen</div>
            <div class="kpi-value">10.73 €</div>
            <div class="kpi-sub" style="color: #F59E0B;">⚡ Optimisé</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 7. Navigation par Onglets
tab1, tab2, tab3 = st.tabs(["👥 Segmentation Client", "🚀 Performance Canaux", "🤖 IA & Allocations"])

with tab1:
    col1, col2 = st.columns([3, 2])
    with col1:
        fig_ca = px.bar(
            filtered_seg,
            x='Segment',
            y='CA_Total',
            color='Segment',
            color_discrete_sequence=['#8B5CF6', '#3B82F6', '#64748B'],
            title="<b>Chiffre d'Affaires par Segment (€)</b>",
            text_auto='.2f'
        )
        fig_ca.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            showlegend=False,
            font=dict(color="#94A3B8")
        )
        st.plotly_chart(fig_ca, use_container_width=True)
        
    with col2:
        st.markdown("<h4 style='color: #F8FAFC;'>Détails des Segments</h4>", unsafe_allow_html=True)
        st.dataframe(
            filtered_seg[['Segment', 'Age_Moyen', 'Depense_Moyenne', 'CA_Total']],
            use_container_width=True,
            hide_index=True
        )

with tab2:
    col1, col2 = st.columns(2)
    with col1:
        fig_conv = px.bar(
            df_mkt,
            x='Channel',
            y='Taux_Conversion',
            color='Taux_Conversion',
            color_continuous_scale='Purples',
            title="<b>Taux de Conversion par Canal (%)</b>",
            text_auto='.1f'
        )
        fig_conv.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color="#94A3B8"))
        st.plotly_chart(fig_conv, use_container_width=True)
        
    with col2:
        fig_cpa = px.line(
            df_mkt,
            x='Channel',
            y='CPA',
            markers=True,
            title="<b>Coût d'Acquisition Client (CPA €)</b>"
        )
        fig_cpa.update_traces(line_color='#10B981', line_width=3, marker_size=8)
        fig_cpa.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color="#94A3B8"))
        st.plotly_chart(fig_cpa, use_container_width=True)

with tab3:
    col1, col2 = st.columns(2)
    with col1:
        fig_acc = px.bar(
            df_models,
            x='Modele',
            y='Accuracy',
            color='Accuracy',
            color_continuous_scale='Blues',
            title="<b>Précision des Modèles (Churn Prediction)</b>",
            text_auto=True
        )
        fig_acc.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color="#94A3B8"), yaxis_range=[0, 115])
        st.plotly_chart(fig_acc, use_container_width=True)
        
    with col2:
        fig_pie = px.pie(
            df_seg,
            values='Budget_Allocations',
            names='Segment',
            hole=0.6,
            color_discrete_sequence=['#8B5CF6', '#3B82F6', '#64748B'],
            title="<b>Recommandation d'Allocation Budgétaire (%)</b>"
        )
        fig_pie.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color="#94A3B8"))
        st.plotly_chart(fig_pie, use_container_width=True)
   
