# Extracting Video Data Using Youtube API V3

This project demonstrates how to work with the Youtube V3 API in python. Using the Google API Client library for python, you can scrap data from Youtube. The project also shows how  to store the extracted data into a CSV file.

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

## Pre-requisites

* GCP Project
* Youtube V3 API Key  
Watch this [youtube tutorial](https://www.youtube.com/watch?v=sVEytWDWYwM)  to create a Youtube V3 API Key.

## Getting Started

The project was developed using:

* Python 3.7.9
* Anaconda (conda)
* Google API Client
* Pandas

Follow the steps below to setup the project.
### Create environment

Create a conda environment using the command:
```
conda create -n "env-name" python=3.7
```

### Activate environment

Activate the environment using the command:
```
conda activate env-name
```

### Install packages

Install project packages using the command:
```
pip install -r requirements.txt
```

### Store env variables

To store your access credentials (examples: API keys, Database access credentials), follow the steps below: 

1. Duplicate *.env.example* file and create a new file names *.env*
2. Store your access credentials as needed


Warning: Keep your API key private. If someone obtains your key, they could use it to consume your quota or incur charges against your Google Cloud project.




## Resources

#### Documentations

* [Youtube V3 API - Getting Started](https://developers.google.com/youtube/v3/getting-started)
* [Google API Python Client Github](https://github.com/googleapis/google-api-python-client/blob/master/docs/start.md)

## Tutorial Articles

* [How to Extract & Analyze YouTube Data using YouTube API?](https://www.analyticssteps.com/blogs/how-extract-analyze-youtube-data-using-youtube-api)
