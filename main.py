from weather import get_city, get_weather
  
while True:
    city_name = input("Enter the city you would like to check the weather for (exit to quit): ").lower()
    if city_name == "exit":
        break

    weather = get_city(city_name)

    get_weather(weather)