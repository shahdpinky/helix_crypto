import tweepy  # use 3.10.0
import json

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
        data_dict = json.loads(data)
        # if (not data_dict['retweeted']) and ('RT @' not in data_dict['text']) and (
        if str(data_dict['user']['id']) in user_ids:
            output = f"{data_dict['created_at']}    {data_dict['user']['screen_name']}: {data_dict['text']}"
            print(output)
        return True


if __name__ == "__main__":
    myStreamListener = MyStreamListener()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    # api = tweepy.API(auth)
    myStream = tweepy.Stream(auth=auth, listener=myStreamListener)

    # my id
    print('start monitoring')
    user_ids = ['1154010518790791168',  # HighStakesCap: eth sol accurate
                '1289071298556170240',  # GCR: meme coin god
                '944686196331966464',  # Hsaka: good moral
                '1138993163706753029',  # pentoshi: random alts
                '906234475604037637',  # CryptoKaleo
                '924874169157849088',  # Robin god
                '887748030304329728',  # cryptodog
                '1421219775389306881',  # myself for testing
                ]
    myStream.filter(follow=user_ids)
