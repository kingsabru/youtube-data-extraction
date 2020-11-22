import os
import json
import csv
import pandas as pd

from googleapiclient.discovery import build

api_key = os.environ.get('YOUTUBE_V3_API_KEY')

youtube = build('youtube', 'v3', developerKey=api_key)

request = youtube.search().list(
  part='snippet',
  type='video',
  q='#endsars',
  videoDuration='medium',
  publishedAfter='2020-01-01T00:00:00Z'
)

response = request.execute()
print(response)