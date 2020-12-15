# Extracting Video Data Using Youtube API V3
## Task
Write a script that extracts YouTube data to analyze the #endsars# trend that rocked the entire world.
The script should be able to perform the following:
* Filter out channels and playlists.
* Get only videos published this year.
* Include videos that are between 4 to 20 mins long.
* Generic such that the search query can be changed.

### Output
Store the output into a csv with the filename having the following format: current_timestamp_youtube_data.

The following video attributes should be a part of the dataset:
* the time video was published
* the video id
* the title of the video
* description
* the URL of the video thumbnail
* number of views
* number of likes
* number of dislikes
* number of comments

Create an additional the column that builds the video URL using the video id.
## Setup
### Pre-requisites
* Pandas
* google-api-python-client
* Youtube V3 API Key

### Installations

## How to create and access password and secret keys from system environment
url: https://youtu.be/IolxqkL7cD8

## Generate API Credentials
## Store API Key in system environment
## Uncomment API_KEY variable
Warning: Keep your API key private. If someone obtains your key, they could use it to consume your quota or incur charges against your Google Cloud project.
## Install the Google APIs Client Library for Python
pip install --upgrade google-api-python-client
Or better, check the Youtuve V3 doc for latest code
url: https://developers.google.com/youtube/v3/quickstart/python



# Resources Used
url: https://github.com/googleapis/google-api-python-client/blob/master/docs/start.md
