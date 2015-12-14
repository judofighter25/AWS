import tweepy

consumer_key = "XdVRmPY3BJ9SjMmDALvLMkxe2";



consumer_secret = "hWdvpb1YnzOtaVPMKJvxe3WImo6qFA9vXhDczP5APO8OD0thoj";

access_token = "1095120943-FjsNf5xiRst1pWMHyH8GBjBxLpXlPqMCWIjmVMw";

access_token_secret = "b0XIamwRPMTusKmuoLppxeg7Uefa61CXEW68eEBHkEzm8";


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



