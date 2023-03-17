from googleapiclient.discovery import build
from dotenv import dotenv_values

config = dotenv_values("../.env")

key = config["KEY"]
youtube = build('youtube', 'v3', developerKey = key)

channel_id = "CHANNEL_ID_HERE"
