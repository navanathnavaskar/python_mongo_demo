############################################################
# This program is used to perform Mongodb oprations 
# using pymongo. 
# Requirements: 
#     1. MongoDB is installed and running on 27017 port
#     2. Python 3.7 and above
############################################################

from db.mongo import Mongo

dbobject = Mongo('testdb', 'users')

marklist = []

m1 = {
    "marathi":44,
    "hindi":55,
    "english":33
}
marklist.append(m1)

m1 = {
    "marathi":88,
    "hindi":77,
    "english":66
}
marklist.append(m1)

doc1 = {
    "name": "Navanath",
    "age": 26,
    "city": "Pune",
    "marks": marklist
}

dbobject.mongo_insert_one(doc1)

doc1 = {
    "name": "Rohan",
    "age": 25,
    "city": "Pune",
    "marks": marklist
}
doc2 = {
    "name": "Roshan",
    "age": 27,
    "city": "Pune",
    "marks": marklist
}
doc3 = {
    "name": "Prashant",
    "age": 24,
    "city": "Mumbai",
    "marks": marklist
}
data = [doc1, doc2, doc3]
dbobject.mongo_insert_many(data)

fil = {
    "name" : "Navanath"
}

print("Get one record using filter : ")
dbobject.mongo_get_one(fil)
print("Get all records : ")
dbobject.mongo_get_all()
print("Delete record using filter : ")
dbobject.mongo_delete(fil)
dupdate = {
    "$set": {
        "city":"Pune"
    }
}
fil1 = {
    "name" : "Rohan"
}
print("Update records : ")
dbobject.mongo_update(fil1, dupdate)
print("Get all records : ")
dbobject.mongo_get_all()
