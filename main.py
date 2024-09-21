import streamlit as st
import plotly.express as px

st.title("Weather Forecast For Next Days")

place = st.text_input(label="Place: ")

days = st.slider(label="Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")

data = st.selectbox(label="Select data to visualize",
                    options=("Temperature", "Sky"))

st.subheader(f"{data} for the next {days} days in {place}")

def get_data(days):
    dates = ['2024-09-22', '2024-09-23', '2024-09-24']
    temp = [25, 28, 26]
    temp = [days * i for i in temp]
    return dates, temp

dates, temp = get_data(days)

figure = px.line(x=dates, y=temp, labels={"x": "Dates", "y": "Temperature (C)"})
st.plotly_chart(figure_or_data=figure)



