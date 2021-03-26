import uuid
import bcrypt
from datetime import datetime
from utils import Result, USERS_FILE_PATH
import json

#Metodo di utilità per cercare un utente dato in ingresso un ID. Se non esiste viene ritornato None
def findByIDorEmail(filter: str) -> dict:
    with open(USERS_FILE_PATH, 'r') as f:
        users = f.readlines()
        for user in users:
            u = json.loads(user)
            if filter == u['id'] or filter == u['email']:
                u.update({'password': u['password'].encode('utf8')})
                return u
        return None

def __saveToFile(user: dict) -> None:
    with open(USERS_FILE_PATH, 'a' ) as f:
        user.update({'password': user['password'].decode('utf8')})
        user.update({'id':str(user['id'])})
        print(json.dumps(user), file=f)

def Save(name: str, surname: str, email: str, password: str) -> (Result, dict):
    if findByIDorEmail(email) is None:
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
        __saveToFile(user)
        user['password'] = ''
        return Result.OK, user
    else:
        return Result.DUPLICATED, None


# La funzione login controlla che esiste un utente con l'email inserita ed usa la funzione bcrypt.checkpw per controllare che la password sia corretta.
def Login(email: str, password: str)->(Result, dict):
    u = findByIDorEmail(email)
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
            print(json.dumps(user), file=f)