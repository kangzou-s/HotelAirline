import fileinput
import re
import json
import datetime
import random
import requests
from datetime import datetime, timedelta
from time import sleep
from sqlalchemy.orm import Session



url = 'https://apis.ihg.com/availability/v3/hotels/offers'
content_type = 'application/json'
api_key = 'dAzcKAcBT8jGMeucgCwAjmASrQCJzeIY'
api_token = 'efbc3755-016f-456f-ac27-f24158882197'
ua_list = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .\
    NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)', ]
headers = {'Content-Type':content_type, 'X-IHG-API-KEY': api_key, 'X-IHG-MWS-API-TOKEN': api_token, 'User-Agent': 'IHGBranded-Priorityclubrewards-Universal/107.5.7.0 (iPhone; iOS 10.2; Scale/2.00)'}


for i in range(365):
    checkin = str((datetime.today() + timedelta(days=i)).date())
    checkout = str((datetime.today() + timedelta(days=(i+1))).date())

    with open("IHG.json", "r+") as jsonFile:
        data = json.load(jsonFile)
        # data["startDate"] = '2022-08-21'
        data["startDate"] = checkin
        # data["endDate"] = '2022-08-22'
        data["endDate"] = checkout
        jsonFile.seek(0)
        json.dump(data, jsonFile)
        jsonFile.truncate()
        jsonFile.close()
    body = open('IHG.json')
    body = body.read()

    resp = requests.post(url, headers=headers, data=body)
    response = json.loads(resp.text)
    hotel1 = response["hotels"][0]
    hotel2 = response["hotels"][4]
    # if hotel1['availabilityStatus'] == 'CLOSED':                    # paid night
    #     print(checkin, end="  ")
    #     print("假日："+"closed")
    # else:
    #     print(checkin, end="  ")
    #     print("假日："+str(hotel1["lowestCashOnlyCost"]) + hotel1["propertyCurrency"])
    #
    #     try:                      # Reward night
    #         print("假日：" + str(hotel1["lowestPointsOnlyCost"]["points"]) + " points")
    #     except:
    #         print("假日：" + "There is not reward night")
    hotelName = hotel2["hotelMnemonic"]
    date = checkin
    price = -1
    point = -1
    pointValue = 1
    Currency = None
    if hotel2['availabilityStatus'] == 'CLOSED':
        print(checkin, end="  ")
        print("洲际：" + "closed")
    else:
        print(checkin, end="  ")
        print("洲际"+str(hotel2["lowestCashOnlyCost"]) + hotel2["propertyCurrency"])
        try:
            print("洲际：" + str(hotel2["lowestPointsOnlyCost"]["points"]) + " points")
            if hotel2["lowestPointsOnlyCost"]["points"] < 20000:
                break
        except:
            print("洲际：" + "There is not reward night")
    # sleep(random.random()*10)




