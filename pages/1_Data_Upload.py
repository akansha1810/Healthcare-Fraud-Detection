import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Upload Data", layout="wide")

st.title("📂 Upload Unseen Healthcare Data")

st.write("Upload the three unseen CSV files.")

st.divider()

beneficiary_file = st.file_uploader(
    "Upload Beneficiary Data",
    type="csv"
)

inpatient_file = st.file_uploader(
    "Upload Inpatient Data",
    type="csv"
)

outpatient_file = st.file_uploader(
    "Upload Outpatient Data",
    type="csv"
)

if beneficiary_file is not None:
    beneficiary = pd.read_csv(beneficiary_file)
    st.success("Beneficiary Data Uploaded Successfully")
    st.dataframe(beneficiary.head())

if inpatient_file is not None:
    inpatient = pd.read_csv(inpatient_file)
    st.success("Inpatient Data Uploaded Successfully")
    st.dataframe(inpatient.head())

if outpatient_file is not None:
    outpatient = pd.read_csv(outpatient_file)
    st.success("Outpatient Data Uploaded Successfully")
    st.dataframe(outpatient.head())
