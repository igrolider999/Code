from pyowm.owm import OWM
from tkinter import *

# Replace with your own API key
api_key = "4a5f9197c4d3b2351ac263c7b12c9d3f"
owm = OWM(api_key)

# Get weather manager
mgr = owm.weather_manager()

# Make a one-time call for current weather in a city (e.g., London)
forecast = mgr.forecast_at_place("Haarlem,NL", "3h")
weather_list = forecast.forecast.weathers  # List of Weather objects

# Loop through each forecast entry
# for weather in weather_list:
#     time = weather.reference_time('iso')  # ISO format datetime
#     status = weather.status                # Weather description
#     temp = weather.temperature('celsius')['temp']
#     wind_speed = weather.wind()['speed']

#     print(f"{time} | {status} | Temp: {temp}°C | Wind: {wind_speed} m/s")

num = 2
print(weather_list[num].temperature('celsius')['temp'], weather_list[num].reference_time('iso'))

w = [weather_list[num].temperature('celsius')['temp'], weather_list[num].reference_time('iso')[11:19]]

root = Tk()
root.geometry("720x480")
state = True
for x in range(0, len(weather_list)):
    w = [weather_list[x].temperature('celsius')['temp'], weather_list[x].reference_time('iso')[11:19]]
    for i in w:
        state = not state
        Label(root, text=i).grid(column=x, row=1 if state is True else 2)

root.mainloop()
