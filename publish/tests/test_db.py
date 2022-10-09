from utils import get_client
from django.http import HttpResponse
# from publish.views import ridesDB
from pymongo import MongoClient
from django.test import SimpleTestCase

client = MongoClient("mongodb+srv://Aoishi:helloAOISHI2805@cluster0.zpuftvw.mongodb.net/?retryWrites=true&w=majority")
db = client.SEProject
ridesDB  = db.rides
class Testdb(SimpleTestCase):
    global id

    def test_insert_db(self):

        data =  {
                  'name':"CSC510-wed",
                  'destination':"James Hunt Library",
                  'date': "2022-10-10",
                  'hour':"10",
                  'minute':"00",
                  'ampm':"AM",
                  'details': "Ride to attend Monday CSC510 Lecture on 10/10/2022 at 10:15 AM."}

        id = ridesDB.insert_one(data).inserted_id
        self.assertEqual(ridesDB.insert_one(data), True)

        result = ridesDB.find_one({'_id': id})
        print("res is", result)
        self.assertEqual(result['_id'], id)

        ridesDB.delete_one({'_id': id})




    # def test_find_db(self):
    #     # id = self.test_insert_db()
    #     result= ridesDB.find_one({'_id':id})
    #     print("res is",result)
    #     self.assertEqual(result['_id'], id)
    #
    # def test_delete_db(self):
    #     # id = self.test_insert_db()
    #     ridesDB.delete_one({'_id':id})







