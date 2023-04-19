# Analyzing the University of Michigan Subreddit

## Sentiment Analysis

Within the sentiment analysis folder, you will find scripts to predict the sentiments of posts. We use a pre-trained hugging face model, which we validated on your labeled dataset. We currently achieve an accuracy of 70%. sentiment_analysis.py is a file containing a class which is used to conduct the sentiment analysis.

## Entity Extraction

Within the Entity_Extraction folder, you will find scripts to extract entities from a given post. We use regular expressions to extract the entities, and have found that this works better than other bruteforce algorithms, as well as pre-trained entity extractors. We currently achieve an accuracy of 87%. entity_extraction.py is a file containg a class which is used to conduct the entity extraction.

In addition, we have several scripts to run our tool on larger coruses of data, and plot the result over time.

## Data Collection

Within the Data_Collection folder, you will find the notebook to organize scraped Reddit data (which was initially in a database file) into formats suitable for our project.

> **Note**
> Our labeled data is not on the github, but rather in our private google drive. It contained 450 posts labeled for sentiment analysis and entity extraction.

