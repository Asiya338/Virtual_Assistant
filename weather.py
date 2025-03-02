import requests

def Weather(query="karimnagar,in"):
    api_key = " 908i_90jnmshaiojnzx009qkc4810e71e"  # Replace with your actual API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={query}&appid={api_key}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        if "main" in data:
            description = data["weather"][0]["description"]
            
            # Check for specific weather conditions and return an appropriate message
            if "clear" in description:
                return "Today is sunny."
            elif "cloud" in description:
                return "Today is cloudy."
            elif "rain" in description:
                return "Today is rainy."
            elif "humidity" in description:
                return "Today is humid."
            else:
                return "Weather condition not recognized."
        else:
            return "Weather data not available for this location."
    else:
        return f"Error: Unable to fetch data (Status code: {response.status_code})"

# Test the function
print(Weather())

