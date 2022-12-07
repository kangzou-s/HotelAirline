import requests
# url = 'https://prf.hn/click/camref:1100l7Tze/destination:https://www.marriott.com/reservation/availabilitySearch.mi?isSearch=false&propertyCode=MRSBR&isRateCalendar=false&costView=AVG&numberOfRooms=1&numberOfAdults=2&numberOfChildren=0&useRewardsPoints=true&clusterCode=none&fromDate=07/26/2022&toDate=07/27/2022$setPMCookies=false'
# r = requests.get(url,params=None,headers={'Content-Type':'application/json'})
# reditList = r.history
# print(f'获取重定向的历史记录：{reditList}')
# print(f'获取第一次重定向的headers头部信息：{reditList[0].headers}')
# print(f'获取重定向最终的url：{reditList[len(reditList)-1].headers["location"]}')


# url = 'https://www.ihg.com/hotels/gb/en/find-hotels/select-roomrate?qDest=Paris,%20France&qPt=CASH&qCiD=26&qCoD=27&qCiMy=62022&qCoMy=62022&qAdlt=1&qChld=0&qRms=1&qIta=99627964&qRtP=6CBARC&qAAR=6CBARC&qSlH=PARDL&qAkamaiCC=FR&srb_u=1&qSrt=sAV&qBrs=6c.hi.ex.sb.ul.ic.cp.cw.in.vn.cv.rs.ki.ma.sp.va.sp.re.vx.nd.ii.sx.we.lx&qWch=0&qSmP=0&qRad=30&qRdU=mi&setPMCookies=true&qpMn=0&qLoSe=false'
# response = requests.get(url)
# print(response.text)




# for i in range(0,256):
#     print(i)

# import datetime
# A = datetime.datetime.fromtimestamp((5941328 + 21564000) * 60)
# B = A - datetime.datetime.today()
# print(A)
# print(B)

# print(r.history)
# print(r.status_code)
# print(r.headers)
# print(r.content.decode())
# print(r.history)
# print(r.text)


# 新需求，从transaction出发，找一系列信息
# import pandas as pd
# transaction = pd.read_csv("/Users/zoukang/Desktop/query_result.csv")
# date = transaction["transaction_date"].tolist()
# asin = transaction["order_id"].tolist()
# print(1)


## 测试数据库的连接
import MySQLdb

## change to use mysqldb, don't use _mysql
from MySQLdb import _mysql
from MySQLdb.constants import FIELD_TYPE
# my_conv = {FIELD_TYPE.DOUBLE: float,FIELD_TYPE.VARCHAR :str}
# db = _mysql.connect(host="localhost", db="AirHotel", read_default_file="~/.my.cnf", charset='utf8', conv=my_conv)

db = MySQLdb.connect(host="localhost", db="AirHotel", read_default_file="~/.my.cnf", charset='utf8')
# db.query("select * from IHGCityList")
# db.query("select * from IHGHotelPrice")
cursor = db.cursor()
cursor.execute("select version()")
data = cursor.fetchone()
print ("Database version : %s " % data)
# r = db.store_result()
# result = r.fetch_row(maxrows=0, how=1)
# print(type(result[0]))
# print(result)


