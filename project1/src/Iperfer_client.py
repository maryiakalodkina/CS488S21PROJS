import socket
import sys
import time

if len(sys.argv) > 4 or len(sys.argv) < 4:
    sys.exit('Error: missing or additional arguments')
if int(sys.argv[2]) < 1024 or int(sys.argv[2]) > 65535:
    sys.exit('Error: port number must be in the range 1024 to 65535')

#Create server
ServerName = sys.argv[1]
ServerPort = int(sys.argv[2])
ServerAddress = (ServerName, ServerPort)

time_window = float(sys.argv[3]) #elapsed in seconds, [0] is prog name

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(ServerAddress)
#Create client socket
#with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientSocket: #IPv4$
    #Ask for connection to server, attach the socket directly to the remote ad$
    # clientSocket.connect(ServerAddress)
    #set time out
   # clientSocket.settimeout(time_window)
#3-way handshake is performed => connection is established
clientSocket.settimeout(time_window)
#clientSocket = socket.create_connection(ServerAddress, timeout=time_window)
starttime = time.time()
count = 0 #in KB
while 1: #and not socket.timeout:
    try:
        #left-justify=padding message uwith fixed size '0'
        message = '0'
        message = message.ljust(1000, '0')
        count += 1
        #Send message
        clientSocket.sendall(message.encode('utf-8')) #change ascii?

    #modified_sent = clientSocket.recvfrom(1000)
    except socket.timeout as e:
        break
    if socket.timeout > 0 and time.time() - starttime >= socket.timeout:      $
        clientSocket.close()

mb = count/1000
rate = mb/time_window

print('Sent = {count} KB. Rate = {rate}'.format(count, rate))

