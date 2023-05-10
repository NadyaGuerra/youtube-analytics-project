from googleapiclient.discovery import build
import os
import isodate
from datetime import timedelta


class PlayList:
    api_key: str = os.getenv("YT_API_KEY")
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, playlist_id):
        self.__playlist_id = playlist_id  # инициализация id
        self.playlist_videos = self.youtube.playlistItems().list(playlistId=playlist_id,
                                                                 part='contentDetails',
                                                                 maxResults=50,
                                                                 ).execute()

        self.video_ids = [video['contentDetails']['videoId'] for video in self.playlist_videos['items']]
        self.__video = self.youtube.videos().list(part='contentDetails,statistics',
                                                  id=self.video_ids).execute()

        self.info = self.youtube.playlists().list(part='snippet',
                                                  id=self.__playlist_id, ).execute()
        self.title = self.info['items'][0]['snippet']['title']  # получаю название
        self.url = f'https://www.youtube.com/playlist?list={self.__playlist_id}'  # ссылка на канал

    @property
    def total_duration(self):
        time = timedelta(seconds=0)

        for video in self.__video['items']:
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            time += duration
        return time

    def show_best_video(self):
        video = ""
        likes = 0
        for video in self.__video["items"]:
            like = video["statistics"]["likeCount"]
        if int(like) > likes:
            likes = int(like)
            video = f"https://youtu.be/{video['id']}"
            return video
