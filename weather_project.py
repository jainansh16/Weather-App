import requests

def weather(city, key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric"
    result = requests.get(url)
    data = result.json()

    if data["cod"] == 200:

        c_temp = data["main"]["temp"]
        k_temp = c_temp + 273.15
        f_temp = ((c_temp * 9) / 5) + 32
        weather_data = data["weather"][0]["description"]

        print(f"Weather in {city}:\n")
        print(f"Temperature in Kelvin: {k_temp} K\n")
        print(f"Temperature in Celsius: {c_temp} °C\n")
        print(f"Temperature in Fahrenheit: {f_temp} °F\n")
        print(f"Weather Description: {weather_data}\n")

    else:

        print(f"Was not able to fetch data for {city}")

def main():

    city_name = input("Enter city name here: ")
    api_key = 'c50e22e4bc8510f0cb076b1a026552b6'
    weather(city_name, api_key)

main()