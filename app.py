
import tweepy
from  textblob import TextBlob 
import pandas as pd
import numpy as np
import re
import string
import pandas as pd
import streamlit as st


consumer_key = "pTivamyKt0GtxZiFizMMhsouj"
consumer_sec = "HEkXmzyaALIAD1AfTHLdRnegC8rstIY2AUHbrzvRGIjoJl3PCo"

# from proxy server we need to connect
access_token = "1490018179690602500-6dR6g69GHBE1fMZICvqyDMKrJINNyS"
access_token_sec = "ZAjbICteZd6FsbWEHeP2SIlmmdIycSEvgoOfJaXjf9wTs"
dir(tweepy)

auth=tweepy.OAuthHandler(consumer_key,consumer_sec)

auth.set_access_token(access_token,access_token_sec)

api_connect=tweepy.API(auth)

auth = tweepy.OAuthHandler(consumer_key,consumer_sec)
auth.set_access_token(access_token,access_token_sec)
api = tweepy.API(auth)
st.title("WELCOME!!!")

posts = api.user_timeline(screen_name="@Ria11871667", count = 10, lang ="en", tweet_mode="extended")
print("Show the 6 recent tweets:\n")
i=1
for tweet in posts[:9]:
    print(str(i) +') '+ tweet.full_text + '\n')
    i= i+1

d= pd.DataFrame([tweet.full_text for tweet in posts], columns=['Tweets'])


def cleanTxt(text):
 text = re.sub('@[A-Za-z0–9]+', '', text)
 text = re.sub('#', '', text)
 text = re.sub('https?:\/\/\S+', '', text)
 text = re.sub(':', '  ', text)
 text = re.sub('_','  ', text)

 return text

d['Tweets'] = d['Tweets'].apply(cleanTxt)


def getSubjectivity(text):
   return TextBlob(text).sentiment.subjectivity
def getPolarity(text):
   return  TextBlob(text).sentiment.polarity
d['Subjectivity'] = d['Tweets'].apply(getSubjectivity)
d['Polarity'] = d['Tweets'].apply(getPolarity)

net=0
neg=0
pos=0
def getAnalysis(score):
 global net,neg,pos
 if score < 0:
  neg+=1
  return 'Negative'
 elif score == 0:
  net+=1
  return 'Neutral'
 else:
  pos+=1
  return 'Positive'
d['Analysis'] = d['Polarity'].apply(getAnalysis)
(
 d
 .style
 .background_gradient(cmap="PuRd_r")

)

if(neg>pos):
  st.header("Sentimental Analysis of Tweets")
  st.write("The person is depressed!!!")
else:
  st.header("Sentimental Analysis of Tweets")
  st.write("The person is not depressed!!")
page_bg_img = '''
<style>
body {
background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)
d
