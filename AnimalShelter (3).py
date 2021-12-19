
from pymongo import MongoClient
from bson.objectid import ObjectId


class AnimalShelter(object):
    #init MongoClient accepting username and password parameters & specificing db to authenticate
    def __init__(self, userName, passWord):
        
        self.client = MongoClient('mongodb://%s:%s@localhost:38048/AAC' %(userName, passWord))
        self.database = self.client['AAC']
        
    #inserts dictionary into collection, if operation returns non None then insert was successful else returns false 
    def create(self, data):
        if data is not None:
            insert = self.database.animals.insert_one(data)#data should be dictionary
            if insert is not None:
                return True
            else:
                return False
        else:
            raise Exception("Parameter Empty")
    
    #returns cursor result of matching entries or FNF if entry doesn't exist
    def read(self, data=None):
        if data is not None:
            results = self.database.animals.find(data)
            return results
        else:
            print("File not Found")
            return
    
    #updates entry with new data if entry is found, else method creates a new entry
    def update(self, data=None, newData=None):
        if data:
            results = self.database.animals.find_one(data, {"_id":False, "name":1, "type":1})
            if results is not None:
                changeData = self.database.animals.update_one(data, newData)
                print("Successfully Updated To: ")
                return newData
            else: 
                changeData = self.database.animals.insert_one(newData)
                print("Successfully Added: ")
                return changeData
        else:
            results = self.database.animals.find_one({}, {"_id":False, "name":1, "type":1})
            return False
    #method deletes entry matching criteria unless entry is not found
    def delete(self, criteria=None):
        if criteria:
            results = self.database.animals.find_one(criteria, {"_id":False, "name":1, "type":1})
            if results is not None:
                remove = self.database.animals.delete_one(criteria)
                print("File Removed")
                return 
            else:
                print("File not Found")
                return
        else:
            print("No criteria")
            return False
    
    
        
