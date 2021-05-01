#Python object key unique key value ko access karne ka program likho

import simplejson as json

x='{"a": 1,"a":2,"a":3,"a":4,"b":1,"b":2}'
print("original python object:-")
print(x)

y=json.loads(x)
print("unique key are:-")
print(y)