import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["jbsl"]
print(myclient.list_database_names())

mycol = mydb["update_database"]
collist = mydb.list_collection_names()

print(collist)
if "update_database" in collist:
    print("collection exist")


for result in mycol.find({}, {"_id" : 0}):
    print(result)

data = [
    {"_id": 1, "name": "abc", "state": "Gujarat"},
    {"_id": 2, "name": "xyz", "state": "maharashtra"},
    {"_id": 3, "name": "jkl", "state": "karnataka"},
    {"_id": 4, "name": "qwerty", "state": "delhi"},


]

x = mycol.insert_many(data)
print(x.inserted_ids)

for result in mycol.find({}, {"_id" : 0}):
    print(result)


myquery = {"name": "xyz", "state": "maharashtra"}
newvalue = {"$set": {"name": "XYYZ", "state": "GUJARAT"}}
mycol.update_one(myquery, newvalue)
print('------------------------')
print('after updating the single value result is : ')
for updated_result in mycol.find():
    print(updated_result)

print('----------------------')
print('updating many value :')
myquery1 = {"name": {"$regex": "^A"}}
newvalue1 = {"$set":{"name": "dha"}}
x = mycol.update_many(myquery1, newvalue1)
print(x.modified_count, 'Documents Updated')

for updated_result in mycol.find():
    print(updated_result)







