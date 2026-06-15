import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

st.set_page_config(page_title="DataOps Local", layout="wide")

st.title("Projet DataOps local")
st.write("Dashboard simple connecté à PostgreSQL.")

DATABASE_URL = "postgresql+psycopg2://dataops:dataops@localhost:5433/oltp"

try:
    engine = create_engine(DATABASE_URL)
    customers = pd.read_sql("SELECT * FROM customers", engine)
    orders = pd.read_sql("SELECT * FROM orders", engine)

    st.subheader("Customers")
    st.dataframe(customers)

    st.subheader("Orders")
    st.dataframe(orders)

    st.metric("Total commandes", len(orders))
    st.metric("Montant total", round(orders["amount"].sum(), 2))

except Exception as e:
    st.error("Impossible de se connecter à PostgreSQL ou les tables n'existent pas encore.")
    st.code(str(e))
    st.info("Lance d'abord : python seed_environment.py")
