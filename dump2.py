#to convert python object to json file
import json

x = {"name": "David",
     "class":"I",
     "age": 6 }
with open("dhanshri.json","w") as f:
    json.dump(x,f,indent=4)
f.close()



