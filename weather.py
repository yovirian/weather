import requests

API_KEY = "d8a6ea215c53b8bc3b628bc81d69b822"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if response.status_code != 200:
            print("Error:", data.get("message", "City not found"))
            return

        # Extract data
        city_name = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"]

        # Display
        print("\nWeather Information")
        print("-------------------")
        print(f"Location     : {city_name}, {country}")
        print(f"Temperature  : {temp}°C")
        print(f"Feels Like   : {feels_like}°C")
        print(f"Humidity     : {humidity}%")
        print(f"Condition    : {condition}")

    except requests.exceptions.RequestException:
        print("Network error. Please check your internet connection.")

def main():
    print("=== Weather App ===")

    while True:
        city = input("\nEnter city name (or type 'exit'): ").strip()

        if not city:
            print("Please enter a valid city name.")
            continue

        if city.lower() == "exit":
            print("Goodbye!")
            break

        get_weather(city)

if __name__ == "__main__":
    main()
