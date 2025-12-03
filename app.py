import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from ucimlrepo import fetch_ucirepo 

# Load the dataset
@st.cache_data
def load_data():
    # url = "https://archive.ics.uci.edu/static/public/186/wine+quality.zip"
    # fetch dataset 
    data = fetch_ucirepo(id=186)    # data - wine data in pandas dataframe format
    df = data.data.original
    print(type(df))
    print(df.head())
    return df

# Data Transformation Logic
def transform_data(df):
    df['quality_label'] = df['quality'].apply(lambda x: 'low' if x <= 3 else ('medium' if x <= 6 else ('good' if x <= 8 else 'excellent')))
    df['acidity_ratio'] = df['fixed_acidity'] / df['volatile_acidity']
    df['density_to_alcohol_ratio'] = df['density'] / df['alcohol']
    return df

data = load_data()
data = transform_data(data)

# Title of the application
st.title("Wine Quality Analysis")

# Display the dataset
st.write("## Raw Data")
st.write(data.head())

# Visualization 1: Alcohol Content Distribution
st.write("## Alcohol Content Distribution")
fig, ax = plt.subplots()
data['alcohol'].hist(bins=20, ax=ax)
ax.set_title("Alcohol Content Distribution")
ax.set_xlabel("Alcohol")
ax.set_ylabel("Frequency")
st.pyplot(fig)

# Visualization 2: Quality Label Distribution
st.write("## Quality Label Distribution")
quality_counts = data['quality_label'].value_counts()
st.bar_chart(quality_counts)

# Visualization 3: Acidity Ratio Distribution
st.write("## Acidity Ratio Distribution")
fig, ax = plt.subplots()
data['acidity_ratio'].hist(bins=20, ax=ax)
ax.set_title("Acidity Ratio Distribution")
ax.set_xlabel("Acidity Ratio")
ax.set_ylabel("Frequency")
st.pyplot(fig)

st.write("## Density to Alcohol Ratio vs. Quality")
fig, ax = plt.subplots()

# Define colors for each quality label
colors = {'low': 'red', 'medium': 'orange', 'good': 'green', 'excellent': 'blue'}

for label in data['quality_label'].unique():
    subset = data[data['quality_label'] == label]
    ax.scatter(subset['density_to_alcohol_ratio'], subset['quality'], 
               label=label, color=colors[label], alpha=0.7)

ax.set_xlabel('Density to Alcohol Ratio')
ax.set_ylabel('Quality')
ax.legend(title='Quality Label')
st.pyplot(fig)