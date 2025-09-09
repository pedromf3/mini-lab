import requests

def get_weather_data(local):
    with open('api_key.txt', 'r') as file:
        key = file.read().strip()

    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{local}?unitGroup=metric&key={key}"

    response = requests.get(url)
    response.raise_for_status() 
    data = response.json()

    days = []
    for i in range(7):
        days.append({
            "date": data["days"][i]["datetime"],
            "maxtemp": data["days"][i]["tempmax"],
            "mintemp": data["days"][i]["tempmin"],
            "rain": data["days"][i]["precipprob"]
        })

    return {"location": local, "days": days}
