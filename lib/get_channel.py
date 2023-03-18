from googleapiclient.discovery import build
from dotenv import load_dotenv
import os

load_dotenv()

key = os.getenv("KEY")

youtube = build('youtube', 'v3', developerKey = key)

channel_id = "UC5uNya42ayhsRnZOR3mO6NA"

def get_channel():
    responseChannel = youtube.channels().list(
    part="snippet,contentDetails,statistics",
    id=channel_id
    ).execute()

    responseVideos = youtube.search().list(
    part="snippet",
    channelId=channel_id,
    type="video",
    order="date",
    maxResults=10
    ).execute()
    
    return responseChannel, responseVideos

