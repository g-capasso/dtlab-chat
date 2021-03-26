import uuid
import bcrypt
from datetime import datetime
from utils import Result, USERS_FILE_PATH
import json


#Metodo di utilità per cercare un utente dato in ingresso un ID. Se non esiste viene ritornato None
def findUserByID(id: str) -> dict:
    with open(USERS_FILE_PATH, 'r') as f:
        users = f.readlines()
        for user in users:
            u = json.loads(user)
            if id == u['id']:
                u.update({'password': u['password'].encode('utf8')})
                return u
        return None

def findUserByEmail(email: str) -> dict:
    with open(USERS_FILE_PATH, 'r') as f:
        users = f.readlines()
        for user in users:
            u = json.loads(user)
            if email == u['email']:
                u.update({'password': u['password'].encode('utf8')})
                return u
        return None

def saveUserToFile(user: dict) -> None:
    with open(USERS_FILE_PATH, 'a' ) as f:
        user.update({'password': user['password'].decode('utf8')})
        user.update({'id':str(user['id'])})
        print(json.dumps(user), file=f)

def SaveUser(name: str, surname: str, email: str, password: str) -> (Result, dict):
    if findUserByEmail(email) is None:
        id = uuid.uuid4()
        hashed = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
        user = {
            'id': id,
            'name': name,
            'surname': surname,
            'email': email,
            'created': datetime.utcnow().isoformat(),
            'password': hashed
        }
        saveUserToFile(user)
        user['password'] = ''
        return Result.OK, user
    else:
        return Result.DUPLICATED, None


# La funzione login controlla che esiste un utente con l'email inserita ed usa la funzione bcrypt.checkpw per controllare che la password sia corretta.
def Login(email: str, password: str)->(Result, dict):
    u = findUserByEmail(email)
    if u is not None and bcrypt.checkpw(password.encode('utf8'), u['password']):
        u.update({'password':''}) 
        return Result.OK, u
    else:
        return Result.NOT_AUTHORIZED, None

def Delete(id: str)-> None:
    newList = []
    with open(USERS_FILE_PATH, 'r') as f:
        users = f.readlines()
        for user in users:
            u = json.loads(user)
            if u['id'] != id:
                newList.append(u)

    with open(USERS_FILE_PATH, 'w')as f:
        for user in newList:
            print(user, file=f)


### TESTING user.py module
if __name__ == '__main__':
    id = uuid.uuid4()
    hashed = bcrypt.hashpw('123'.encode('utf8'), bcrypt.gensalt())
    user = {
        "id": id,
        "name": 'giuseppe',
        "surname": 'capassso',
        "email": 'giuseppe@null.com',
        "created": datetime.utcnow().isoformat(),
        "password": hashed
    }
    saveUserToFile(user)
    u = findUserByID(str(id))
    u = findUserByEmail('giuseppe@null.com')
    res, u = Login(u['email'], '123')
    print(u)
