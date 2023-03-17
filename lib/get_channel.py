from googleapiclient.discovery import build
from dotenv import dotenv_values

config = dotenv_values("../.env")

key = config["KEY"]
youtube = build('youtube', 'v3', developerKey = key)

channel_id = "CHANNEL_ID_HERE"

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