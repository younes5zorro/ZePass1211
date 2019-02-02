from pymongo import MongoClient
# from pymongo import InsertOne
import datetime
import json 
import pandas as pd
import requests 
import pymongo

from mongoengine.connection import connect

# import motor.motor_tornado as mt
# Client = MongoClient("mongodb://admin:admin123@ds213715.mlab.com:13715/movapp",connect=False, serverSelectionTimeoutMS=30000)
# Client = MongoClient("mongodb://anas:anas123@ds247171.mlab.com:47171/qstapp" , connectTimeoutMS = 30000)
Client = MongoClient("mongodb+srv://admin:admin@recommenderdb-68jw8.mongodb.net/recommenderdb?retryWrites=true&ssl=true&ssl_cert_reqs=CERT_NONE",connect=False)


# Client = MongoClient("mongodb://admin:Mohammed.021995@SG-RecSys-18047.servers.mongodirector.com:47456,SG-RecSys-18048.servers.mongodirector.com:47456,SG-RecSys-18049.servers.mongodirector.com:47456/admin?replicaSet=RS-RecSys-0&ssl=true")
# Client =MongoClient("mongodb://admin:bigdata5@ds247171.mlab.com:47171/qstapp")
# db = Client.get_database('movie_rec')

# db = Client['qstapp']

# db = Client.get_database('movapp')
db = Client['app_db']
db_test = db.test
# count = db.rows.count_documents({})

db.test.insert_one({'i': "kjdsfsdfjsdlkfn"})
# print(count)
# print(db_movies.insert_one({'imd':"jhsdbfhbhdsf"}))
# db_movies.update({'imd':"jhsdbfhbhdsf"}, {'imd':"jhsdbfhbhdsf"},  upsert = True)
# movies = pd.read_csv('movies.dat', sep='::', names=['movie_id','movie_name','movie_tags'])
# # users = pd.read_csv('users.dat', sep='::', names=['user_id','gender','age','occupation','zip_code'])
# # ratings = pd.read_csv('ratings.dat', sep='::', names=['user_id','movie_id','rating','timestamp'])

# def get_data(movie,year):


#     URL = "http://www.omdbapi.com/"

#     PARAMS = {'t':movie,'y':year,'apikey':'7db8c464'} 
  
#     r = requests.get(url = URL, params = PARAMS) 
#     data = r.json() 
#     return data

# for index, row in movies.iterrows():
#     # if index < 2:
        
#     movie = row['movie_name'][:-6].strip()
#     year = row['movie_name'][-5:-1]
#     tags = row['movie_name'].split("|")
#     data = get_data(movie,year)

#     tt = {"movie_id":row['movie_id'],"movie_name": movie, "year":year,"tags":tags, "data": data}
#     if not (db_movies.update(tt, tt,  upsert = True)['updatedExisting']):
#         print("insert || ",tt['movie_name'])
#     else:
#         print("update || ",tt['movie_name'])


# # print(movies.head())
# # print("start")
# # client_db.movies.insert(json.loads(movies.T.to_json()).values())
# # print("movies done")
# # client_db.users.insert(json.loads(users.T.to_json()).values())
# # print("users done")
# # client_db.ratings.insert(json.loads(ratings.T.to_json()).values())
# # print("ratings done")


# # cursor_excess_new = (
# #     crows.find()  
# #       .sort([("_id", 1)])
# # )

# # queries = [InsertOne(doc) for doc in cursor_excess_new]
# # srows.bulk_write(queries)
