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
db_movies = db.movies
db_users = db.users
db_ratings = db.ratings

# count = db.rows.count_documents({})

# db_test.insert_one({'i': "kjdsfsdfjsdlkfn"})
# movies = pd.read_csv('movies.dat', sep='::', names=['movie_id','movie_name','movie_tags'])
# links = pd.read_csv('links.csv', sep=',',dtype=str)
# links.columns = ["movie_id","imdbId","tmdbId"]
# links.movie_id.apply(int)

# links["movie_id"] = links["movie_id"].astype(int)
# users = pd.read_csv('users.dat', sep='::', names=['user_id','gender','age','occupation','zip_code'])
# ratings = pd.read_csv('ratings.dat', sep='::', names=['user_id','movie_id','rating','timestamp'])


# n = 3892
# keys = ["7db8c464","7db8c464","856db772","25550120"]

# keys = ["4b7932ba","ca9c5b","f8a0ad6e","7b7f806c"]

# keys = ["3635a730","ca9c5b","f8a0ad6e","7b7f806c"]

# def get_data(key,movie):


#     URL = "http://www.omdbapi.com/"

#     PARAMS = {'i':movie,'apikey':key} 
  
#     r = requests.get(url = URL, params = PARAMS) 
#     data = r.json() 
#     return data


# result  = pd.merge(movies, links, on='movie_id')


# for index, row in result.iterrows():

#     if index > -1 :    
#         movie = row['movie_name'][:-6].strip()
#         year = row['movie_name'][-5:-1]
#         tags = row['movie_tags'].split("|")

#         data = get_data(keys[int(index/(n/4))],"tt"+row['imdbId'])
#         # data = {}

#         tt = {"movie_id":row['movie_id'],"imdbId":row['imdbId'],"movie_name": movie, "year":year,"tags":tags, "data": data}
#         if not (db_movies.update(tt, tt,  upsert = True)['updatedExisting']):
#             print(index,"insert || ",tt['movie_name'],'||' ,row['movie_name'])
#         else:
#             print(index,"update || ",tt['movie_name'])

dijob =   {0:  "other" ,
	  1:  "academic/educator",
	  2:  "artist",
	  3:  "clerical/admin",
	  4:  "college/grad student",
	  5:  "customer service",
	  6:  "doctor/health care",
	  7:  "executive/managerial",
	  8:  "farmer",
	  9:  "homemaker",
	 10:  "K-12 student",
	 11:  "lawyer",
	 12:  "programmer",
	 13:  "retired",
	 14:  "sales/marketing",
	 15:  "scientist",
	 16:  "self-employed",
	 17:  "technician/engineer",
	 18:  "tradesman/craftsman",
	 19:  "unemployed",
	 20:  "writer"}


for doc in db_users.find():
    myquery = doc
    newvalues = { "$set": { "work": dijob[doc["occupation"]] } }

    print(db_users.update_one(myquery, newvalues))
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
