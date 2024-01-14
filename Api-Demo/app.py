import requests
import json

def fetch_random_cat():
    url = "https://meowfacts.herokuapp.com/"
    try:
        response = requests.get(url)
        response.raise_for_status()

        fact = response.json()["data"][0]
        return fact
    except requests.exceptions.HTTPError as err:
        print(f"Error: {err}")
        return None

def fetch_random_dog():
    url = "https://dog-api.kinduff.com/api/facts"
    try:
        response = requests.get(url)
        response.raise_for_status()

        fact = response.json()["facts"][0]
        return fact
    except requests.exceptions.HTTPError as err:
        print(f"Error: {err}")
        return None

if __name__ == "__main__":
    print(fetch_random_cat())
    print(fetch_random_dog())

