from flask import Flask, jsonify, request, abort
from menuDAO import menuDAO
from orderDAO import orderDAO

app = Flask(__name__, static_url_path='', static_folder='.')

#curl "http://127.0.0.1:5000/menu"
@app.route('/menu')
def getAll():
    #print("in getall")
    results = menuDAO.getAll()
    return jsonify(results)

#curl "http://127.0.0.1:5000/menus/2"
@app.route('/menu/<int:id>')
def findById(id):
    foundMenu = menuDAO.findByID(id)

    return jsonify(foundMenu)

#curl  -i -H "Content-Type:application/json" -X POST -d "{\"Item\":\"hello\",\"About\":\"someone\",\"Price\":123}" http://127.0.0.1:5000/menus
@app.route('/menu', methods=['POST'])
def create():
    
    if not request.json:
        abort(400)
    # other checking 
    menu = {
        "Item": request.json['Item'],
        "About": request.json['About'],
        "Price": request.json['Price'],
    }
    values =(menu['Item'],menu['About'],menu['Price'])
    newId = menuDAO.create(values)
    menu['id'] = newId
    return jsonify(menu)

#curl  -i -H "Content-Type:application/json" -X PUT -d "{\"Item\":\"hello\",\"About\":\"someone\",\"Price\":123}" http://127.0.0.1:5000/menus/1
@app.route('/menu/<int:id>', methods=['PUT'])
def update(id):
    foundMenu = menuDAO.findByID(id)
    if not foundMenu:
        abort(404)
    
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'Price' in reqJson and type(reqJson['Price']) is not int:
        abort(400)

    if 'Item' in reqJson:
        foundMenu['Item'] = reqJson['Item']
    if 'About' in reqJson:
        foundMenu['About'] = reqJson['About']
    if 'Price' in reqJson:
        foundMenu['Price'] = reqJson['Price']

    values = (foundMenu['Item'],foundMenu['About'],foundMenu['Price'],foundMenu['id'])
    menuDAO.update(values)
    return jsonify(foundMenu)
        

    

@app.route('/menu/<int:id>' , methods=['DELETE'])
def delete(id):
    menuDAO.delete(id)
    return jsonify({"done":True})


@app.route('/orders', methods=['POST'])
def createOrder():
    
    if not request.json:
        abort(400)
    # other checking 
    orders = {
        "Item": request.json['Item'],
        "About": request.json['About'],
        "Quantity": request.json['Quantity'],
		
    }
    values =(orders['Item'],orders['About'],orders['Quantity'])
    newId = orderDAO.create(values)
    orders['id'] = newId
    return jsonify(orders)


@app.route('/orders')
def getAllOrders():
    #print("in getall")
    ordersResults = orderDAO.getAllOrders()
    return jsonify(ordersResults)
	
@app.route('/orders/<int:id>', methods=['PUT'])
def updateOrders(id):
    foundOrders = orderDAO.findByID(id)
    if not foundOrders:
        abort(404)
    
    if not request.json:
        abort(400)
    reqJson = request.json
    
	 # if 'Quantity' in reqJson and type(reqJson['Quantity']) is not int:
      
    if 'Item' in reqJson:
        foundOrders['Item'] = reqJson['Item']
    if 'About' in reqJson:
        foundOrders['About'] = reqJson['About']
     

    values = (foundOrders['Item'],foundOrders['About'],foundOrders['id'], foundOrders[Quantity])
    orderDAO.update(values)
    return jsonify(foundOrders)	


if __name__ == '__main__' :
    app.run(debug= True)