import uuid
from datetime import datetime
from utils import Result
import json
import user

FILE_NAME = 'data/messages.txt'

def saveMessageToFile(message: dict) -> None:
    with open(FILE_NAME, 'a' ) as f:
        message.update({'id':str(message['id'])})
        print(json.dumps(message), file=f)

def getMessagesByReceiver(receiverID: str)->list:
    res = []
    with open(FILE_NAME, 'r')as f:
        messages = f.readlines()
        for message in messages:
            m = json.loads(message)
            if receiverID == m['receiver']:
                res.append(m)
    return res

def SaveMessage(senderID: str, receiverMail: str, body: str) -> (Result,dict):
    sndr = user.findUserByID(senderID)
    rcvr = user.findUserByEmail(receiverMail)

    if sndr is not None and rcvr is not None and senderID != rcvr['id']:
        id = uuid.uuid4()
        message = {
            "id": id,
            "sender": senderID,
            "receiver": rcvr['id'],
            "created": datetime.utcnow().isoformat(),
            "body": body
        }
        saveMessageToFile(message)
        return Result.OK, message
    else:
        return Result.NOT_FOUND, None

def GetMessages(receiverID: str) -> (Result, dict):
    r = user.findUserByID(receiverID)
    if r is not None:
        return Result.OK, getMessagesByReceiver(receiverID)
    else:
        return Result.NOT_FOUND, None
 

