import streamlit as st
import pandas as pd

st.title("Investment KPI Dashboard")
st.markdown("Visualize extracted KPIs from investment documents.")

uploaded_file = st.file_uploader("Upload Excel file", type=["xlsx"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.dataframe(df)

    st.bar_chart(df.set_index("Metric"))
