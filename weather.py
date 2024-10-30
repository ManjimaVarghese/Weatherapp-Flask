from dotenv import load_dotenv
from pprint import pprint
import requests
import os
from bs4 import BeautifulSoup

load_dotenv()

def get_current_weather(city="Kansas City"):
    # Google search query URL
    search_url = f'https://www.google.com/search?q=weather+{city.replace(" ", "+")}'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
    }

    # Send the request to Google
    response = requests.get(search_url, headers=headers)

    # Check if the request was successful
    if response.status_code != 200:
        print("Failed to retrieve data.")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')

    # Initialize weather data dictionary
    weather_data = {
        "city": city,
        "temperature": "N/A",
        "unit": "N/A",
        "condition": "N/A"
    }

    # Parse the weather data safely
    temperature_element = soup.find("span", attrs={"id": "wob_tm"})
    unit_element = soup.find("div", attrs={"id": "wob_dts"})
    condition_element = soup.find("span", attrs={"id": "wob_dc"})

    if temperature_element:
        weather_data["temperature"] = temperature_element.text
    if unit_element:
        weather_data["unit"] = unit_element.text
    if condition_element:
        weather_data["condition"] = condition_element.text

    return weather_data

# Example usage
if __name__ == "__main__":
    print('\n*** Get Current Weather Conditions ***\n')

    city = input("\nPlease enter a city name: ").strip() or "Kansas City"
    
    weather_data = get_current_weather(city)

    if weather_data:
        print("\nWeather Data:")
        pprint(weather_data)
    else:
        print("Could not retrieve weather data.")
