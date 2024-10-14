import json
import urllib.request

address=input('enter location:')
if (len(address)<1):
    address='https://py4e-data.dr-chuck.net/comments_2084048.json'

print('retrieveing', address)
index=0
sum=0
dat=urllib.request.urlopen(address)
data=dat.read().decode()
info = json.loads(data)
print('User count:', len(info))
try:
    js=json.loads(data)
except:
    js=None
print(json.dumps(js['comments'][1]['count'], indent=4))
counts_data=js['comments']
for datos in counts_data:  
    sum=sum+int(counts_data[index]['count'])
    index=index+1
    print (sum)

