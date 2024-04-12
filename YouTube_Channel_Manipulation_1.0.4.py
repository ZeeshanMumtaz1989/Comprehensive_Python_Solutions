"""
Author: Zeeshan Mumtaz
Date: April 10, 2024
Description: Using Google CLoud API Key for YouTube, this script extract following
4 x attributes of any given YouTube Channel:

1 - Title of the Video/ Shorts
2 - Duration in Minutes and Seconds
3 - Number of Total Views so far
4 - Total Comments by the Audience.

After extrating all of the 4 attributes, the results are stored in a CSV File

"""



import csv
import os
import googleapiclient.discovery
from unidecode import unidecode
from datetime import datetime
import concurrent.futures

API_KEY = "AIzaSyAQd1ufQzgJazZmGIi-FuldRywH2_BJdIE"

def get_channel_videos(channel_id):
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=API_KEY)

    # Retrieve playlist ID of the uploaded videos
    res = youtube.channels().list(id=channel_id, part="contentDetails").execute()
    playlist_id = res["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]

    videos = []
    next_page_token = None

    while True:
        # Retrieve videos from the playlist
        res = youtube.playlistItems().list(
            playlistId=playlist_id,
            part="snippet",
            maxResults=50,
            pageToken=next_page_token
        ).execute()

        videos += res["items"]
        next_page_token = res.get("nextPageToken")

        if not next_page_token:
            break

    return videos

def get_video_details(video_id):
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=API_KEY)

    # Retrieve video details
    res = youtube.videos().list(
        id=video_id,
        part="snippet,contentDetails,statistics"
    ).execute()

    video = res["items"][0]
    return video

def clean_title(title):
    return unidecode(title)

def write_to_csv(filename, videos):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Duration', 'Views', 'Comments'])
        for video in videos:
            title = clean_title(video["snippet"]["title"])
            print(title)
            duration = video.get("contentDetails", {}).get("duration", "N/A")
            views = video.get("statistics", {}).get("viewCount", "N/A")
            comments = video.get("statistics", {}).get("commentCount", "N/A")
            writer.writerow([title, duration, views, comments])

def main():
    channel_id = "UCvz84_Q0BbvZThy75mbd-Dg"
    videos = get_channel_videos(channel_id)

    # Using ThreadPoolExecutor to fetch video details concurrently
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        # Fetching details for all videos concurrently
        video_details = list(executor.map(lambda video: get_video_details(video["snippet"]["resourceId"]["videoId"]), videos))

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"youtube_videos_{timestamp}.csv"
    write_to_csv(filename, video_details)
    print(f"CSV file '{filename}' containing all videos has been created.")

if __name__ == "__main__":
    main()
