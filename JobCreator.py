#This is the job creator which tells the job seeker what jobs to perform
from socket import *
from random import randrange

serverName = gethostbyname(gethostname())#gets the host ip
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

while True:

    job = str(randrange(4)) #decides by a random generator what job to ask the seeker to perform

    #statements for job that it asks the seeker to perform
    if job=='0':
        print("Add together two numbers of your choice")

    elif job=='1':
        print("Subtract two numbers of your choice")

    elif job=='2':
        print("Divide two numbers of your choice")

    elif job=='3':
        print("Multiply two numbers of your choice")

    #input for the two numbers
    num1 = input('Input the first number: ')
    num2 = input('Input the second number: ')


    clientSocket.send(num1.encode())#sends num1 to the seeker
    clientSocket.send(num2.encode())#sends num2 to the seeker
    clientSocket.send(job.encode())#sends job to the seeker

    #asks the seeker if it wants to perform more jobs. "no" will terminate the client and server
    data = input('Do you want to preform more jobs? (yes or no) ')
    clientSocket.send(data.encode())#sends whehter or not to perform more jobs

    calc = clientSocket.recv(1024)
    print('Answer From Server: ', calc.decode())#recieves the calculation answer from the seeker

    #will terminate if no more jobs are requested
    if data=="no":
        print(clientSocket.recv(1024).decode())
        break
        clientSocket.close()
