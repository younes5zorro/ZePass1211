# import re
# import string
import random
# import datetime
# import codecs
import json
import itertools
from bson import json_util
import operator

from flask import Flask, render_template, request, jsonify , session, url_for, redirect

import pandas as pd
# import numpy as np

# from sklearn import preprocessing
# from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
# # import pickle


# from keras.models import load_model
from pymongo import MongoClient
app = Flask(__name__)

Client = MongoClient()
db = Client.get_database('app_db')
db_movies = db.movies
db_users = db.users
db_ratings = db.ratings
db_ratusers = db.ratusers

def page_acceuil():
    return render_template('home2.html')

def users(limit):
    users = db_ratusers.find({}).limit(int(limit))
    return json_util.dumps((users))

def movis_user(user):
    dic2={}

    useratings = db_ratings.find({"user_id":int(user)}).sort( [("rating", -1)]  ).limit(10)
    # users = db_ratusers.find({"user_id":int(user)})

    lisii = [u["movie_id"] for u in useratings]
    dic2 = db_movies.find( { "movie_id":{"$in" : lisii }} ).limit(10)
    return json_util.dumps((dic2))

def findbb(user,model):
    users = db_ratusers.find({"user_id":int(user)})
    dic = {}
    dic2 = {}

    if(model == "1"):
        model = "keras_network"
    elif(model == "2"):
        model = "Matrix_factorisation"
    elif(model == "3"):
       model = "NN_keras"
    elif(model == "4"):
       model = "Non-negative_Matrix_factorisation"
    else:
        return {}

    for us in users:
        for movie in us['not_rating'][:30]:
            # loaded_model = load_model("models/"+model+".h5")
            dic[movie] = random.uniform(0.1, 5.0)
            # dic[movie] = loaded_model.predict([pd.Series(int(user)),pd.Series(int(movie))])

    # predictions = predictions.argmax(axis=-1)
    # print(list(dict(sorted(dic.items(), key=operator.itemgetter(1), reverse=True)[:5]).keys()))
    best5 = list(dict(sorted(dic.items(), key=operator.itemgetter(1), reverse=True)[:10]).keys())
    dic2 = db_movies.find( { "movie_id": {"$in" : best5} } )
    return json_util.dumps((dic2))


# def Deeplearning(user,movies,model):
#     dic = {}
#     dic2 = {}
#     for movie in movies:
#         loaded_model = load_model("models/"+model+".h5")
#         dic[movie] = loaded_model.predict(([user,movie]))
#     # predictions = predictions.argmax(axis=-1)
#     newA = dict(sorted(dic.iteritems(), key=operator.itemgetter(1), reverse=True)[:5]).keys
#     return dic



def test(user):
    dic ={}
    if(id == "1"):
        value = findbb(user,"keras_network")
    elif(id == "2"):
        value = findbb(user,"Matrix_factorisation")
    elif(id == "3"):
       value = findbb(user,"NN_keras")
    elif(id == "4"):
       value = findbb(user,"Non-negative_Matrix_factorisation")
    elif(id == "0"):
        return
    else:
        value = "Parametres Error ...."
    doc = {
        "user":user,
        "movies":value,
        }
    
    return jsonify(doc)
    

# routes app
app.add_url_rule('/', 'index', page_acceuil, methods=['GET'])


app.add_url_rule('/api/get/<id>/<txt>', 'test', test, methods=['GET'])
app.add_url_rule('/api/users/<limit>', 'users', users, methods=['GET'])
app.add_url_rule('/api/movie_user/<user>', 'movis_user', movis_user, methods=['GET'])
app.add_url_rule('/api/find/<user>/<model>', 'findbb', findbb, methods=['GET'])

if __name__ == "__main__":
    app.run(debug=True)

