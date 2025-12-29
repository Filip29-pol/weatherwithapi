import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

def get_data(place, forecasted_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()

    # Check if the API returned an error
    if "list" not in data:
        print(f"Error from API: {data.get('message', 'Unknown error')}")
        return None

    # Calculate values (8 readings per day for a 5-day forecast)
    nr_values = 8 * forecasted_days
    filtered_data = data["list"][:nr_values]

    return filtered_data

if __name__ == "__main__":
    # Wrap in a check to avoid printing 'None' if it fails
    result = get_data(place="Tokyo", forecasted_days=3)
    if result:
        print(result)

