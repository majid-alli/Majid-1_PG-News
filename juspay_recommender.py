import streamlit as st
import pandas as pd

st.set_page_config(page_title="PAPG News Dashboard", page_icon=":newspaper:", layout="wide")

st.title(":newspaper: PAPG World News Dashboard")
st.caption("Latest updates from Razorpay, PayU, Cashfree, Easebuzz, Pine Labs, BillDesk, TechProcess, Worldline, Pay10, CCAvenue, and Juspay")

st.warning("Google News RSS cannot be fetched directly in Streamlit Cloud due to network restrictions. Using manual links instead.")

COMPANIES = {
    "Razorpay": "https://news.google.com/search?q=Razorpay%20payment%20gateway",
    "PayU": "https://news.google.com/search?q=PayU%20payment%20gateway",
    "Cashfree": "https://news.google.com/search?q=Cashfree%20payment%20gateway",
    "Easebuzz": "https://news.google.com/search?q=Easebuzz%20payment%20gateway",
    "Pine Labs": "https://news.google.com/search?q=Pine%20Labs%20payment%20gateway",
    "BillDesk": "https://news.google.com/search?q=BillDesk%20payment%20gateway",
    "TechProcess": "https://news.google.com/search?q=TechProcess%20payment%20gateway",
    "Worldline": "https://news.google.com/search?q=Worldline%20payment%20gateway",
    "Pay10": "https://news.google.com/search?q=Pay10%20payment%20gateway",
    "CCAvenue": "https://news.google.com/search?q=CCAvenue%20payment%20gateway",
    "Juspay": "https://news.google.com/search?q=Juspay%20payment%20gateway",
}

selected_company = st.selectbox("Select Company", ["All"] + list(COMPANIES.keys()))

if selected_company == "All":
    for name, url in COMPANIES.items():
        st.markdown(f"### {name}")
        st.markdown(f"[Latest News]({url})")
else:
    st.markdown(f"### {selected_company}")
    st.markdown(f"[Latest News for {selected_company}]({COMPANIES[selected_company]})")
