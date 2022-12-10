import json
import requests
from datetime import datetime, timedelta

allPrice = []
dayPrice = []


url = "https://api-mobile.airfranceklm.com/mobile/offers/v2/lowest-fare-offers"
token = "Bearer kh6f3zbxp8q8ab58a3vk5d4e"
headers = {"Content-Type": "application/json", 'User-Agent': 'AF-STR/13.1.1 (com.airfrance.mobile.iphone.afmobile; build:2022.07.20.57; iOS 15.6.0) Alamofire/5.6.2',"AFKL-TRAVEL-Host": 'AF', "Authorization": token}
for i in range(1):
    goDate = str((datetime.today() + timedelta(days=i)).date())
    backDate = str((datetime.today() + timedelta(days=(i+1))).date())

    with open("AirFrance/AF_lowestOffer.json", "r+") as jsonFile:
        data = json.load(jsonFile)
        # data["requestedConnections"][0]["departureDate"] = goDate
        # data["endDate"] = checkout
        jsonFile.seek(0)
        json.dump(data, jsonFile)
        jsonFile.truncate()
        jsonFile.close()
    body = open('AirFrance/AF_lowestOffer.json')
    body = body.read()
    try:
        resp = requests.post(url, headers=headers, data=body, timeout=3)
        response = json.loads(resp.text)
        # for flight in response['itineraries']:
        #     dayPrice.append()
    except:
        print("Error!")
    # print(resp.status_code)
    # response = json.loads(resp.text)
    # print(response)

