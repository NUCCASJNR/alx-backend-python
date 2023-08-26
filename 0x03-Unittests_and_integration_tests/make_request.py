#!/usr/bin/env python3

import requests
import json

def fetch_data_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

if __name__ == "__main__":
    print(fetch_data_from_url("https://swapi-api.alx-tools.com/api/films/1"))
