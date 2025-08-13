import streamlit as st
import pandas as pd

st.title("🚀 Codespace Devcontainer Test")

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Score": [85, 92, 78]
}
df = pd.DataFrame(data)

st.subheader("Sample DataFrame")
st.dataframe(df)

st.success("Streamlit is running inside your Codespace!")
