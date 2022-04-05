import pymongo
client = pymongo.MongoClient("mongodb+srv://sap:sap@cluster1.ugtiu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
dataBase = client["Food"]