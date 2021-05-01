import simplejson as json

with open("name.json","r") as f:
    data=json.load(f)

print(data)

