import json
import requests as req
from pymongo import MongoClient

raw_data = req.get('http://api.weatherstack.com/current?access_key=3ca37dd38e17caf9ce73135525b9b62c&query=New%20York')
data = raw_data.text
json_data = json.loads(data)

print(json_data['request'])

client = MongoClient("mongodb://127.0.0.1:27017")
print("Connection Successful")
client.close()