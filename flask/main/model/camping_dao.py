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
            print("failed")
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
            print("failed")
        return result
        # recommanded searching results

    def get_camping_review(self,name):
        db_class= Database()
        sql = "Select * from CAMPING_REVIEW where ="+name 
        try:
            result = db_class.executeAll(sql)
        except:
            print("failed")
        return result

    def get_camping_addresses(self,name):
        db_class= Database()
        sql = "Select * from CAMPING_ADDRESS where CAMPING_INDEX= "+index 
        try:
            result = db_class.executeAll(sql)
        except:
            print("failed") 
        return result

    def get_every_camping_locations(self):
        db_class = Database()
        results = None
        sql = "select * from CAMPING_ADDRESS"
        try:
            results = db_class.executeAll(sql)
        except:
            print("failed")
        return results
    
