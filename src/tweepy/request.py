import tweepy

access_token = "2441775246-zPKRTNRx5y7Ocu0SiCmNTs9VmaMWXaLPqH7UAnY"
access_token_secret = "zInt4CvFdujo9O77dE8zH3193RiWy3k2jiv6x81IAIWg9"
consumer_key = "GbTukY7r10xHsWKls4oGq3DIw"
consumer_secret = "mjBF1dAboaREGHtmQQp4yd8x4LhuSuenFFb4DRWcrPKw2P9rui"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

my_follower_ids = api.get_follower_ids()

followers_tree = {"followers": []}
for id in my_follower_ids:
    # get the followers of your followers
    try:
        follower_ids = api.get_follower_ids(user_id=id)
    except tweepy.errors.Unauthorized:
        print("Unauthorized to access user %d's followers" % (id))

    followers_tree["followers"].append({"id": id, "follower_ids": follower_ids})
