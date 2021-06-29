from flask import Flask , request , jsonify
import database
app = Flask(__name__)

@app.route('/')
def hello_world():  
   return 'Hello World' 

@app.route('/insert' , methods=['GET'])
def insert():
    name = request.args.get('name')
    age = request.args.get('age')
    address = request.args.get("address") 
    database.insert_data(name, age,address)
    return jsonify({'message' : "success"})

@app.route('/update' , methods=['GET'])
def update():
    _id = request.args.get('_id')
    name = request.args.get('name')
    age = request.args.get('age')
    address = request.args.get("address") 
    database.update_data(_id,name,age,address)
    return jsonify({'message' : "success"})

@app.route('/find' , methods=['GET'])
def find():
    _id = request.args.get('_id')
    jsonData = database.get_data(_id)
    return jsonify(jsonData)

@app.route('/delete' , methods=['GET'])
def delete():
    _id = request.args.get('_id')
    database.delete_data(_id)
    return jsonify({'message' : "success"})

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=5000, debug=True)
