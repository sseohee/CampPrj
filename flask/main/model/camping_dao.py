# from dto import Camping_review
from model.dbModule import Database
from datetime import datetime

class CampingDao:

    def get_top_ten_viewed(self):
        db_class = Database()
        results = None
        formattedDate = datetime.now().strftime("%Y%m%d")
        now_hour = datetime.now().hour
        try:
            sql = """SELECT INFO.CAMPING_INDEX, INFO.NAME, POPULARITY.SCORE FROM CAMPING_INFO as INFO INNER JOIN CAMPING_POPULARITY as POPULARITY ON INFO.CAMPING_INDEX = POPULARITY.CAMPING_INDEX ORDER BY SCORE LIMIT 10;"""
            results = db_class.executeAll(sql)
        except:
            print("오류 발생")
        return results
# 20200103 01 -> search counts
# rank() mysql . 

    def search_camping_info(self,sido,gu): 
        result = None
        db_class = Database()
        sql = "SELECT * FROM CAMPING_INFO INFO WHERE INFO.CAMPING_INDEX IN (SELECT ADDRESS.CAMPING_INDEX FROM CAMPING_ADDRESS ADDRESS WHERE ADDRESS.REGION= '"+sido+"' AND ADDRESS.CITY='"+gu+"');"
        try:
            result = db_class.executeAll(sql)
        except:
            print("오류 발생")
        return result
        # recommanded searching results

    def get_camping_review(self,name):
        db_class= Database()
        sql = "Select * from CAMPING_REVIEW where ="+name 
        try:
            result = db_class.executeAll(sql)
        except:
            print("오류 발생")
        return result

    def get_viewed_count(self,index,date,time):
        count = 0 
        db_class= Database()
        sql = """SELECT JSON_EXTRACT(VIEWED_HISTORY_COUNT,'$.\""""+date+"""".\""""+time+""""') FROM CAMPING_POPULARITY WHERE CAMPING_INDEX =\""""+index+ "\";"
        print(sql)
        try:
            count = db_class.execute(sql)
        except:
            print("error occured")
        return str(count)
    
    # def set_viewed_count(self,index):
    #     sql  

    def get_camping_addresses(self,name):
        db_class= Database()
        sql = "Select * from CAMPING_ADDRESS where CAMPING_NAME= "+name 
        try:
            result = db_class.executeAll(sql)
        except:
            print("오류 발생") 
        return result

    def get_every_camping_locations(self):
        db_class = Database()
        results = None
        sql = "select * from CAMPING_ADDRESS"
        try:
            results = db_class.executeAll(sql)
        except:
            print("오류 발생")
        return results
    
