#Python object ko json string mai convert karne ka program likho
import simplejson as json
x={
    'name': 'David',
     'class':'I',
     'age': 6  
 }


with open("json_string.json","w") as f:
    json.dump(x,f)
# f.close()
