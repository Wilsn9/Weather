# Weather App 🌦️

A simple Python weather application that uses WeatherAPI to fetch current weather data for a city.

## Purpose

I made this project to learn more about:
- APIs
- HTTP requests
- JSON handling
- Error handling in Python

## Features

- Search weather by city
- Shows temperature and weather condition
- Gives weather recommendations based on temperature

## Technologies Used

- Python
- Requests
- WeatherAPI

## Installation

- python -m venv venv
- source venv/bin/activate

```bash
pip install requests
pip install python-dotenv
```

In dotenv add your API key here:

```
API_KEY = "Your key"
```

## Run the Program

```bash
python main.py
```

## Example

```text
City: Stockholm
Country: Sweden
Temperature: 18 °C
Weather: Partly cloudy
Weather comment: The weather is pleasant!
```
