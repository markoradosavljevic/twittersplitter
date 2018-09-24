# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "1001175056322629632-ZutZIWO6HCFsM3SyTat5UNqclJ2iGy"
access_token_secret = "d8wg4AfF7iYakp4dESM1cI6gwZVjk9GXaLDVKv1TUFgs1"
consumer_key = "9M5alUSR5uVgxsDEttrGFAeQ5"
consumer_secret = "fMMnrzqIwg97nzhVohiPzbgvrUGzQczQP4EcrLrhNfXXRHHrIm"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['brnabic','vuk jeremic','vlast','porodiljsko','trudnicko','djilas','opozicija', 'savez za srbiju', 'lutovac'])