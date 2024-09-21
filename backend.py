import requests

API_KEY = "6d69d2a4b73e882047548fb77daf07da"


def get_data(place, forecast_days=None, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data  = data['list']
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    if kind == "Temperature":
        temperature = [dict['main']['temp'] for dict in filtered_data]
        dates = [dict['dt_txt'] for dict in filtered_data]
        return temperature, dates
    elif kind == "Sky":
        sky_conditions = [dict['weather'][0]['main'] for dict in filtered_data]
        return sky_conditions


if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3, kind="Sky"))
    