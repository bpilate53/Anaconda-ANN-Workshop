#Code adapted from University of South Alabama course ISC  629 course: Python Flask Workshop 
#https://github.com/mahesh6420/flask-lab
import pymongo

class Database:

    def get_database(self):
        db_client = pymongo.MongoClient('localhost', 27017)
       
        #db_client = pymongo.MongoClient("mongodb+srv://admin:8SLKvfeaChjpi9Zy@cluster0.tz99yuz.mongodb.net/?retryWrites=true&w=majority")
        
        prediction_db = db_client.prediction_db

        return prediction_db