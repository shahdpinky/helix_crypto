import tweepy

consumer_key = 'qKRFFvNNIUpScj7iQpL2ek46j'
consumer_secret = '62zToE7CYBRf2XzHXZ2gLgiNcHc5EMrDD5RNEEqzriqYYvt0qg'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAC8wVQEAAAAAnvokzWJQfmmwDKAs88YeIMhIBtw%3DvZeLO3cN0iI4rsL3LVjXnrrbApQn9QcU9ha3GC56FvMIHPWrjs'
access_token = '1421219775389306881-NhdpWiB7cX13ZXBXvNGa7AEsXsb9tl'
access_token_secret = 'sktF8EYNmkM9DtFHFNK6Ig58yrPHyVKOdPEfxIKEwVtJe'


class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)

    def on_error(self, status_code):
        if status_code == 420:
            # returning False in on_error disconnects the stream
            return False
        print(status_code)

    def on_data(self, data):
        print(data)
        return True


if __name__ == "__main__":
    myStreamListener = MyStreamListener()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    # api = tweepy.API(auth)
    myStream = tweepy.Stream(auth=auth, listener=myStreamListener)

    myStream.filter(follow=['1421219775389306881'])
