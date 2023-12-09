from flask import Flask, render_template, jsonify,request
import pandas as pd

app = Flask(__name__)

liked = []
unliked = []
popular = []

articles = pd.read_csv("C:/Users/subra/PycharmProjects/pythonProject/app/project141/articles.csv")
articles_details = articles[['title','url','text','lang','total_events']]
print(articles.columns)
# @app.route("/")

def default():
    global articles_details
    data = {"title":articles_details.iloc[0,0],"url":articles_details.iloc[0,1],"text":articles_details.iloc[0,2],"lang":articles_details.iloc[0,3],"total_events":str(articles_details.iloc[0,4])}
    return data

@app.route("/get-article")
def get_articles():
    global articles, articles_details
    dt = default()
    print(dt)
    return jsonify({"article":dt,"success":"success"})

@app.route("/liked-article")
def liked_articles():
    global articles_details
    dtl = default()
    liked.append(dtl)
    articles_details.drop([0],inplace=True)
    articles_details = articles_details.reset_index(drop = True)
    return jsonify({"success":"success"})

@app.route("/unliked-article")
def unliked_articles():
    global articles_details
    dtul = default()
    unliked.append(dtul)
    articles_details.drop([0],inplace=True)
    articles_details = articles_details.reset_index(drop = True)
    return jsonify({"success":"success"})

@app.route("/liked")
def diplay_like():
    global liked
    return jsonify({"data":liked})

@app.route("/unliked")
def diplay_unlike():
    global unliked
    return jsonify({"data":unliked})

@app.route("/popular-articles")
def popular_articles():
    return "#"

@app.route("/recommended-articles")
def populares():
    return "$"

app.run()