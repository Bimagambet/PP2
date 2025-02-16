import json

x = '{ "name":"Sultan", "country":"Germany"}'

y = json.loads(x)

print(y["country"])