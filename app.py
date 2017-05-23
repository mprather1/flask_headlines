import feedparser
from flask import Flask
from flask_json import FlaskJSON, JsonError, json_response, as_json
import json

app = Flask(__name__)
FlaskJSON(app)

BBC_FEED = "http://feeds.bbci.co.uk/news/rss.xml"

@app.route('/')
def get_news():
  arr = []
  
  feeds = feedparser.parse(BBC_FEED)
  
  for feed in feeds['entries']:
    data = {
      'title': feed.get('title'),
      'published': feed.get('published'),
      'summary': feed.get('summary')
    }
    
    json_str = json.dumps(data)
    
    arr.append(feed)
  
  return json_response(feeds=set(arr))


if __name__ == "__main__":
  app.run(port=8000, host='0.0.0.0', debug=True)