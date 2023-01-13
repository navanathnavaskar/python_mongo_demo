from pymongo import MongoClient

class Mongo:
    
    def __init__(self, dbname, collectionname):
        self.dbname = dbname
        self.collectionname = collectionname
        
        # Create client
        client = MongoClient('localhost', 27017)

        # Get DB instance
        db = client[self.dbname]
        
        # Get collection
        self.coll = db[self.collectionname]
        
    def mongo_insert_one(self, data):
        try:
            res = self.coll.insert_one(data)
            print("Inserted One Record with id = " + str(res.inserted_id))
        except Exception as e:
            print("An Error occurred wile inserting doc : " + e)
            
    def mongo_insert_many(self, data):
        try:
            res = self.coll.insert_many(data)
            print("Inserted multiple records with IDs : " + str(res.inserted_ids))
        except Exception as e:
            print("An error occurred while inserting multiple docs : "+ e)
            
    def mongo_get_one(self, datafilter):
        data = self.coll.find_one(datafilter) 
        if data != None:
            print(data)
        else:
            print("No record found for given filter")

    def mongo_get_all(self):
        for x in self.coll.find():
            print(x)
        
    def mongo_delete(self, data):
        x = self.coll.delete_one(data)
        if x :
            print("Successfully deleted " + str(x.deleted_count) + " records.")
        else:
            print("No Record found for delete.")

    def mongo_update(self, datafilter, dataupdate):
        x = self.coll.update_one(datafilter, dataupdate)
        print("Found and Updated " + str(x.matched_count) + " records.")