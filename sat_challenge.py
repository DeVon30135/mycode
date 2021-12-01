import requests
import datetime
import reverse_geocoder as rg


url = "http://api.open-notify.org/iss-now"

def main():
    response = requests.get(url).json()

    lat = response["iss_position"]["latitude"]
    lon = response["iss_position"]["longitude"]
    print(f"Latitude: {lat}")
    print(f"Longitude: {lon}")

    time = response["timestamp"]
    date_time = datetime.datetime.fromtimestamp(time)
    print(f"Timestamp: {date_time}")

    # reverse_geocoder MUST be passed a tuple as the argument!
    coords= (lat, lon)
    results= rg.search(coords)[0]
    state = results["cc"]
    city = results["admin2"]
    print(f"Location: {city}, {state}")

if __name__ == "__main__":
    main()
