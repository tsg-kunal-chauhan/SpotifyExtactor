import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Global Song List
songsName = ['abc.mp3', 'xyz ahs 8uj - .mp3']
spotifySongURI = []

def populateSongs():
    # # Address to fetch the files
    # # path = "C://Users//Vanshi//Desktop//gfg"
    # try:
    #     # songsName = os.listdir(path)
    # except:
    #     print("Unable to fetch songs from the given destination")
    return

def processSongsList():
    # loop to fetch only the song names (splitting the mp3 extension)
    for i in range(len(songsName)):
        songsName[i] = songsName[i].split('.')[0]
    
    return

def retrieveAccessToken():
    # Calling API for access Token
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    data = "grant_type=client_credentials&client_id=" + \
        os.getenv('client_id')+"&client_secret="+os.getenv('client_secret')

    try:
        accessTokenJson = requests.post(
            'https://accounts.spotify.com/api/token',
            headers=headers,
            data=data)

        if (accessTokenJson.status_code != 200):
            print("API status not 200 for access Token. The response code is " +
                accessTokenJson.status_code)
            quit()

        accessTokenJson = accessTokenJson.json()

    except:
        print("Error calling the API for access Token")
        quit()

    accessToken = accessTokenJson["access_token"]

    # print(accessToken)
    return accessToken

def callAPItoSearchPopulateSongsURI(accessToken):
    # API call
    headers = {
        'Authorization': 'Bearer ' + accessToken}

    try:
        response = requests.get('https://api.spotify.com/v1/search?' +
                                'q=dil+kyu+yeah+mera' +
                                '&type=track&limit=1',
                                headers=headers
                                )

        if (response.status_code != 200):
            print("API status not 200 for track search. The response code is " +
                response.status_code)
            quit()

        response = response.json()

    except:
        print("Error calling the API for track search")
        quit()

    spotifySongURI.append(response['tracks']['items'][0]['uri'])

    # print(spotifySongURI)
    return 

populateSongs()
processSongsList()
accessToken =  retrieveAccessToken()
callAPItoSearchPopulateSongsURI(accessToken)

#print(spotifySongURI)
# print(songsName)
