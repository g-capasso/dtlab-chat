from enum import Enum
from os.path import join, isfile, isdir
from os import mkdir, mknod
# Result è un'enumerazione. Serve a rendere più leggibile il codice. Ad esempio, 
# potrei far ritornare 2 quando un utente non viene trovato, ma questo sarebbe poco leggibile. 
# In python, le enumerazioni sono un particolare tipo di classe che ereditano da Enum.
class Result(Enum):
    OK = 1
    NOT_FOUND = 2 
    NOT_AUTHORIZED = 3
    DUPLICATED = 4

__data_directory = 'data'
USERS_FILE_PATH = join(__data_directory, 'users.txt')
MESSAGES_FILE_PATH = join(__data_directory, 'messages.txt')

# This function creates directory and files needed to read/write users and messages. It has to be called when program starts
def InitFS():
    if not isdir(__data_directory):
        mkdir(__data_directory)
        mknod(USERS_FILE_PATH)
        mknod(MESSAGES_FILE_PATH)
    else:
        if not isfile(USERS_FILE_PATH):
            mknod(USERS_FILE_PATH)

        if not isfile(MESSAGES_FILE_PATH):
            mknod(MESSAGES_FILE_PATH)
