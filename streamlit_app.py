import streamlit as st
st.cache_data.clear()

col1, col2, col3 = st.columns([3,3,3])
with col1:
    st.header("Imagen")
with col3:
    st.header("SMETRIA")

st.markdown("<h3 style='text-align: center;'>Sistema de monitorización de eventos en tramos</h3>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Camino de Santiago - Camino Portugués</h3>", unsafe_allow_html=True)
st.divider()

# -------------------------------------------------------------------------------
