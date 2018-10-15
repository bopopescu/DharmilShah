import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["jbsl"]
print(myclient.list_database_names())

mycol = mydb["limitdb"]
collist = mydb.list_collection_names()

print(collist)
if "limitdb" in collist:
    print("collection exist")


for result in mycol.find({}, {"_id" : 0}):
    print(result)

# data = [
#     {"_id": 1, "name": "abc", "state": "Gujarat"},
#     {"_id": 2, "name": "xyz", "state": "maharashtra"},
#     {"_id": 3, "name": "jkl", "state": "karnataka"},
#     {"_id": 4, "name": "qwerty", "state": "delhi"},
#     {"_id": 5, "name": "qaz", "state": "punjab"}
# ]
#
# x = mycol.insert_many(data)
# print(x.inserted_ids)

for result in mycol.find({}, {"_id" : 0}):
    print(result)

print('')
print('use of limit function')

result = mycol.find().limit(3)
for x in result:
    print(x)
