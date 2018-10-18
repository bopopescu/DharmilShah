import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["jbsl"]
print(myclient.list_database_names())

mycol = mydb["sortdata"]
collist = mydb.list_collection_names()

print(collist)
if "sortdata" in collist:
    print("collection exist")

# data = [
#     {"_id": 1, "name": "dha", "mno": "78952"},
#     {"_id": 2, "name": "da", "mno": "7892"},
#     {"_id": 3, "name": "asda", "mno": "78952123"},
# ]
#
# x = mycol.insert_many(data)
# print(x.inserted_ids)

for result in mycol.find({}, {"_id" : 0}):
    print(result)

myquery2 = {"name": {"$lt": "d"}}
mydoc2 = mycol.find(myquery2)
for x in mydoc2:
    print(x)

print('--------------------------------')
mydoc = mycol.find().sort("id")
for x in mydoc:
    print(x)

