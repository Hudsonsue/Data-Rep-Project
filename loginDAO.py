import pymysql
import pymysql.cursors
class LoginDAO:

    db=""
    def __init__(self): 
        self.db = pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        database="datarepresentation"
		)

    def login(self, username, password):	
		
## Check if account exists using MySQL
        cursor=self.db.cursor()
        sql= "select * from accounts where username =%s and password =%s"
        cursor.execute(sql, (username, password))
        account = cursor.fetchone()	
        returnArray = []
        print(account)
        if account:
            return 1
        return None
		 
loginDAO = LoginDAO()