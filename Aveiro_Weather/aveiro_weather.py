# Aveiro Weather Forecast
# Author: Pedro Ferreira
# Last Updated: April 10, 2025
# Version 1.2

import requests
import matplotlib.pyplot as plt

with open('api_key.txt', 'r') as file:
    key = file.read().strip()
    
url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Aveiro?unitGroup=metric&key={key}"

def main():
    day = []
    maxtemp = []
    mintemp = []   
    rain = [] 

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTP Error for bad responses
        data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return
    except ValueError:
        print("Error parsing JSON response.")
        return

    for i in range(7):
        day.append(data["days"][i]["datetime"])
        maxtemp.append(data["days"][i]["tempmax"])
        mintemp.append(data["days"][i]["tempmin"])
        rain.append(data["days"][i]["precipprob"])

    fig, ax1 = plt.subplots()

    # Plot max and min temperatures on the left y-axis
    ax1.plot(day, maxtemp, label='Max Temp (°C)', color='red', marker='o')
    ax1.plot(day, mintemp, label='Min Temp (°C)', color='blue', marker='o')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Temperature (°C)')
    ax1.tick_params(axis='y')
    ax1.legend(loc='upper left')

    # Create a second y-axis for precipitation
    ax2 = ax1.twinx()
    ax2.bar(day, rain, label='Precipitation (%)', alpha=0.5)
    ax2.set_ylabel('Precipitation (%)')
    ax2.tick_params(axis='y')
    ax2.legend(loc='upper right')

    plt.title('Aveiro Weather')
    ax1.set_zorder(ax2.get_zorder() + 1) 
    ax1.patch.set_visible(False)

    plt.show()

if __name__ == '__main__':
    main()

