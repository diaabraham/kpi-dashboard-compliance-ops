import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import numpy as np

# Set page config
st.set_page_config(layout="wide", page_title="KPI Dashboard")

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        padding: 0rem 1rem;
    }
    .metric-card {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 5px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# Header
st.markdown("""
    <h1 style='text-align: center; color: #2c3e50;'>Internal KPI Dashboard – Retail Strategy (Q4 2024)</h1>
    <h3 style='text-align: center; color: #7f8c8d;'>Built for CFO-level reporting | Multi-Region View</h3>
    """, unsafe_allow_html=True)

# Generate sample data
def generate_monthly_data():
    months = pd.date_range(start='2024-01-01', end='2024-12-31', freq='M')
    data = {
        'ON': [450 + i*10 + np.random.randint(-20, 20) for i in range(len(months))],
        'QC': [380 + i*8 + np.random.randint(-15, 15) for i in range(len(months))]
    }
    return pd.DataFrame(data, index=months)

# Create metrics data
metrics_data = {
    'Compliance Cost per FTE': ('$2,845', '↓ 8% vs prev quarter'),
    'Headcount Variance': ('+12 FTE', '↑ 3% above forecast'),
    'Audit Readiness Score': ('87/100', '↑ 15 points YTD'),
    'Labor Cost Allocation': ('68.5%', '↓ 2.3% vs target'),
    'Overtime Hours YTD': ('4,280', '↑ 12% vs prev year')
}

# Display metrics in columns
cols = st.columns(len(metrics_data))
for col, (metric, (value, delta)) in zip(cols, metrics_data.items()):
    with col:
        st.markdown(f"""
            <div class='metric-card'>
            <h4>{metric}</h4>
            <h2>{value}</h2>
            <p>{delta}</p>
            </div>
            """, unsafe_allow_html=True)

# Create two columns for the main content
col1, col2 = st.columns([0.4, 0.6])

# Regional Breakdown Table
with col1:
    st.markdown("### Regional Breakdown")
    regional_data = pd.DataFrame({
        'Region': ['Ontario', 'Quebec'],
        'Total FTE': [425, 318],
        'Compliance Cost': ['$1.21M', '$0.89M'],
        'Variance vs Budget': ['-3.2%', '+1.8%'],
        'Open Incidents': [14, 8]
    })
    st.dataframe(regional_data, hide_index=True)

# Charts
with col2:
    # Monthly Compliance Cost Trend
    monthly_data = generate_monthly_data()
    fig1 = px.line(monthly_data, title='Monthly Compliance Cost Trend (2024)')
    fig1.update_layout(height=300)
    st.plotly_chart(fig1, use_container_width=True)
    
    # Productivity Ratio by Branch
    productivity_data = pd.DataFrame({
        'Branch': ['Toronto', 'Ottawa', 'Montreal', 'Quebec City'],
        'Productivity Ratio': [0.92, 0.88, 0.85, 0.89]
    })
    fig2 = px.bar(productivity_data, x='Branch', y='Productivity Ratio',
                  title='Productivity Ratio by Branch')
    fig2.update_layout(height=300)
    st.plotly_chart(fig2, use_container_width=True)

# Insights Section
st.markdown("### Key Insights")
st.markdown("""
* Compliance cost per FTE reduced 12% in Ontario due to successful automation rollout in Toronto and Ottawa branches
* Quebec region audit readiness score improved significantly from 65 to 84 following the Q3 policy update implementation
* Overtime hours trending 12% above previous year, primarily driven by seasonal demand in Montreal branch
""")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: #7f8c8d;'>Last updated: December 15, 2024 | Data refresh: Daily at 0600 EST</p>", unsafe_allow_html=True)
