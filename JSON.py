import json

# data = '{"var1":"aaqil", "var2":56}'
# # print(data)
# # print(data['var1']) as this is string we cannot access as key value pair

# # The json. load() is used to read the JSON document from file and The json. loads() is used to convert the JSON String document into the Python dictionary

# parsed = json.loads(data) 

# print(parsed)
#print(type(parsed))
# print(parsed['var1'])

# # Opening JSON file
# f = open('data.json',)
   
# # returns JSON object as a dictionary
# data = json.load(f)
   
# # Iterating through the json list
# for i in data['emp_details']:
#     print(i)
   
# # Closing file
# f.close()

# data2 = {
# 	"channel_name":"Suntv",
# 	"cars":['bmw','audi','ferari'],
# 	"fridge":('roti','sabzi'),
# 	"isBad": False
# }

# jscomp = json.dumps(data2) # This converts following python dictionary to JSON compatible
# print(jscomp)

# The json.dumps() method has parameters to order the keys in the result:

# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }

# # sort the result alphabetically by keys:
# print(json.dumps(x, indent=4, sort_keys=True))
