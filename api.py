# coding: utf-8
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""


class StdOutListener(StreamListener):    
    
    def on_data(self, data):
        data = json.loads(data)
        text = data['text']
        time = data['created_at']

        print('Text: '+text)
        print('Time: '+time)
        print('========')

        #save wteets by mask
        #text = str(text.encode('utf-8'))
        #file = open('123.txt', 'a+')
        #file.write("\r\n"+text)
        #file.close()
        
        return True
    
    def on_error(self, status):
        print(status)
        
if __name__ == '__main__':

    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    print('Starting Streaming API')
    stream = Stream(auth, l)

    stream.filter(track=['usa'])