
from app import extensions

def getfilenumber():
    file   = open('files/counter.txt', 'r')
    number = str(file.read())
    file.close()
    file   = open('files/counter.txt', 'w+')
    file.write(str(int(number) + 1))
    file.close()
    return number


