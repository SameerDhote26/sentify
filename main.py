from scrapeComments import Scrape
import re
import requests

API_TOKEN = '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'
API_URL = "https://api-inference.huggingface.co/models/sbcBI/sentiment_analysis_model"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

video_id = 'nBZT7lF5dag'

def query(payload):
    response = requests.post(API_URL,headers=headers,json=payload)
    return response.json()

def predict(prediction):
    for item in prediction:
        max = ['',0]
        for dict in item:
            if float(dict['score']) > float(max[1]):
                max[0] = dict['label']
                max[1] = dict['score']

    return max

def refine(text):
    text = re.sub(r'[^a-zA-Z0-9 ]','',text)
    return text
comments = Scrape(video_id=video_id)
commments_list = comments.scrape()

i = 1

for comment in commments_list['items']:
    comment_text =comment['snippet']['topLevelComment']['snippet']['textOriginal']
    comment_text = str(comment_text)
    comment_text = refine(comment_text)
    # print(f'{i}. {comment_text}')
    json = {'inputs':comment_text}
    prediction = query(json)
    print(predict(prediction),comment_text)
    i = i + 1