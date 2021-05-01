#Python dictionary(sort by key) object ko json data ::mai convert karne ka program likho

import simplejson as json


x={
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4
    }

print("Original String:")
print(x)
print("\nJSON data:")
print(json.dumps(x, sort_keys=True, indent=4))

