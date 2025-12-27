import json
# This is JSON
userJSON = '{"first_name": "John", "last_name":"Doe", "age":30}'

# JSON to dict
user = json.loads(userJSON)
print(user)

# This is dictionary
carDict = {
    'make': 'Ford', 'model':'Mustang', 'year':1970
}

# Dict to JSON
car = json.dumps(carDict)
print(car)