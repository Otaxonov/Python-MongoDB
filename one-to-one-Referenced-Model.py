from pymongo import MongoClient
from bson.objectid import ObjectId

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
people_collection = db['people']
passports_collection = db['passports']

# Insert passport document
passport = {
    "passport_number": "987654321",
    "issued_country": "USA",
    "expiration_date": "2035-05-15"
}
passport_id = passports_collection.insert_one(passport).inserted_id

# Insert person document with reference to the passport
person = {
    "name": "Jane Doe",
    "age": 28,
    "passport_id": passport_id  # Reference to the passport document
}
people_collection.insert_one(person)

# Query the person along with their passport
person_data = people_collection.find_one({"name": "Jane Doe"})
passport_data = passports_collection.find_one({"_id": person_data["passport_id"]})

print("Person:", person_data)
print("Passport:", passport_data)
