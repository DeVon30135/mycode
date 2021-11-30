#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

def main():
        ## Ask user for input
        got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )

        ## Send HTTPS GET to the API of ICE and Fire character resource
        gotresp = requests.get(AOIF_CHAR + got_charToLookup)

        ## Decode the response
        got_dj = gotresp.json()
        houses = got_dj["allegiances"]
        books = got_dj["books"]
        pov_books = got_dj["povBooks"]

        pprint.pprint("All Character Info:")
        pprint.pprint(got_dj)

        print("\nName: " + got_dj["name"])

        print("\nList of houses:")
        for house in houses:
            print(requests.get(house).json()["name"])

        print("\nList of books:")
        for book in books:
            print(requests.get(book).json()["name"])

        for pov_book in pov_books:
            print(requests.get(pov_book).json()["name"])

if __name__ == "__main__":
        main()
