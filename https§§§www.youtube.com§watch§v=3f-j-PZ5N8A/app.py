import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt

import plotly_express as px
class BL:
    nav = ['HOME','Stats','Header', 'Plot', 'InteractivePlot']
    def stats(st, df):
        st.header("Stats:")
        st.write(df.describe())

    def header(st, df):
        st.header("Header:")
        st.write(df.head())

    def plot(st, df):
        fig, ax = plt.subplots(1,1)
        ax.scatter(x=df['Depth'], y=df['Magnitude'])
        ax.set_xlabel('Depth')
        ax.set_ylabel('Magnitude')

        st.pyplot(fig)


    def interactive_plot(st, df):
        x_axis_val = st.selectbox('select x-axis:', options=df.columns)
        y_axis_val = st.selectbox('select y-axis:', options=df.columns)

        col = st.color_picker('select color')
        plot = px.scatter(df, x=x_axis_val, y=y_axis_val)
        plot.update_traces(marker=dict(color=col))
        st.plotly_chart(plot)

st.title("hello obar1!")
st.text("simple web app for hearthquake data")
st.markdown("done with `streamlit`")

st.sidebar.text("Navigation")
# upload data with file upload 
uploaded_data = st.sidebar.file_uploader("upload file here...")

pages_options = st.sidebar.radio('Pages', options=BL.nav)


if uploaded_data:

    df = pd.read_csv(uploaded_data)

    if pages_options=='Stats':
        BL.stats(st,df)
    if pages_options=='Header':
        BL.header(st,df)
    if pages_options=='Plot':
        BL.plot(st,df)
    if pages_options=='InteractivePlot':
        BL.interactive_plot(st,df)