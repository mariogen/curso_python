from bson.objectid import ObjectId
from pymongo import MongoClient
import datetime
from pprint import pprint

client = MongoClient('mongodb://localhost:27017/')

client.drop_database('test_database')

db = client.test_database

posts = db.posts

post = {"author": "Mike",
        "text": "My first blog post!",
         "tags": ["mongodb", "python", "pymongo"],
         "date": datetime.datetime.utcnow()}

post_id = posts.insert_one(post).inserted_id
print(post_id)

print(db.list_collection_names())

pprint(posts.find_one({'author':'Mike'}))

print(post_id == ObjectId(str(post_id)))

new_posts = [{"author": "Mike",
              "text": "Another post!",
              "tags": ["bulk", "insert"],
              "date": datetime.datetime(2009, 11, 12, 11, 14)},
             {"author": "Eliot",
              "title": "MongoDB is fun",
              "text": "and pretty easy too!",
              "date": datetime.datetime(2009, 11, 10, 10, 45)}]
result = posts.insert_many(new_posts)
print(result.inserted_ids)

for post in posts.find({"author": "Mike"}):
    pprint(post)
    print()

print('document count',posts.count_documents({}))

d = datetime.datetime(2009, 11, 12, 12)
for post in posts.find({"date": {"$lt": d}}).sort("author"):
    pprint(post)







