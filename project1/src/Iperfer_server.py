
import socket
import sys
import time
import argparse

#To find out in which mode to run
#Credit: https://docs.python.org/2/library/argparse.html#action 
parser = argparse.ArgumentParser()
parser.add_argument('-s')
flag = parser.parse_args()
if flag.s:
    pass
    #Iperfer should operate in server mode

    #python3 Iperfer.py -s <listen port>

    if len(sys.argv) > 3 or len(sys.argv) < 3:
        sys.exit('Error: missing or additional arguments')
    if int(sys.argv[3]) < 1024 or int(sys.argv[3]) > 65535:
        sys.exit('Error: port number must be in the range 1024 to 65535')

     #....

else:
    pass
    #Iperfer should operate in client mode

#Creating server
ServerName = 'Iperfer_server'
ServerPort = int(sys.argv[3])
ServerAddress = (ServerName, ServerPort)

#Creating server socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Associating server port number with the socket
serverSocket.bind(ServerAddress)

#Waiting for some client to knock on the door
serverSocket.listen(1) #maximum number of queued connections (at least 1)

print('The server is ready to listen')
#Creating connection socket
#It is blocked and don't go to while-loop if no one connects
connection_socket, addr = serverSocket.accept() 

count = 0 #in KB

start_time = time.time()
while 1:
    #Receiving message from client
    message = connection_socket.resv(1000)

    #Modifying the message
    modified_message = message.replace('0', '1')
    count+=1

    #Sending the modified message
    modified_socket.send(modified_message)
    print("Reply sent", addr)

stop_time = time.time() - start_time
mb = count/1000
rate = mb/stop_time

print('Sent = {count} KB. Rate = {rate}'.format(count, rate))

#Closing communication with client
connection_socket.close()