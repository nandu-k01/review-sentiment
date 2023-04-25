import streamlit as st
import nltk
from transform import transform_lem
from nltk.sentiment import SentimentIntensityAnalyzer
import re


nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()



st.title("Amazon Review's Sentiment")
# st.subheader('Enter the URL')
st.subheader('Enter the review')
title = st.text_input(label='Input')

if st.button("Predict"):
    if re.match("^[0-9\W]+$", title): # checking if the user input is valid 
        st.subheader("Enter Valid review")
    else:     
        title_transformed = transform_lem(title)     # removing special characters, stopwords, and lemmatizing
        # st.subheader(title_transformed)
        sentiment = sia.polarity_scores(title_transformed)  # finding the polarity score of the processed text
        # st.subheader(sentiment)
        if sentiment['compound'] > 0.200: # if the compund polarity score is greater than 0.200 then positive
            st.subheader("Looks Good")
        elif sentiment['compound'] >= -0.200 and sentiment['compound'] <= 0.200: # polarity score between -0.200 and 0.200 then neutral
            st.subheader("Not great or bad, Neutral review")
        else:                                    # less than -0.200 the review is negative
            st.subheader("Stay away from this product") 




