import requests as rs
import json

import os
from dotenv import load_dotenv
load_dotenv(dotenv_path="./.env" )

channelHandle = "MrBeast"
API_Key = os.getenv("API_KEY")

def get_playlist_id():

    try:
    
        url = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={channelHandle}&key={API_Key}"

        response = rs.get(url)
        response.raise_for_status()

        data = response.json()

        channelItems = data["items"][0]
        channelPlaylistId = channelItems["contentDetails"]["relatedPlaylists"]['uploads']
        
        #print(channelPlaylistId)
        
        return channelPlaylistId

    except rs.exceptions.RequestException as e:
        raise e


if __name__ == "__main__":
    get_playlist_id()
