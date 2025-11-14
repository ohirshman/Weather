import plotly
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import streamlit as st
import pandas as pd

def simple_streamlit():
    st.title("My First Streamlit App")

    st.header("Interactive Widget")
    x = st.slider("Select a value", 0, 100, 25)
    st.write(f"You selected the value: {x}")

def penguins_plots():
    df = sns.load_dataset('penguins')

    plot_choice = st.radio('Choose you plot library:', ['Seaborn', 'Plotly'])

    if plot_choice == 'Seaborn':
        fig, ax = plt.subplots()
        sns.scatterplot(data=df, x='flipper_length_mm', y='body_mass_g', hue='species')
        st.pyplot(fig)

    elif plot_choice == 'Plotly':
        fig = px.scatter(df, x='flipper_length_mm', y='body_mass_g', color='species', title='Pegnguins')
        st.plotly_chart(fig)