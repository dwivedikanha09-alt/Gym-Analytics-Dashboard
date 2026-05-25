import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="Gym Member Analytics Dashboard",
    page_icon="🏋️",
    layout="wide",
)

# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------
df = pd.read_csv("gym_members_exercise_tracking.csv")

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------
st.markdown("""
<style>

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

[data-testid="stAppViewContainer"]{
    background: linear-gradient(135deg,#0f172a,#111827,#1e293b);
    color:white;
}

[data-testid="stSidebar"]{
    background:#0f172a;
    border-right:1px solid #334155;
}

.big-title{
    font-size:60px;
    font-weight:900;
    text-align:center;
    background: linear-gradient(to right,#38bdf8,#818cf8);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    margin-top:10px;
}

.subtitle{
    text-align:center;
    color:#cbd5e1;
    font-size:20px;
    margin-bottom:30px;
}

.card{
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(10px);
    border:1px solid rgba(255,255,255,0.1);
    padding:25px;
    border-radius:25px;
    box-shadow:0px 10px 30px rgba(0,0,0,0.4);
}

.metric-box{
    background: linear-gradient(135deg,#1e293b,#334155);
    padding:25px;
    border-radius:20px;
    text-align:center;
    border:1px solid #475569;
    transition:0.3s;
}

.metric-box:hover{
    transform: translateY(-5px);
}

.metric-value{
    font-size:40px;
    font-weight:800;
    color:#38bdf8;
}

.metric-label{
    font-size:18px;
    color:#cbd5e1;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------
st.markdown(
    "<div class='big-title'>🏋️ Gym Analytics Dashboard</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Modern Streamlit Dashboard for Gym Member Exercise Tracking</div>",
    unsafe_allow_html=True
)

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------
st.sidebar.title("⚙ Dashboard Controls")

numeric_cols = df.select_dtypes(include=np.number).columns.tolist()

selected_num = st.sidebar.selectbox(
    "📊 Select Numeric Feature",
    numeric_cols
)

# ---------------------------------------------------
# KPI SECTION
# ---------------------------------------------------
total_members = len(df)
total_columns = len(df.columns)
missing_values = df.isnull().sum().sum()
avg_value = round(df[selected_num].mean(), 2)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class='metric-box'>
        <div class='metric-value'>{total_members}</div>
        <div class='metric-label'>Total Members</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class='metric-box'>
        <div class='metric-value'>{total_columns}</div>
        <div class='metric-label'>Features</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class='metric-box'>
        <div class='metric-value'>{missing_values}</div>
        <div class='metric-label'>Missing Values</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class='metric-box'>
        <div class='metric-value'>{avg_value}</div>
        <div class='metric-label'>Average {selected_num}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ---------------------------------------------------
# CHART SECTION
# ---------------------------------------------------
col1, col2 = st.columns(2)

with col1:

    fig = px.histogram(
        df,
        x=selected_num,
        nbins=30,
        template="plotly_dark",
        title=f"{selected_num} Distribution",
    )

    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        title_font_size=22
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:

    fig2 = px.box(
        df,
        y=selected_num,
        template="plotly_dark",
        title=f"{selected_num} Box Plot",
    )

    fig2.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        title_font_size=22
    )

    st.plotly_chart(fig2, use_container_width=True)

# ---------------------------------------------------
# CORRELATION HEATMAP
# ---------------------------------------------------
st.subheader("🔥 Correlation Heatmap")

corr = df[numeric_cols].corr()

fig3 = px.imshow(
    corr,
    text_auto=True,
    color_continuous_scale='Blues',
    template='plotly_dark'
)

fig3.update_layout(
    height=700,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
)

st.plotly_chart(fig3, use_container_width=True)

# ---------------------------------------------------
# DATA PREVIEW
# ---------------------------------------------------
st.subheader("📄 Dataset Preview")

st.dataframe(df, use_container_width=True)

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------
st.markdown("---")

st.markdown("""
<center>
<h3 style='color:#94a3b8'>
Designed with ❤️ using Streamlit
</h3>
</center>
""", unsafe_allow_html=True)