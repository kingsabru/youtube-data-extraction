import os
import pandas as pd
import time
from decouple import config

from googleapiclient.discovery import build

def searchs_query(youtube_obj, rate_limit:int, query_str:str, max_results:int, videoDuration:str, type:str):
  next_page_token = None
  allItems = []

  count = 0

  while (count < rate_limit) and 1:
    request = youtube_obj.search().list(
        part='snippet',
        type=type,
        q=query_str,
        videoDuration=videoDuration,
        publishedAfter='2020-01-01T00:00:00Z',
        maxResults=max_results,
        pageToken=next_page_token
    )

    response = request.execute()

    allItems += response['items']

    next_page_token = response.get('nextPageToken')

    count += 1

    if next_page_token is None:
      break
  
  return allItems

def video_query(youtube_obj, videoIds, part):
  items = []
  count = 0

  while (count < len(videoIds)) and 1: 
    request = youtube_obj.videos().list(
        part='snippet, statistics',
        id=",".join(videoIds[count:count+50]),
    )

    response = request.execute()
    
    items += response['items']
    
    count+=50

  return items

def extract_video_id(items:list):
  return list(map(lambda x:x['id']['videoId'], items))

def extract_data(items:list):
  video_id = []
  video_title = []
  video_desc = []
  time_published = []
  thumbnail_url = []
  view_count = []
  like_count = []
  dislike_count = []
  comments_count = []
  video_url = []

  for i in items:
    video_id.append(i['id'])
    video_title.append(i['snippet']['title'])
    video_desc.append(i['snippet']['description'])
    time_published.append(i['snippet']['publishedAt'])  
    thumbnail_url.append(i['snippet']['thumbnails']['default']['url'])
    
    view_count.append(i['statistics'].get('viewCount'))
    like_count.append(i['statistics'].get('likeCount'))
    dislike_count.append(i['statistics'].get('dislikeCount'))
    comments_count.append(i['statistics'].get('commentCount'))
    
    video_url.append("https://www.youtube.com/watch?v=" + i['id'])
  
  data = {
    'videoId': video_id,
    'tltle': video_title,
    'description': video_desc,
    'timePublished': time_published,
    'thumnailUrl': thumbnail_url,
    'views': view_count,
    'likes': like_count,
    'dislikes': dislike_count,
    'comments': comments_count,
    'videoUrl': video_url
  }
  
  print("Data extracted successfully")

  return data

def store_data(data):
  current_timestamp = time.strftime("%Y%m%d-%H%M%S")
  file_name = current_timestamp+"_youtube_data.csv"
  data.to_csv(file_name, index=False)

  # TODO: Refactor to only return 1 or Success
  print("File created successfully. File name is {0}".format(file_name))

def main():
  # setting Youtube API_KEY
  api_key = config('API-KEY')

  # TODO: Reconfigure how env variable is accessed. 
  #       Use Resource: https://able.bio/rhett/how-to-set-and-get-environment-variables-in-python--274rgt5#:~:text=To%20set%20and%20get%20environment%20variables%20in%20Python%20you%20can,Get%20environment%20variables%20USER%20%3D%20os.
  youtube = build('youtube', 'v3', developerKey=api_key)

  # setting parameters
  request_rate_limit = 2
  max_results = 50
  search_query = "Maradona"
  search_type= 'video'
  video_duration = 'medium'

  print("Search Rate Limit has been set to {0}.".format(request_rate_limit))

  resultList = searchs_query(youtube, request_rate_limit, search_query, max_results, video_duration, search_type)
  print("Search request successful. The response contains {0} items".format(len(resultList)))

  video_ids = extract_video_id(resultList)
  print("Video IDs extracted successfully.")

  videoList = video_query(youtube, video_ids, 'snippet, statistics')
  print("Videos request successful.")

  data = extract_data(videoList)

  df = pd.DataFrame(data)

  store_data(df)

if __name__ == "__main__":
  main()