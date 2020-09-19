import http.client
import json

conn = http.client.HTTPSConnection("api.sendgrid.com")

payload = "{}"

headers = { 'authorization': "Bearer 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" }

conn.request("GET", "/v3/marketing/contacts/count", payload, headers)

res = conn.getresponse()
data = (res.read()).decode("utf-8")
dict_data = dict(json.loads(data))

contacts = 100 - int(dict_data["contact_count"])
# print(contacts)