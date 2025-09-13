
**Code (weather.py)**  
```python
import requests

API_KEY = "your_api_key_here"  # get from https://openweathermap.org/
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter city: ")
url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
res = requests.get(url).json()

if res.get("main"):
    print(f"Weather in {city}: {res['weather'][0]['description']}")
    print(f"Temperature: {res['main']['temp']}°C")
    print(f"Humidity: {res['main']['humidity']}%")
else:
    print("City not found!")
