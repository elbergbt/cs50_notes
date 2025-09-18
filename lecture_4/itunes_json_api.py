import json
import sys
import requests

music_band = input("Input music band: ")

response = requests.get('https://itunes.apple.com/search?entity=song&limit=1&term=' + music_band)

o = response.json()
for result in o['results']:
    print(result['trackName'])