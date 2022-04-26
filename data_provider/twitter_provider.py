
import json
import os

import backoff
import tweepy

consumer_key = 'jLJ3NjkfpbxRcXEHFcZqtnKmx'
consumer_secret = 'rAnHN5JCAtaDqiTqw89FS4Zaj07HGfC5Ajs154oTa7Cy6uaqIq'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAKDWawEAAAAA6umME4eN29IYIwlS6MUbfUSj%2Bks%3DY3sDH9GjKKJfxTtmTQbzPF1DHu1I3QKhUVxCr0jZCJYHYqdi2B'
access_token = '1421219775389306881-Anuu22AzKYrzCX9hrdrymryk4mGmqu'
access_token_secret = 'tcQ8hYRe1PhVXwBiHkysRSFnUVtM0g475BXP4Zb2BpkNq'


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

@backoff.on_exception(backoff.expo, (tweepy.error.RateLimitError))
def get_friends(user):
    data_folder = 'data/'
    #create data folder if it does not exist
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)
    #create user folder if it does not exist
    if not os.path.exists('{}{}'.format(data_folder, user)):
        os.makedirs('{}{}'.format(data_folder, user))
    #check if friends file exists
    if os.path.isfile('{}{}/friends.json'.format(data_folder, user)):
        #read friends from disk
        with open('{}{}/friends.json'.format(data_folder, user), 'r') as f:
            friends = json.load(f)
    else:
        #get friends from twitter
        try:
            friends = api.friends_ids(user)
        except tweepy.error.TweepError as e:
            print(e)
            friends = [user]
        #write friends to disk
        with open('{}{}/friends.json'.format(data_folder, user), 'w') as f:
            json.dump(friends, f)
    #print(friends)
    return friends
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
