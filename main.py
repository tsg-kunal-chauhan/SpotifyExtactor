import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Global Song List
songsName = ['abc.mp3', 'xyz ahs 8uj - .mp3']

# Address to fetch the files
# path = "C://Users//Vanshi//Desktop//gfg"
# songsName = os.listdir(path)

# loop to fetch only the song names (splitting the mp3 extension)
for i in range(len(songsName)):
    songsName[i] = songsName[i].split('.')[0]

# Calling API for access Token
headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}
data = "grant_type=client_credentials&client_id=" + \
    os.getenv('client_id')+"&client_secret="+os.getenv('client_secret')

try:
    accessTokenJson = requests.post(
        'https://accounts.spotify.com/api/token', headers=headers, data=data)
    print(accessTokenJson.status_code)

    if (accessTokenJson.status_code != 200):
        print("API status not 200 for access Token")
        quit()

    accessTokenJson = accessTokenJson.json()

except:
    print("Error calling the API for access Token")
    quit()

accessToken = accessTokenJson["access_token"]
print(accessToken)
# API call
# response = requests.get("")


print(songsName)
