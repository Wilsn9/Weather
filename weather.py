import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")


# Endpoint for current weather data
base_url = "https://api.weatherapi.com/v1/current.json"



def get_city(city):
    params = {
        "key": API_KEY,
        "q": city
    }
    try:
        # Send GET request to WeatherAPI
        response = requests.get(base_url, params=params)
        
        # Raise error if request failed
        response.raise_for_status()
        # Convert response to dictionary
        
        return response.json()
    
    except requests.exceptions.HTTPError:
        print("Error: Could not retrieve weather data.")

    except requests.exceptions.ConnectionError:
        print("Error: No internet connection.")

    except requests.exceptions.Timeout:
        print("Error: The request took too long.")

    except requests.exceptions.RequestException:
        print("Error: Something went wrong.")
        

def get_weather(weather_data):
    try:
        
        # Send GET request to WeatherAPI
        city = weather_data["location"]["name"]
        
        # Raise error if request failed
        country = weather_data["location"]["country"]
        
        # Convert response to dictionary
        temp = weather_data["current"]["temp_c"]        
        
        if temp >= 25:
            comment = "It's really hot outside!"
        elif temp >= 20:
            comment = "It's hot outside!"
        elif temp >= 15:
            comment = "The weather is pleasant!"
        elif temp >= 5:
            comment = "Bring a light jacket!"
        elif temp >= 0:
            comment = "Bring a thicker jacket!"
        else:
            comment = "It's cold! Dress properly!"

        condition = weather_data["current"]["condition"]["text"]
        print("City:", city)
        print("Country:", country)
        print("Temperature:", temp, "°C")
        print("Weather:", condition)    
        print(f"Weather comment: {comment}")
    except KeyError:
        print("The city does not exist try another city")
        
