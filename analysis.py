import tweepy

# Consumer keys and access tokens, used for OAuth
from tweepy import Stream
from tweepy import StreamListener

consumer_key = 'wkGiUdy48psyiXsvZqbgJVCk8'
consumer_secret = '4568Wi7QUS6yUooxmuZ0Mlo7BbToMdti8IAaq59Aho4czkeMYb'
access_token = '795592327775580160-hfQblj4Ray0vzt9yVNUYnZeDrUmhJzw'
access_token_secret = 'oE2wyUGIVReZ1zVDvq9J7NfKEEv3ILULvMbGEJCBs7qFA'

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

# Sample method, used to update a status
# api.update_status('Hello Python Central!')


class StdOutListener(StreamListener):
    ''' Handles data received from the stream. '''

    def on_status(self, status):
        # Prints the text of the tweet
        print('Tweet text: ' + status.text)

        # There are many options in the status object,
        # hashtags can be very easily accessed.
        print(status)
        # for hashtag in status.entries['hashtags']:
        #     print(hashtag['text'])

        return True


    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True  # To continue listening


    def on_timeout(self):
        print('Timeout...')
        return True  # To continue listening


class Candidate():
    def __init__(self, handle):
        self.handle = handle
        self.favourites = 0
        self.retweets = 0
        self.followers = 0
        self.tweets = 0

        self.me = api.get_user(handle)
        self.followers = self.me.followers_count

    def analyse(self):
        tweets = api.user_timeline(self.handle, count=100)
        for tweet in tweets:
            self.favourites += tweet.favorite_count
            self.retweets += tweet.retweet_count
            self.tweets += 1

    def report(self):
        print(self.handle)
        score = (self.retweets * self.favourites)/(self.followers)
        print("Score:    ", score)
        print("Tweets:   ", self.tweets)
        print("Favs:     ", self.favourites)
        print("RTs:      ", self.retweets)
        print("Followers:", self.followers)
        print("")


if __name__ == '__main__':
    # listener = StdOutListener()
    # auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    # auth.set_access_token(access_token, access_token_secret)
    #
    # stream = Stream(auth, listener)
    # # stream.filter(follow=[38744894], track=['@realDonaldTrump'])
    # stream.filter(track=['#mondaymotivation'])

    candidates = [ Candidate("@realDonaldTrump"), Candidate("@HillaryClinton") ]

    for candidate in candidates:
        candidate.analyse()
        candidate.report()
