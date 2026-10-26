import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Student Service Requests Analysis",
    page_icon="📊",
    layout="wide",
)

st.title("Student Service Requests Analysis")
st.write("Upload a CSV file to explore the dataset and generate a data dictionary.")

uploaded_file = st.file_uploader(
    "Upload student_service_requests.csv",
    type=["csv"],
)

if uploaded_file is None:
    st.info("Upload your student_service_requests.csv file to begin.")
    st.stop()

try:
    df = pd.read_csv(uploaded_file)
except Exception as error:
    st.error(f"Could not read the CSV file: {error}")
    st.stop()

if df.empty:
    st.warning("The uploaded dataset is empty.")
    st.stop()

st.success("Dataset loaded successfully.")

# Dataset overview
st.subheader("Dataset Overview")
col1, col2 = st.columns(2)
col1.metric("Total Rows", df.shape[0])
col2.metric("Total Columns", df.shape[1])

# First 10 rows
st.subheader("First 10 Rows")
st.dataframe(df.head(10), use_container_width=True)

# Data types
st.subheader("Data Types and Information")
data_types = df.dtypes.astype(str).to_frame("Data_Type")
st.dataframe(data_types, use_container_width=True)

# Category frequency distributions
st.subheader("Category Frequencies")
categorical_cols = df.select_dtypes(
    include=["object", "category", "string"]
).columns

if len(categorical_cols):
    for col in categorical_cols:
        with st.expander(f"Frequency for {col}"):
            frequency = (
                df[col]
                .value_counts(dropna=False)
                .rename_axis(col)
                .reset_index(name="Count")
            )
            st.dataframe(frequency, use_container_width=True)
else:
    st.info("No categorical columns were found in this dataset.")

# Compact data dictionary
st.subheader("Compact Data Dictionary")
data_dict = pd.DataFrame({
    "Field_Name": df.columns,
    "Data_Type": [str(df[col].dtype) for col in df.columns],
    "Non_Null_Count": [int(df[col].notna().sum()) for col in df.columns],
    "Missing_Count": [int(df[col].isna().sum()) for col in df.columns],
    "Unique_Values": [int(df[col].nunique()) for col in df.columns],
})
st.dataframe(data_dict, use_container_width=True)

# Download data dictionary
st.download_button(
    label="Download Data Dictionary (CSV)",
    data=data_dict.to_csv(index=False).encode("utf-8"),
    file_name="data_dictionary.csv",
    mime="text/csv",
)

# Missing values summary
st.subheader("Missing Values Summary")
missing_data = pd.DataFrame({
    "Field_Name": df.columns,
    "Missing_Count": [int(df[col].isna().sum()) for col in df.columns],
})
st.dataframe(missing_data, use_container_width=True)
