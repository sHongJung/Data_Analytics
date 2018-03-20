# Dependencies
import requests
import json
import datetime
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

# Weather
api_key = "c7f9f57b4779391ea1f5ae067591c971"

# Endpoint URL for five day forecast Phoenix, AZ
target_url = "http://api.openweathermap.org/data/2.5/forecast" \
    "?q=Phoenix,us&units=IMPERIAL&mode=json&APPID=" + api_key

# Print URL
print(target_url)

# Request Data
city_weather = requests.get(target_url).json()

# List for holding temperatures
temps = []
times = []

# Display the weather with dates
for temp in city_weather["list"]:
    print("%s | %s F" % (temp["dt_txt"], temp["main"]["temp"]))
    temps.append(temp["main"]["temp"])

    weather_date = datetime.datetime.strptime(
        temp["dt_txt"], "%Y-%m-%d %H:%M:%S")
    times.append(weather_date)


# Plot the temperatures over time
plt.plot(times, temps)
formatter = DateFormatter('%Y-%m-%d %H:%M:%S')
plt.gcf().axes[0].xaxis.set_major_formatter(formatter)
plt.gcf().autofmt_xdate()
plt.show()
