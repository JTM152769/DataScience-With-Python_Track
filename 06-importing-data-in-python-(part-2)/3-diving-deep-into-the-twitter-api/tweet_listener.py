'''Here I define a Tweet listener that creates a file called 'tweets.txt', collects streaming tweets as 
.jsons and writes them to the file 'tweets.txt'; once 100 tweets have been streamed, the listener closes
the file and stops listening. 






class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api=None):
        super(MyStreamListener, self).__init__()
        self.num_tweets = 0
        self.file = open("tweets.txt", "w")

    def on_status(self, status):
        tweet = status._json
        self.file.write( json.dumps(tweet) + '\n' )
        self.num_tweets += 1
        if self.num_tweets < 100:
            return True
        else:
            return False
        self.file.close()

    def on_error(self, status):
print(status)
