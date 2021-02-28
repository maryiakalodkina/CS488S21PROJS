
import socket
import sys
import timeit
import argparse

if len(sys.argv) > 3 or len(sys.argv) < 3:
    sys.exit('Error: missing or additional arguments')
if int(sys.argv[3]) < 1024 or int(sys.argv[3]) > 65535:
    sys.exit('Error: port number must be in the range 1024 to 65535')

#Credit: https://docs.python.org/2/library/argparse.html#action 
parser = argparse.ArgumentParser()
parser.add_argument('-s', action='store_true')
flag = parser.parse_args()
if flag.s:
    pass
    #Iperfer should operate in server mode
else:
    pass
    #Iperfer should operate in client mode


#Server code

#Creating server
ServerName = 'localhost'
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

while 1:
    try:
        #Receiving message from client
        message = connection_socket.resv(1000)

        #Modifying the message
        modified_message = message.replace('0', '1')
        count+=1

        #Sending the modified message
        modified_socket.send(modified_message)
    
        print("Reply sent", addr)

mb = count/1000
rate = mb/time_window
print('The total number of bytes received (in kilobytes) = {count}'.format(count), end=' ')
print('The rate at which traffic could be read (in megabits per second (Mbps)) = {rate}'.format(rate))

#Closing communication with client
connection_socket.close()