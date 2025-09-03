
import streamlit as st
import requests
import pandas as pd

API_URL = "http://localhost:8000"

st.set_page_config(page_title="Smart Grocery Inventory Dashboard", layout="wide")

st.title("🛒 Grocery Store Inventory")

st.subheader("Check Inventory by Product")

# Predefined grocery items (same as seed_data.py)
grocery_items = ["Bananas", "Milk", "Bread", "Eggs", "Apples"]

store_id = 1  # we only have one store in this demo
selected_item = st.selectbox("Choose a product:", grocery_items)

if st.button("Check Inventory"):
    resp = requests.get(f"{API_URL}/inventory/{store_id}/{selected_item}")
    if resp.status_code == 200:
        data = resp.json()
        if "error" in data:
            st.error(data["error"])
        else:
            df = pd.DataFrame([data])
            st.table(df)
    else:
        st.error("Error fetching inventory")
