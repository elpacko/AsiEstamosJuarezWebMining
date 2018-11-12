import tweepy
import configparser
import elasticInserter

def insertES(tweetID, insertBody):
    try:
        # print insertBody
        elasticInserter.es.index(index='tweets', doc_type='tweet', id=int(tweetID), body=insertBody)
    except Exception as e:
        print(e)
        print "error to insert to ES"
        pass



config = configparser.ConfigParser()
config.sections()
config.read('../settings.ini')
consumer_key = config['TOKENS']['consumer_key']
consumer_secret = config['TOKENS']['consumer_secret']
access_token = config['TOKENS']['access_token']
access_token_secret = config['TOKENS']['access_token_secret']


# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)
screen_name = '@lapolaka'
screen_name = '@diariodejuarez'
screen_name = '@netnoticiasmx'
for status in tweepy.Cursor(api.user_timeline, screen_name=screen_name, exclude_replies=True).items():
    #print status._json['text']
    insertBody = {
        "text": status._json['text'],
        "created_at": status.created_at,
        "screen_name": screen_name
    }
    insertES(status.id, insertBody)



