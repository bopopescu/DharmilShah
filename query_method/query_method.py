import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["jbsl"]
print(myclient.list_database_names())

mycol = mydb["order"]
collist = mydb.list_collection_names()
print(collist)

if "order" in collist:
    print("the collection exist")

data = [
    {"_id": 0, "name": "abc", "product":"deo", "order":2},
    {"_id": 1, "name": "xyz", "product": "bat", "order": 12},
    {"_id": 2, "name": "jkl", "product": "tennis", "order": 232},
    {"_id": 3 , "name": "qwerty", "product":"trouser", "order":23},
    {"_id": 4, "name": "lkjhf", "product": "shirt", "order": 42},

]
x = mycol.insert_many(data)
print(x.inserted_ids)

for x in mycol.find({},{"_id":0}):
    print(x)

print('')
print('to find particular product')
myquery = {"product": "trouser"}
mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)

print('--------------------')
print('to find similar or greater then particular number ')
myquery1 = {"product": {"$regex" : "^t"}}
mydoc1 = mycol.find(myquery1)
for x in mydoc1:
    print(x)

print('--------------------')
print('ro find the lower number value use this ')
myquery2 = {"product": {"$lt": "t"}}
mydoc2 = mycol.find(myquery2)
for x in mydoc2:
    print(x)























