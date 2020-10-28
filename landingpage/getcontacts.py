# import http.client
import json

# conn = http.client.HTTPSConnection("api.sendgrid.com")

# payload = "{}"

# headers = { 'authorization': "Bearer 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" }

# conn.request("GET", "/v3/marketing/contacts/count", payload, headers)

# res = conn.getresponse()
# data = (res.read()).decode("utf-8")
# dict_data = dict(json.loads(data))

# contacts = 69 - int(dict_data["contact_count"])

import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError

# try:
client = MailchimpMarketing.Client()
client.set_config({
    "api_key": "98c739edddb5f125479032c9da209c76",
    "server": "us17"
})

response = client.lists.get_list("d48294805c")

contacts = 69 - response["stats"]["member_count"]
print(contacts)
# except ApiClientError as error:
#   print("")
