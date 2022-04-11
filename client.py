import socket

str1=input("Zgjedhni hostin dhe portin (Shtyp default per localhost): ")

if str1=='default':
   serverName='localhost'
   serverPort = 14000
else:
    serverName=input("Shkruaj nje IP adrese te re: ")
    serverPort=input("Shkruaj numrin e portit: ")
    serverPort=int(serverPort)


clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bufferSize = 2048

def send_msg(msg):
    msgFromClient = msg
    bytesToSend = str.encode(msgFromClient)
    clientSocket.sendto(bytesToSend, (serverName, serverPort))


do = input('''
		Choose any:
		1 - Store Information
		2 - Search
		3 - Delete your informations
		==> ''')

if do == '1':
    fname = input("Enter first name :")
    lname = input("Enter last name :")
    uname = input("Enter user name :")
    contact = input("Enter your Contact number :")
    emailid = input("Enter your Email-Id :")
    password = input("Enter your password :")
    msg = "1" + "&" + fname + "&" + lname + "&" + uname + "&" + contact + "&" + emailid + "&" + password
    send_msg(msg)
    

if do == '2':
    do = input('''
    		Choose any:
    		1 - Searchby username
    		2 - Searchby first name
    		==> ''')
    if do == '1':
        uname_s = input("Enter your username :")
        msg = "2" + "&" + "1" + "&" + uname_s
        send_msg(msg)
        while True:
            
            msgFromServer = clientSocket.recvfrom(1024)
            global msg_rec
            msg_rec = msgFromServer[0]
            print(msg_rec)

    if do == '2':
        fname_s = input("Enter your first name :")
        msg = "2" + "&" + "2" + "&" + fname_s
        send_msg(msg)
        while True:
           
            msgFromServer = clientSocket.recvfrom(1024)
            msg_rec = msgFromServer[0]
            print(msg_rec)