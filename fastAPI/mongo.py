import pymongo

def listDbColl(client):
    allDatabases = client.list_database_names()
    collection = client['sampleApiCollection']
    allCollections  = collection.list_collection_names()
    print(allDatabases)
    print(allCollections)

def connectDB():
    client = pymongo.MongoClient('mongodb://localhost:27017')
    return client

def createCollection(client, DBname, collectionName):
    db = client[DBname]
    collection = db[collectionName]
    return collection

def Insert(collection, document):
    if type(document) == list:
        collection.insert_many(document)
    elif type(document) == dict:
        collection.insert_one(document)
    else:
        pass


if __name__ == '__main__':
    client = connectDB()
    
    # Creating the DB, client, document
    collection = createCollection(client, 'APIdb', 'sampleApiCollection')

    # Inserting Data
    document1 = {
        "name": "Bitan",
        "age": 24
    }
    docList = [
        {"name": "Subho", "location": "Jharkhand", "age": 21},
        {"name": "Arijit", "location": "Sodepur", "age": 30},
        {"name": "Arjun", "location": "Jammu", "age": 22},
        {"name": "Yash", "location": "Pune", "age": 23}
    ]

    Insert(collection, document1)
    Insert(collection, docList)
    

    print(collection.find_one())
    print(collection.find_one({"name": "Yash"}))
    print(collection.find({"name": "Yash"}, {"_id": 0, "name": 1, "locaton": 1})) # Only show name and location column


    where = {"name": "Yash"}
    newVal  = {"$set": {"location": "Kochi"}}
    collection.update_one(where, newVal) # Updates only 1 record which matches the condition
    collection.update_many(where, newVal) # Updates all the records that satisfy the condition
    

    where = {"name": "Arjun"}
    collection.delete_one(where)
    collection.delete_many(where)