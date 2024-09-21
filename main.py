import streamlit as st
import plotly.express as px
from backend import get_data

# Add title, textinput, slider, selectbox, subheader
st.title("Weather Forecast For Next Days")
place = st.text_input(label="Place: ")
days = st.slider(label="Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
data = st.selectbox(label="Select data to visualize",
                    options=("Temperature", "Sky"))
st.subheader(f"{data} for the next {days} days in {place.title()}")

if place:
    # Get temperature/sky data
    filtered_data = get_data(place, days)

    if data == "Temperature":
        temperature = [dict['main']['temp']/10 for dict in filtered_data]
        dates = [dict['dt_txt'] for dict in filtered_data]
        # Plot the temperature data
        figure = px.line(x=dates, y=temperature, 
                        labels={"x": "Dates", "y": "Temperature (C)"})
        st.plotly_chart(figure_or_data=figure)
    elif data == "Sky": 
        sky_conditions = [dict['weather'][0]['main'] for dict in filtered_data]
        images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                  "Rain": "images/rain.png", "Snow": "images/snow.png"}
        image_paths = [images[condition] for condition in sky_conditions]
        # Render the images
        st.image(image=image_paths, caption=sky_conditions, width=115)



