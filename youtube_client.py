import google_auth_oauthlib.flow
from googleapiclient.discovery import build

import creds

class YoutubeClient(object):
    def __init__(self):
        client_id = creds.CLIENT_ID
        client_secret = creds.SECRET_KEY

        scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

        credentials = google_auth_oauthlib.get_user_credentials(
            scopes, client_id, client_secret
        )

        self.youtube = build('youtube', 'v3',credentials=credentials)

    def video_comments(self, video_id): 
        video_response = self.youtube.commentThreads().list(
            part='snippet,replies', 
            videoId=video_id 
        ).execute() 

        comments = []

        while video_response: 
            for item in video_response['items']: 
                comments.append(item['snippet']['topLevelComment']['snippet'])

            if 'nextPageToken' in video_response: 
                video_response = self.youtube.commentThreads().list( 
                    part = 'snippet,replies', 
                    videoId = video_id, 
                    pageToken=video_response["nextPageToken"]
                ).execute() 
            else: 
                break

        return comments

    def set_thumbnail(self, video_id, file):
        self.youtube.thumbnails().set(
            videoId=video_id,
            media_body=file
        ).execute()