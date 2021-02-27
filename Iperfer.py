import socket
import sys
import timeit

if len(sys.argv) > 4 or len(sys.argv) < 4:
    sys.exit('Error: missing or additional arguments')
if sys.argv[2] < 1024 or sys.argv[2] > 65535:
    sys.exit('Error: port number must be in the range 1024 to 65535')

#Create server
ServerName = sys.argv[1]
ServerPort = sys.argv[2]
ServerAddress = (ServerName, ServerPort)

time_window = sys.argv[3] #elapsed in seconds, [0] is prog name


#Create client socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientSocket: #IPv4, TCP socket
    #Ask for connection to server, attach the socket directly to the remote address.
    clientSocket.connect(ServerAddress)
    #set time out
    clientSocket.settimeout(time_window)
#3-way handshake is performed => connection is established
count = 0 #in KB
    while 1: 
        try:
            #left-justify=padding message with fixed size '0'
            message = '0' 
            message = message.ljust(1000, '0')
            count += 1
            #Send message
            clientSocket.sendall(message.encode('ascii')) #change ascii?

            #modified_sent = clientSocket.recvfrom(1000)

        except socket.timeout as e:
            break

mb = count/1000
rate = mb/time_window
print('Sent = {count} KB'.format(count), end='     ')
print('Rate = {rate}'.format(rate))

 