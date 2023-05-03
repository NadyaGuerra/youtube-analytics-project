from googleapiclient.discovery import build
import os


class Video:
    api_key: str = os.getenv("YT_API_KEY")
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, video_id):
        self.__video_id = video_id
        self.__video = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                id=self.__video_id).execute()
        self.__title = self.__video['items'][0]['snippet']['title']
        self.__url = f'https://youtu.be/{self.__video_id}'
        #self.__url = f'https://www.youtube.com/watch?v={self.__video_id}'
        self.view_count = self.__video['items'][0]['statistics']['viewCount']
        self.like_count = self.__video['items'][0]['statistics']['likeCount']


@property
def url(self):
    return self.__url

@property
def title(self):
    return self.__title


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.__playlist_id = playlist_id

@property
def playlist_id(self):
    return self.__playlist_id
