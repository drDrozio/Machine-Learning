# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 12:21:47 2020

@author: Ishan SS
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from wordcloud import WordCloud,STOPWORDS
import matplotlib.pyplot as plt

st.title("Twitter Sentiment Analysis")
st.markdown("Web App analysing Twitter US Airline Sentiments")

st.sidebar.title("Analysis Parameters")
st.sidebar.markdown("Toggle with given parameters to get desired outputs")

@st.cache(persist=True)
def load_data(path):
    data=pd.read_csv(path)
    data['tweet_created']=pd.to_datetime(data['tweet_created'])
    return data

trainData=load_data('twitter_train.csv')
testData=load_data('twitter_test.csv')

st.write(trainData)

st.sidebar.subheader("Show Random Tweet")
random_tweet=st.sidebar.radio('Sentiment',('positive','neutral','negative'))
st.sidebar.markdown(trainData.query('airline_sentiment == @random_tweet')[['text']].sample(n=1).iat[0,0])

st.sidebar.subheader("Number of Tweets by sentiment")
select= st.sidebar.selectbox('Visualization Type',['Histogram','Pie Chart'],key='1')
senti_counts=trainData['airline_sentiment'].value_counts()
senti_counts=pd.DataFrame({'Sentiments':senti_counts.index, 'Tweets':senti_counts.values})
if st.sidebar.checkbox("Show",False):
    st.markdown("### Number of tweets by sentiment")
    if select == 'Histogram':
        fig=px.bar(senti_counts,x='Sentiments',y='Tweets',color='Tweets',height=500)
        st.plotly_chart(fig)
    else:
        fig=px.pie(senti_counts,values='Tweets',names='Sentiments')
        st.plotly_chart(fig)
        
st.sidebar.subheader("Breakdown airline tweets by sentiment")
choice=st.sidebar.multiselect('Pick airlines',('US Airways','United','American','Southwest','Delta','Virgin America'),key='0')
if len(choice)>0:
    choice_data=trainData[trainData.airline.isin(choice)]
    fig1=px.histogram(choice_data,x='airline',y='airline_sentiment',histfunc='count',color='airline',facet_col='airline_sentiment',
                      labels={'airline_sentiment':'tweets'},height=600,width=800)
    st.plotly_chart(fig1)

st.sidebar.subheader("Word Cloud")
word_senti=st.sidebar.radio('Display wordcloud for what sentiment?',('positive','neutral','negative'))
if st.sidebar.checkbox("Show",False,key='3'):
    st.header('Word Cloud for %s sentiment'% (word_senti))
    df=trainData[trainData['airline_sentiment']==word_senti]
    words=''.join(df['text'])
    processed_words=''.join([word for word in words.split() if 'http' not in word and word.startswith('@') and word!='RT'])
    wordcloud=WordCloud(stopwords=STOPWORDS,background_color='white',height=640,width=800).generate(processed_words)
    plt.imshow(wordcloud)
    plt.xticks([])
    plt.yticks([])
    st.pyplot()
    



