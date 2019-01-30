print('====================================================================================')
print('')

from textblob import TextBlob as TB
import sys, tweepy
import matplotlib.pyplot as plt

consumerkey = 'DvteP2PhQKnCcRxPhJQ3A3U0f'
consumersecretkey = 'AScugEoronUCzrPBe53L9uklXBzqdKIOtebBRQUNQDIE4FpkbI'
accesstoken = '772015734322978817-g132FcsbvE0hI12Bjo472iLr8PPISj6'
accesstokensecret = 'lmG1u5aylrh4BqOFMxVsE9fjjGfh7unMAaBd7fie2okV0'

authentication = tweepy.OAuthHandler(consumer_key = consumerkey, consumer_secret = consumersecretkey )
authentication.set_access_token(accesstoken, accesstokensecret)
my_api = tweepy.API(authentication)

# The text blob works in the following manner
# Say we have a sentence, if the sentnce describes something in a positive manner then Textblob will return 1
# If the sentence describes something to be negative it returns -1
# For a neutral sentence it returns 0

text_to_analyze = 'I am a very good man'
a = TB(text_to_analyze)
print(a.sentiment.polarity)

text_to_analyze = 'I am a best man'
a = TB(text_to_analyze)
print(a.sentiment.polarity)

text_to_analyze = 'I am a bad man'
a = TB(text_to_analyze)
print(a.sentiment.polarity)

text_to_analyze = 'I am a very bad man'
a = TB(text_to_analyze)
print(a.sentiment.polarity)

text_to_analyze = 'I am a man'
a = TB(text_to_analyze)
print(type(a))
print(a.sentiment.polarity)

search_word = input('Enter the hashtag or a word to be searched: ')
number = int(input('Enter number of tweets to be searched: '))

tweets = tweepy.Cursor(my_api.search, q=search_word, lang='English').items(number)

print('')

positive_sentiment = 0
negative_sentiment = 0
neutral_sentiment = 0

# Now looping through the 500 tweets
for tweet in tweets:
    examine = TB(tweet.text)
    if (examine.sentiment.polarity == 0):
        neutral_sentiment += 1
    elif (examine.sentiment.polarity > 0.00):
        positive_sentiment += 1
    elif (examine.sentiment.polarity < 1):
        negative_sentiment += 1

def percentage(sent, numb):
    return 100*float(sent)/float(numb)

positive_perc = percentage(positive_sentiment, number)
negative_perc = percentage(negative_sentiment, number)
neutral_perc = percentage(neutral_sentiment, number)

print(positive_perc)
print(negative_perc)
print(neutral_perc)
