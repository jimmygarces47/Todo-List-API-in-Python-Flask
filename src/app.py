from flask import Flask,jsonify,request
import json
app = Flask(__name__)

todos=[
{"label":"my first task","done":False}
]
# Estas dos líneas siempre seben estar al final de tu archivo app.py.
@app.route('/blabla', methods=['GET'])
def hello_world():
    return 'Hello, World!'

@app.route('/todos', methods=['GET'])
def hello():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json(force=True)
    todos.append(request_body)
    print("Incoming request with the following body", request_body)
    return (jsonify(todos))

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)
    todos.pop(position)
    return (jsonify(todos))

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
  

  