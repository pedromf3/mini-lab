# Author: Pedro Ferreira
# Last Updated: April 5, 2025
# Version 1.1

import requests

with open('api_key.txt', 'r') as file:
    key = file.read().strip()
    
url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Aveiro?unitGroup=metric&key={key}"

def main():
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return
    except ValueError:
        print("Error parsing JSON response.")
        return

    print(f"{'Day':<12}{'Max Temp (°C)':<15}{'Min Temp (°C)':<15}")
    print("-" * 42)

    for i in range(7):
        day = data["days"][i]["datetime"]
        maxtemp = data["days"][i]["tempmax"]
        mintemp = data["days"][i]["tempmin"]
        print(f"{day:<12}{maxtemp:<15}{mintemp:<15}")

if __name__ == '__main__':
    main()

