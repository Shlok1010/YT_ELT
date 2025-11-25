import requests as rs
import json

import os
from dotenv import load_dotenv
load_dotenv(dotenv_path="./.env" )

channelHandle = "MrBeast"
API_Key = os.getenv("API_KEY")

max_results = 50 # Number of results to retrieve

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



def get_video_id(playlist_id):

    video_ids = []
    page_token = None
    base_url = f"https://youtube.googleapis.com/youtube/v3/playlistItems?part=contentDetails&maxResults={max_results}&playlistId={playlist_id}&key={API_Key}"

    try:
        while True:

            url = base_url
            if page_token:
                url += f"&pageToken={page_token}"

            response = rs.get(url)
            response.raise_for_status()
            data = response.json()

            # FIXED: key name
            for item in data.get("items", []):
                video_id = item["contentDetails"]["videoId"]   # FIXED key
                video_ids.append(video_id)

            # FIXED: update the correct variable
            page_token = data.get("nextPageToken")

            # FIXED: break condition
            if not page_token:
                break

        return video_ids

    except rs.exceptions.RequestException as e:
        raise e


if __name__ == "__main__":
    playlist_id = get_playlist_id()   # <-- FIXED
    get_video_id(playlist_id)
