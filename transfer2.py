from pymongo import MongoClient
# from pymongo import InsertOne
import datetime
import json 
import pandas as pd
import requests 
import pymongo


# import motor.motor_tornado as mt
# Client = MongoClient("mongodb://admin:admin123@ds213715.mlab.com:13715/movapp",connect=False, serverSelectionTimeoutMS=30000)
# Client = MongoClient("mongodb://anas:anas123@ds247171.mlab.com:47171/qstapp" , connectTimeoutMS = 30000)
Client = MongoClient()


# Client = MongoClient("mongodb://admin:Mohammed.021995@SG-RecSys-18047.servers.mongodirector.com:47456,SG-RecSys-18048.servers.mongodirector.com:47456,SG-RecSys-18049.servers.mongodirector.com:47456/admin?replicaSet=RS-RecSys-0&ssl=true")
# Client =MongoClient("mongodb://admin:bigdata5@ds247171.mlab.com:47171/qstapp")
# db = Client.get_database('movie_rec')

# db = Client['qstapp']

db = Client.get_database('app_db')
# db_movies = db.movies
# db_users = db.users
# db_ratings = db.ratings
db_ratusers = db.ratusers

# count = db.rows.count_documents({})

# db_test.insert_one({'i': "kjdsfsdfjsdlkfn"})
movies = pd.read_csv('movies.dat', sep='::', names=['movie_id','movie_name','movie_tags'])
users = pd.read_csv('users.dat', sep='::', names=['user_id','gender','age','occupation','zip_code'])
df = pd.read_csv('ratings.dat', sep='::', names=['user_id','movie_id','rating','timestamp'])

doc = {}

# for id,lst in df.groupby('user_id')['movie_id'].apply(list):
    # print(id,lst)

# print(df.groupby('user_id')['movie_id'].apply(list)[])

user_list =  users.user_id.unique()
movie_list =  movies.movie_id.unique()


for row in user_list:
    
    rating_list = df.groupby('user_id')['movie_id'].apply(list)[int(row)]

    notrat_list = [ int(t) for t in movie_list if t not in rating_list ]


    # tt = {"user_id":int(row),"notrat_list":notrat_list[:50],"rating_list":rating_list}
    tt = {"user_id" : int(row),"rating_list" : rating_list,"not_rating" :notrat_list }
    # db_ratusers.insert_one(tt)
    print(row,(db_ratusers.insert_one(tt)).inserted_id)
    # if not (db.ratusers.update(tt, tt,  upsert = True)['updatedExisting']):
    #     print(row, " || insert || ",tt['user_id'])
    # else:
    #     print(row," || update || ",tt['user_id'])

    # break
# myresults = list(mydb.mycollection.find())
# print(ratings.head())

# for index, row in users.iterrows():
    
#     tt = {"user_id":int(row['user_id']),"movie_id":int(row['movie_id']),"rating":int(row['rating']),"timestamp":int(row['timestamp'])}
#     if not (db_ratings.update(tt, tt,  upsert = True)['updatedExisting']):
#         print(index, " || insert || ",tt['user_id'])
#     else:
#         print(index," || update || ",tt['user_id'])

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
