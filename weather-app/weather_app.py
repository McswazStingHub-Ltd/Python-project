import requests

cities = {
    "lagos": (6.4550, 3.3841),
    "abuja": (9.0765, 7.3986),
    "kano": (12.0022, 8.5920),
    "port harcourt": (4.8156, 7.0498),
}

print("=" * 40)
print("Live Weather App")
print("=" * 40)

city = input("Enter city: ").strip().lower()

if city not in cities:
    print("Sorry, city not found.")
    exit()

lat, lon = cities[city]

url = (
    f"https://api.open-meteo.com/v1/forecast"
    f"?latitude={lat}&longitude={lon}"
    f"&current=temperature_2m,relative_humidity_2m,wind_speed_10m"
)

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    weather = response.json()["current"]

    print("\nCurrent Weather")
    print("-" * 40)
    print(f"City: {city.title()}")
    print(f"Temperature : {weather['temperature_2m']} °C")
    print(f"Humidity    : {weather['relative_humidity_2m']} %")
    print(f"Wind Speed  : {weather['wind_speed_10m']} km/h")

except requests.exceptions.RequestException as e:
    print("\nNetwork Error")
    print(e)
