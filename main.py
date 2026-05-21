import weather
  
while True:
    city_name = input("Enter the city you would like to check the weather for (exit to quit): ").lower()
    if city_name == "exit":
        break
    weather_data = weather.get_city(city_name)
    if weather_data:
        weather.get_weather(weather_data)