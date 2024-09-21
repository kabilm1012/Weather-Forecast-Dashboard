import streamlit as st

st.title("Weather Forecast For Next Days")

place = st.text_input(label="Place: ")

days = st.slider(label="Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")

data = st.selectbox(label="Select data to visualize",
                    options=("Temperature", "Sky"))

st.subheader(f"{data} for the next {days} days in {place}")

