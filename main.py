import streamlit as st
import time
st.write("ehlo")
if st.button('baloons',type='primary'):
    st.toast("balloons")
    time.sleep(3)
    st.rerun()