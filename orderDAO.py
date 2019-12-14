import pymysql
import pymysql.cursors
class OrderDAO:
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
        sql="insert into orders (Item, About,Quantity) values (%s,%s,%s)"
        cursor.execute(sql, values)

        self.db.commit()
        return cursor.lastrowid

    def getAllOrders(self):
        cursor = self.db.cursor()
        sql="select * from orders"
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
        sql="select * from orders where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDictionary(result)

    def update(self, values):
        cursor = self.db.cursor()
        sql="update orders set quantity = %s where id = %s"
        cursor.execute(sql, values)
        self.db.commit()
		
     
    def convertToDictionary(self, result):
	 
	 
        colnames=[ 'id','Item','About', "Quantity"]
        item = {}
        
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        return item
		

        
orderDAO = OrderDAO()