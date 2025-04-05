from pymongo import MongoClient

# Step 1: Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['mycollection']

# Step 2: Insert data
collection.insert_one({"name": "John", "age": 30, "city": "New York"})
collection.insert_many([
    {"name": "Alice", "age": 28, "city": "Los Angeles"},
    {"name": "Bob", "age": 35, "city": "Chicago"}
])

# Step 3: Query data
person = collection.find_one({"name": "John"})
print(person)

people_in_ny = collection.find({"city": "New York"})
for person in people_in_ny:
    print(person)

# Step 4: Update data
collection.update_one({"name": "John"}, {"$set": {"age": 31}})

# Step 5: Delete data
collection.delete_one({"name": "Bob"})

# Step 6: Close connection
client.close()
