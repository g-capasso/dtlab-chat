from flask import Flask, request, jsonify
import user
import message
from utils import Result

app = Flask(__name__)

def getErrorCode(result: Result)->int:
    
    if result is Result.NOT_FOUND:
        code = 404
    elif result is Result.NOT_AUTHORIZED:
        code = 403
    elif result is Result.DUPLICATED:
        code = 409
    else:
        code = 500

    return code

@app.route('/user', methods=['POST'])
def createUser():
    data = request.get_json()
    name = data['name']
    surname = data['surname']
    email = data['email']
    password = data['password']
    
    result, u = user.SaveUser(name, surname, email, password)

    if result is not Result.OK:
        code = getErrorCode(result)
        return '', code
    else:
        return u, 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data['email']
    password = data['password']
    
    result, u = user.Login(email, password)

    if result is not Result.OK:
        code = getErrorCode(result)
        return '', code
    else:
        return u, 200

@app.route('/inbox', methods=['POST'])
def send():
    data = request.get_json()
    receiver = data['receiver']
    sender = data['sender']
    body = data['body']

    result,m = message.SaveMessage(sender, receiver, body)

    if result is not Result.OK:
        code = getErrorCode(result)
        return '', code
    else:
        return m, 201

@app.route('/inbox/<receiverID>', methods=['GET'])
def receive(receiverID: str):

    result,mxs = message.GetMessages(receiverID)

    if result is not Result.OK:
        code = getErrorCode(result)
        return '', code
    else:
        return jsonify(mxs), 200

@app.route('/user', methods=['DELETE'])
def deleteUser():

    email = request.authorization['username']
    password = request.authorization['password']
    result, u = user.Login(email, password)
    if result is not Result.OK:
        code = getErrorCode(result)
        return '', code
    else:
        user.Delete(u['id'])
        return '', 204

if __name__ == '__main__':
    app.run(host='localhost',port=5000,debug=True)
