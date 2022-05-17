import socket
import sys

serverAddress = socket.gethostbyname(socket.gethostname())
port = 14000
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bufferSize = 2048

admin = socket.gethostbyname(socket.gethostname())

try:
    serverSocket.bind((serverAddress, port))

except socket.error:
    print("The Server failed to start!")
    sys.exit()

print("Server started successfully! \n")

while True:

    data, client_address = serverSocket.recvfrom(bufferSize)

    method = data.decode("utf-8")
    
    print("Server connected with the client: [" + client_address[0] + "] with port: ["+ str(client_address[1]) +"]\n")

    def send_to_client(a):
   
        bytesToSend = str.encode(a)
        serverSocket.sendto(bytesToSend, client_address)
        
    def delete(a,b):
        if(client_address[0] != admin):
            send_to_client("You cannot perform this action!")
        else:    
            try:
                session = open('data.txt', 'r')
                lines = session.readlines()
                session.close()
                for line in lines:
                    if a in line and b in line:
                        lines.remove(line)
                session_2 = open('data.txt', 'w')
                for line in lines:
                    session_2.write(line)
                session_2.close()
                send_to_client("success")
            except:
                msg_reply = "failure"
                send_to_client(msg_reply)

    def search(a):
        try:
            session=open("data.txt",'r')
            for x in session:
                if a in x:
                    y=x.split("&")
                    del y[-1]
                    p=""
                    for l in y:
                        p=p+l
                        p=p+"&"
                    send_to_client(p)              
        except:
            msg_reply = "failure"
            send_to_client(msg_reply)

    def entry(a,b,c,d,e,f):
        if(client_address[0] != admin):
            send_to_client("You cannot perform this action!")
        else:
            try:
                session=open("data.txt",'a')
                session.write(a+"&"+b+"&"+c+"&"+d+"&"+e+"&"+f+"\n")
                session.close()
                msg_reply = "success"
                send_to_client(msg_reply)
            except:
                msg_reply = "failure"
                send_to_client(msg_reply)

    print(data)
    clientMsg = format(data)
    clientIP = format(client_address)
    msg_recieved=clientMsg.split("&")
    if msg_recieved[0]=="b'1":
        entry(msg_recieved[1],msg_recieved[2],msg_recieved[3],msg_recieved[4],msg_recieved[5],msg_recieved[6][:-1])
    elif msg_recieved[0]=="b'2":
        search(msg_recieved[2][:-1])
    elif msg_recieved[0]=="b'3":
        delete(msg_recieved[1],msg_recieved[2][:-1])
