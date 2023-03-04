from googleapiclient.discovery import build

api_key = 'AIzaSyA9ruse2CM1c4BUTClUapc_CyLM2bbtMkc'





class Scrape():
    api_key = 'AIzaSyA9ruse2CM1c4BUTClUapc_CyLM2bbtMkc'

    def __init__(self,video_id) -> None:
        self.video_id = video_id
    
    def scrape(self):
        youtube = build('youtube','v3',developerKey=api_key)

        comments = youtube.commentThreads().list(part="snippet",maxResults="100",videoId=self.video_id).execute()

        return comments