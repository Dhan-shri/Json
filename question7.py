#Text file data ko json file data mai convert karo,jaise ki neeche diya hai

import simplejson as json

filename='question7.txt'
d={ }
with open(filename) as f:
    for line in f:
        k,l = line.strip().split(None, 1) 
        d[k]=l.strip()
print(d)

with open("textfile.json","w") as f:
    json.dump(d,f,indent=4)
f.close()


# import simplejson as json

# filename='question7.txt'
# d={ }
# with open(filename) as f:
#     for line in f:
#         k,l = line.strip().split(None, 1) 
#         d[k]=l.strip()
# print(d)

# with open("textfile.json","w") as f:
#     json.dump(d,f,indent=4,sort_keys=True)
# f.close()


