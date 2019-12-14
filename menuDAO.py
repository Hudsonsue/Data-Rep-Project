import pymysql
import pymysql.cursors
class MenuDAO:
    db=""
    def __init__(self): 
        self.db = pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        database="datarepresentation"
		)
		
		
    def create(self, values):
        cursor = self.db.cursor()
        sql="insert into menu (Item, About, Price) values (%s,%s,%s)"
        cursor.execute(sql, values)

        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql="select * from menu"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            print(result)
            returnArray.append(self.convertToDictionary(result))


        return returnArray

    def findByID(self, id):
        cursor = self.db.cursor()
        sql="select * from menu where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDictionary(result)

    def update(self, values):
        cursor = self.db.cursor()
        sql="update menu set Item= %s,About=%s, Price=%s  where id = %s"
        cursor.execute(sql, values)
        self.db.commit()
		
    def delete(self, id):
        cursor = self.db.cursor()
        sql="delete from menu where id = %s"
        values = (id,)

        cursor.execute(sql, values)

        self.db.commit()
        print("delete done")

    def convertToDictionary(self, result):
        colnames=['id','Item','About', "Price"]
        item = {}
        
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        
        return item
        
menuDAO = MenuDAO()