from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
people_collection = db['people']

# Insert a person document with an embedded passport document
person = {
    "name": "John Doe",
    "age": 30,
    "passport": {
        "passport_number": "123456789",
        "issued_country": "USA",
        "expiration_date": "2030-01-01"
    }
}

people_collection.insert_one(person)

# Query the person along with their passport
person_data = people_collection.find_one({"name": "John Doe"})
print(person_data)
