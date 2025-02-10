import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Data Science for Everyone")
st.write("Welcome to my app!!")
st.sidebar.title("Select dataset")
st.image("h.jpg")
df = pd.read_csv("wine.csv")
app_mode = st.sidebar.selectbox("Seect a page >>", ["01 Introduction","02 Data Visualization "])
if app_mode == "01 Introduction":
    st.write("Let's start exploring the dataset:")
    st.dataframe(df.head(10))
    st.dataframe(df.describe())
    st.markdown("### Statistics Summary of the dataset >>")
else:
    st.write("Let's do some data visualization.")

    columns = df.columns
    user_selection = st.selectbox("Select a variable", columns)
    st.bar_chart(df[user_selection])

    st.line_chart(df["Alcohol"])


    selections = st.multiselect("Select a variable", columns, ["Alcohol", "Proline"])
    fig, ax = plt.subplots(figsize = (6,4))
    sns.barplot(x= selections[0], y = selections[1], data = df, palette = "Blues")
    st.pyplot(fig)

