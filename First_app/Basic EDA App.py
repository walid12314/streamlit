import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Title
st.title("Simple Data Analysis Web App")

# File upload
uploaded_file = st.file_uploader("Mall_Customers", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)

    # Display some stats
    st.header("Basic Statistics")
    st.write(df.describe())

 
    # Filter numeric columns for scatter plot
    numeric_values =  df.select_dtypes(include=[np.number])
    numeric_columns = df.select_dtypes(include=[np.number]).columns

    fig, ax = plt.subplots()
    sns.heatmap(numeric_values.corr(), annot=True, ax=ax)
    st.pyplot(fig)

    if len(numeric_columns) > 1:
        # Select columns for scatter plot
        st.header("Scatter Plot")
        x_axis = st.selectbox("Select X-axis", numeric_columns)
        y_axis = st.selectbox("Select Y-axis", numeric_columns)

        fig, ax = plt.subplots()
        ax.scatter(df[x_axis], df[y_axis])
        ax.set_xlabel(x_axis)
        ax.set_ylabel(y_axis)
        st.pyplot(fig)
    else:
        st.write("Not enough numeric columns for scatter plot.")


