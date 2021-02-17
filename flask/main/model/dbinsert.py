# import pymysql
# import csv

# conn= pymysql.connect(host='localhost',user='root',password='drims123',db='carproject',charset='utf8')
# curs = conn.cursor()

# addr_sql = "insert into CAMPING_ADDRESS (CAMPING_INDEX,ROAD_ADDRESS,NUMBER_ADDRESS,X_LOCATION,Y_LOCATION, REGION,CITY, ZIPCODE) values (%s,%s,%s,%s,%s,%s,%s,0)"
# camping_addr = open("Camp_Address2.csv",'r')
# camping_info = open("Camp_Info2.csv",'r')

# addr = csv.reader(camping_addr)
# info = csv.reader(camping_info)
# info_sql = "insert into CAMPING_INFO (CAMPING_INDEX,NAME,SITE_DIMENTION,SITE_COUNT,MAX_CAPACITY,FACILITY,IS_EXPOSURE,THEME) values (%s,%s,%s,%s,%s,%s,True,NULL)"
# for line in addr:
#     camping_index = line[0]
#     road_ad = line[1]
#     number_add = line[2]
#     xaxis = float(line[3])
#     yaxis = float(line[4])
#     region  = line[5]
#     city = line[6]
#     curs.execute(addr_sql,(camping_index,road_ad,number_add,xaxis,yaxis,region,city))
# # for line in info:
# #     camping_index = line[0]
# #     name =line[1]
# #     try:
# #         dim = float(line[2])
# #     except:
# #         dim = None
# #     print(dim)
# #     site = int(line[3])
# #     max_capa = int(line[4])
# #     facil = line[5]
# #     # curs.execute(info_sql,(line[0],line[1],line[2],line[3],line[4],line[5],line[6],True))
# #     curs.execute(info_sql,(camping_index,name,dim,site,max_capa,facil))

# conn.commit()
# conn.close()
# camping_info.close()
# camping_addr.close()