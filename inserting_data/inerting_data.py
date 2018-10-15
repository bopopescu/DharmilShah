print('Inserting the data to the collection ')
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]

mycol = mydb["customers"]

mydata = {"name" : "abc", "state" : "gujarat"}

x = mycol.insert_one(mydata)

print(x.inserted_id)

# inserting multiple data to the collection customers

mylist = [
    {"name" :" abc", "roll no" : "27"},
    {"name" : "xyz", "roll no" : "2"},
    {"name" : "jkl", "roll no" : "7"}

]
x1 = mycol.insert_many(mylist)

print(x.inserted_id)




