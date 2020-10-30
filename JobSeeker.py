#This is a job seeker that offers its services to the creator
from socket import *

#These are the jobs the seeker can offer there services too

#addition function
def add(a,b):
    add = int(a) + int(b)
    return add

#subtraction function
def subtract(a,b):
    subtract = int(a) - int(b)
    return subtract

#divide funciton
def divide(a,b) :
    divide =  int(a) / int(b)
    return divide

#multiply function
def multiply(a,b):
    multiply = int(a)*int(b)
    return multiply

serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('The Job Seeker is ready to recieve jobs!!!') #The server is ready to recieve from the client

connectionSocket, addr = serverSocket.accept()

while True:
    num1 = connectionSocket.recv(1024).decode()#recieves num1 from the creator
    num2 = connectionSocket.recv(1024).decode()#recieves num2 from the creator
    job = connectionSocket.recv(1024).decode()#recieves the job the creator wants the seeker to perform
    data = connectionSocket.recv(1024).decode()#recieves whether or not to perform more jobs

    calc = 0

#depending on what job the creator asks seeker to preform it will choose the correct skill to apply to the service
    if job=='0':
        calc = str(add(num1,num2)) #will calculate addition

    elif job=='1':
         calc = str(subtract(num1,num2)) #will calculate subtraction

    elif job=='2':
         calc = str(divide(num1,num2)) #will calculate division

    elif job=='3':
         calc = str(multiply(num1,num2)) #will calculate multiplication

    connectionSocket.send(calc.encode())

    #If the user enters "no" to not perform more jobs, the server will terminate
    if data == "no":
        print("------ SERVER REMOTE SHUTDOWN ------")
        connectionSocket.send(('Server Terminated').encode())
        connectionSocket.close()
        raise SystemExit
