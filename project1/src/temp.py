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

clientSocket.settimeout(time_window)
#3-way handshake is performed => connection is established

start_time = time.time() 
count = 0 #in KB 
while (time.time() - 
start_time) < time_window:
    try:
        #left-justify=padding message uwith fixed size '0'
        message = '0'
        message = message.ljust(1000, '0')
        while (time.time() - start_time) < time_window:
           count += 1
           clientSocket.sendall(message.encode('utf-8')) #change ascii?
    except socket.timeout as e:
        break 
clientSocket.close() 


megabit = count*0.0078125

#print("count: {}".format(count))
rate = megabit/time_window
#print("time_window: {}".format(time_window))
print('Sent = {} KB. Rate = {} Mbps'.format(count, rate))
