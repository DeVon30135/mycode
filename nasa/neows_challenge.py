#!/usr/bin/python3
import requests
import pprint

## Define NEOW URL
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

# this function grabs our credentials
# it is easily recycled from our previous script
def returncreds():
    ## first I want to grab my credentials
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")
    return nasacreds

# this is our main function
def main():
    ## first grab credentials
    nasacreds = returncreds()

    ## update the date below, if you like
    startdate = input("Enter start date (YYYY-MM-DD):")
    enddate = input("Enter end date (YYYY-MM-DD):")

    ## the value below is not being used in this
    ## version of the script
    # enddate = "end_date=END_DATE"

    # make a request with the request library
    neowrequest = requests.get(f"{NEOURL}{startdate}&{enddate}&{nasacreds}")

    # strip off json attachment from our response
    neodata = neowrequest.json()
    total_count = neodata["element_count"]

    print(f"Total Asteroids: {total_count}")

    asteroids = neodata["near_earth_objects"]
    danger_count = 0
    biggest_size = 0
    miss_distance= 10000
    for dates in asteroids:
        for asteroid in asteroids[dates]:
            if asteroid["is_potentially_hazardous_asteroid"]:
                danger_count += 1
            if asteroid["estimated_diameter"]["meters"]["estimated_diameter_max"] > biggest_size:
                biggest_size = asteroid["estimated_diameter"]["meters"]["estimated_diameter_max"]
            miss = float(asteroid["close_approach_data"][0]["miss_distance"]["lunar"])
            if miss < miss_distance:
                miss_distance = miss

    print(f"REQUEST URL: {NEOURL}{startdate}&{enddate}&{nasacreds}")
    print(f"Total Dangerous Asteroids: {danger_count}")
    print(f"Largest Asteroids (Meters): {biggest_size}")
    print(f"Closest Call (lunar): {miss_distance}")

if __name__ == "__main__":
    main()
