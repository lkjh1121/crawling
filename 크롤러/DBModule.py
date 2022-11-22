#DBModule.py
import pymysql 

class DBModule:
    #생성자를 만든다. 
    def __init__(self, hostname="127.0.0.1", 
                       userid="user01",
                       password="1234",
                       dbname="mydb",
                       port=5306):
        self.db = pymysql.connect(host=hostname, 
                user=userid, 
                password=password, 
                db=dbname, 
                port=port)
        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)

    def close(self):
        self.db.close()
        self.db= None            

    #insert, update,delete 쿼리 , 파라미터값 주고 받기 
    def execute(self, query, args={}):
        self.cursor.execute(query, args)
        self.db.commit() #확정하기 

    def executeOne(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchone()
        return row

    def executeAll(self, query, args={}):
        self.cursor.execute(query, args)
        rows = self.cursor.fetchall()
        return rows
