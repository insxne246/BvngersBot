import requests
import json

url = ""

data = {}

data["content"] = ""
data["username"] = "BVNGERS BOT"

#leave this out if you dont want an embed
data["embeds"] = []
embed = {}

embed["description"] = "text in embed"
embed["title"] = "embed title"
data["embeds"].append(embed)

result = requests.post(url, data=json.dumps(data), headers={"Content-Type": "application/json"})

try:
    result.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(err)
else:
    print("Payload delivered successfully, code {}.".format(result.status_code))
