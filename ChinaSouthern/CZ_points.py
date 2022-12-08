import fileinput
import re
import json
import datetime
import random
import requests
from datetime import datetime, timedelta
import pandas as pd
import csv
from time import sleep
from sqlalchemy.orm import Session

# 链接等的设置
url = 'https://m.csair.com/CSMBP/bookProcess/mileage/queryInterFlight?type=MOBILE&APPTYPE=touch&chanel=touch&lang=en&holder=ADR'
content_type = 'application/json; charset=utf-8'
ua_list = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .\
    NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)', ]
headers = {'Content-Type':content_type,  'User-Agent': random.choice(ua_list)}


load = pd.read_csv('csairInter.csv')
depCity = load["DepCity"].tolist()
arrCity = load["ArrCity"].tolist()
dayOfWeek = load["DayOfWeek"].tolist()
for j in range(26, len(depCity)):
    with open("CZ_Points.json", "r+") as jsonFile:
        data = json.load(jsonFile)
        data["depCity"] = depCity[j]
        data["arrCity"] = arrCity[j]
        jsonFile.seek(0)
        json.dump(data, jsonFile)
        jsonFile.truncate()
        jsonFile.close()
    if dayOfWeek[j] == 1:
        A = '2022-08-22'
    elif dayOfWeek[j] == 2:
        A = '2022-08-23'
    elif dayOfWeek[j] == 3:
        A = '2022-08-24'
    elif dayOfWeek[j] == 4:
        A = '2022-08-25'
    elif dayOfWeek[j] == 5:
        A = '2022-08-26'
    elif dayOfWeek[j] == 6:
        A = '2022-08-27'
    else:
        A = '2022-08-28'
    datetime_obj = datetime.strptime(A, '%Y-%m-%d')                 # 确定了出发地，目的地，起始的爬取时间
    # print(A)

    flag1, flag2, flag3 = 0, 0, 0
    for i in range(200):
        datetime_obj = datetime_obj + timedelta(days=1)
        datetime_str = str(datetime_obj.date())
        datetime_str = re.sub('-', '', datetime_str)
        with open("CZ_Points.json", "r+") as jsonFile:
            data = json.load(jsonFile)
            data["flightDate"] = datetime_str
            # data["depCity"] = "PAR"
            # data["arrCity"] = "NYC"
            jsonFile.seek(0)
            json.dump(data, jsonFile)
            jsonFile.truncate()
            jsonFile.close()
        body = open('CZ_Points.json')
        body = body.read()
        try:
            resp = requests.post(url, headers=headers, data=body, timeout=5)
            response = json.loads(resp.text)
        except:
            print("Time out: date:" + datetime_str)
            continue
        print("日期：" + str(datetime_obj.date()), end="    ")
        print("出发地:" + str(depCity[j]), end="   ")
        print("目的地:" + str(arrCity[j]))
        try:
            for flights in response["segments"]:
                EconomyRewards = flights["dateFlight"]["directFlight"][0]["cabinsY"]
                SuperEconomyRewards = flights["dateFlight"]["directFlight"][0]["cabinsW"]
                BusinessRewards = flights["dateFlight"]["directFlight"][0]["cabinsFJ"]
                if len(EconomyRewards) > 0:
                    print("经济舱余位：" + str(EconomyRewards[0]["info"]))
                    print("经济舱价格：" + str(EconomyRewards[0]["adultMileage"]))
                    if EconomyRewards[0]["info"] == '>9' or int(EconomyRewards[0]["info"]) > 0:
                        flag1 += 1
                        # print('\n''\n\n\n\n\n')
                if len(BusinessRewards) > 0:
                    print("商务舱余位：" + str(BusinessRewards[0]["info"]))
                    print("商务舱价格：" + str(BusinessRewards[0]["adultMileage"]))
                    if BusinessRewards[0]["info"] == '>9' or int(BusinessRewards[0]["info"]) > 0:
                        flag2 += 1
                        # print('\n''\n\n\n\n\n')
                if len(SuperEconomyRewards) > 0:
                    print("超级经济舱余位：" + str(SuperEconomyRewards[0]["info"]))
                    print("超级经济舱价格：" + str(SuperEconomyRewards[0]["adultMileage"]))
                    if SuperEconomyRewards[0]["info"] == '>9' or int(SuperEconomyRewards[0]["info"]) > 0:
                        flag3 += 1
                        # print('\n''\n\n\n\n\n')
        except:
            print("There is not places or there is error")
    print(depCity[j] + "出发", arrCity[j] + "到达")
    print("经济舱有" + str(flag1) + "天有空位")
    print("商务舱有" + str(flag2) + "天有空位")
    print("超经有" + str(flag3) + "天有空位")
    print('\n''\n\n\n\n\n')
    print('\n''\n\n\n\n\n')
    print('\n''\n\n\n\n\n')
