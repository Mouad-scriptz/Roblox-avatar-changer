import json
try:
    import requests
except:
    import os
    os.system("pip install requests")
    input("Please restart the program.")
    exit()
cookie = ""
with open("cookie.txt", "r") as file: # Getting the cookie from cookie.txt
    cookie = file.read()
    file.close()
payload = {
  "assets": [  
    { #Tshirt example ⬇
      "id": 1028595,
      "name": "Bloxxer",
      "type": "Asset",
      "assetType": {
        "id": 2, #For type ids goto: https://roblox.fandom.com/wiki/Asset_types
        "name": "TShirt"
      },
      "thumbnail": {
        "Final": False,
        "Url": ""
      },
      "thumbnailType": "Asset",
      "link": "https://www.roblox.com/catalog/1028595/Bloxxer",
      "selected": True
    },
    { #Face example ⬇
      "id": 144075659,
      "name": "Smile",
      "assetType": {
        "id": 18, #For type ids goto: https://roblox.fandom.com/wiki/Asset_types
        "name": "Face"
      },
    },
    { #Shirt example ⬇
      "id": 144076358,
      "name": "Blue and Black Motorcycle Shirt",
      "assetType": {
        "id": 11, #For type ids goto: https://roblox.fandom.com/wiki/Asset_types
        "name": "Shirt"
      },
    },
    { #Pants example ⬇
      "id": 144076760,
      "name": "Dark Green Jeans",
      "assetType": {
        "id": 12, #For type ids goto: https://roblox.fandom.com/wiki/Asset_types
        "name": "Pants"
      },
    },
    { #Hair example ⬇
      "id": 376524487,
      "name": "Blonde Spiked Hair",
      "assetType": {
        "id": 41, #For type ids goto: https://roblox.fandom.com/wiki/Asset_types
        "name": "HairAccessory"
      },
    }
  ]
}
def get_token(): #For getting x-csrf-token token
    token = requests.post("https://auth.roblox.com/v2/logout", cookies={".ROBLOSECURITY": cookie}).headers["x-csrf-token"]
    return token
headers = { #Headers the request will use to get authorized
    "accept": "application/json",
    "content-type": "application/json",
    "cookie": f".ROBLOSECURITY={cookie}",
    "x-csrf-token": get_token()
}
req = requests.post("https://avatar.roblox.com/v2/avatar/set-wearing-assets", headers=headers, data=json.dumps(payload)) # sending the request

if json.loads(req.content)["success"] == "true" and req.status_code == 200 or 201: #Checking if request is successful
    if len(json.loads(req.content)["invalidAssets"]) != 0:
        invalid_assets = json.loads(req.content)["invalidAssets"] 
    else:
        invalid_assets = "None"
    if len(json.loads(req.content)["invalidAssetIds"]) != 0:
        invalid_ids = json.loads(req.content)["invalidAssetIds"]
    else:
        invalid_ids = "None"
    print(f"Success! \nInvalid Assets: {invalid_assets}\nInvalid Asset Ids: {invalid_assets}") #Prints out Success if succeed and invalid assets/ids
else:
    print(f"Failed! \nReason: {req.content}") #Prints out failed :< (report reason by opening an issue)
