import uuid
from datetime import datetime
from utils import Result, MESSAGES_FILE_PATH
import json
import user

def __saveToFile(message: dict) -> None:
    with open(MESSAGES_FILE_PATH, 'a' ) as f:
        message.update({'id':str(message['id'])})
        print(json.dumps(message), file=f)

def __getByReceiver(receiverID: str)->list:
    res = []
    with open(MESSAGES_FILE_PATH, 'r')as f:
        messages = f.readlines()
        for message in messages:
            m = json.loads(message)
            if receiverID == m['receiver']:
                res.append(m)
    return res

def Save(senderMail: str, receiverMail: str, body: str) -> (Result,dict):
    sndr = user.findByIDorEmail(senderMail)
    rcvr = user.findByIDorEmail(receiverMail)

    if sndr is not None and rcvr is not None and sndr['id'] != rcvr['id']:
        id = uuid.uuid4()
        message = {
            'id': id,
            'sender': senderMail,
            'receiver': rcvr['id'],
            'created': datetime.utcnow().isoformat(),
            'body': body
        }
        __saveToFile(message)
        return Result.OK, message
    else:
        return Result.NOT_FOUND, None

def Retrieve(receiverID: str) -> (Result, dict):
    r = user.findByIDorEmail(receiverID)
    if r is not None:
        return Result.OK, __getByReceiver(r['id'])
    else:
        return Result.NOT_FOUND, None
 

