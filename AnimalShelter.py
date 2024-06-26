from pymongo import MongoClient
from bson.objectid import ObjectId
import pprint

class Animal:
    
    #Initialize class object
    def __init__(self, username, password):
        USER = username
        PASS = password
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 32232
        DB = 'AAC'
        COL = 'animals'
        
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER, PASS, HOST, PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        
    #Function to create a new document under the class object
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)
        else:
            raise Exception("Nothing to save, data parameter is empty")
    
    #Function to find and print every document in the database according to query parameters
    def read(self, pJson):
        animalList = []
        for animal in self.database.animals.find():
            animalList.append(animal)
        return animalList    
    
    #Function to find and update every document in the database according to query parameters
    def update(self, keyToFind, dataToFind, keyToSet, dataToSet):
        resultChanged = self.database.animals.update_many({keyToFind: dataToFind}, {"$set": {keyToSet: dataToSet}})
        print(resultChanged.matched_count)
        print(resultChanged.modified_count)
    
    #Function to find and delete every document in the database according to query parameters
    def delete(self, keyToDelete, valueToDelete):
        resultDeleted = self.database.animals.delete_many({keyToDelete: valueToDelete})
        print(resultDeleted.deleted_count)