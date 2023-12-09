from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np
import csv

df1=pd.read_csv('shared_articles.csv')
df2=pd.read_csv('users_interactions.csv')

# printing top 5 rows for first dataframe
df1.head(1)

# printing top 5 rows for second dataframe
df2.head(1)

# information of first dataframe
df1.info()

# information of second dataframe
df2.info()

"""# Demographic Filtering"""

# printing title and event type of first 10 articles
df1[['title', 'eventType']].head(10)

# keeping rows with event type as 'CONTENT SHARED'


df3 = df1[df1["eventType"]=="CONTENT SHARED"]
print(df3)

# df4 = df1[(df2["contentId"]==df1["contentId"])]
# print(df4)

# printing shape to verify
print(df3)

# finding total events
def count_events(df):
  like =df2[(df2["contentId"]==df["contentId"]) & (df2["eventType"]=="LIKE")].shape[0]
  # print(like)
  view = df2[(df2["contentId"]==df["contentId"]) & (df2["eventType"]=="VIEW")].shape[0]
  # print(view)
  bookmark = df2[(df2["contentId"]==df["contentId"]) & (df2["eventType"]=="BOOKMARK")].shape[0]
  # print(bookmark)
  follow = df2[(df2["contentId"]==df["contentId"]) & (df2["eventType"]=="FOLLOW")].shape[0]
  # print(follow)
  return(like+view+bookmark+follow)

df1["final"] = df1.apply(count_events,axis=1)

# sort the dataframe
df1 = df1.sort_values(["final"],ascending = False)

# printing top 10 articles with title name and total events
df1[['title', 'final','contentId']].head(10)

def convert_to_lower_case(x):
  if isinstance(x,str):
    return(x.lower())
  else:
    return("")

df1["title"] = df1["title"].apply(convert_to_lower_case)



count = CountVectorizer(stop_words="english")
data = count.fit_transform(df1["title"])

similarity = cosine_similarity(data,data)

df1 = df1.reset_index()

indexing = pd.Series(df1.index,index=df1["contentId"])

def recommended(similarity,contentId):
  # count1 = CountVectorizer(stop_words="english")
  # count1.fit_transform(contentId)
  id = indexing[contentId]
  print(id)
  similarity_percentage = list(enumerate(similarity[id]))
  sorted_similarity = sorted(similarity_percentage)
  sorted_similarity = sorted_similarity[1:5]
  print(sorted_similarity)
  articles = [i[0] for i in sorted_similarity]
  print(df1["contentId"].iloc[articles])
  print(df1["title"].iloc[articles])

recommended(similarity,-4110354420726924665)

df1.to_csv("article.csv")