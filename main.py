import streamlit as st

st.write("ehlo")
if st.button('baloons',type='primary'):
    st.toast("balloons")
    st.rerun()