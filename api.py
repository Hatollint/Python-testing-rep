# coding: utf-8
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

access_token = "2167863662-kxfvpit4ovRcXtLFbxbj0GA221YRZPoKvbD09LL"
access_token_secret = "RX1tfvsgMUdmYLYSxlvITrKitBi0zaROAdhGM7CeLKjXG"
consumer_key = "9abTYr6PaeSMU8vIRSoUJTXxH"
consumer_secret = "oqmzkBfYkCFFDSKF8eF3LAHsRh1tULn2yeR2yXnoDtZnbfqtpn"


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