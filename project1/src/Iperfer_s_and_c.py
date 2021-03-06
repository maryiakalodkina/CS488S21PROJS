
import socket
import sys
import time
#import argparse

#To find out in which mode to run
#Credit: https://docs.python.org/2/library/argparse.html#action 
#parser = argparse.ArgumentParser()
#parser.add_argument('-s')
#flag = parser.parse_args()
#if flag.s:

if sys.argv[1] == "-s":
    #pass
    #Iperfer should operate in server mode

    #python3 Iperfer.py -s <listen port>
    if len(sys.argv) > 3 or len(sys.argv) < 3:
        sys.exit('Error: missing or additional arguments')
    if int(sys.argv[2]) < 1024 or int(sys.argv[2]) > 65535:
        sys.exit('Error: port number must be in the range 1024 to 65535')
    
    #Creating server
    ServerName = 'localhost'
    ServerPort = int(sys.argv[2])
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
    count = 0 #in KB

    while 1:
        connection_socket, addr = serverSocket.accept()  #move to while-loop
        start_time = time.time()

        #Receiving message from client
        message = connection_socket.recv(1000) 

        #Modifying the message
        modified_message = message.replace('0', '1')
        count+=1

        #Sending the modified message
        modified_socket.send(modified_message)
        print("Reply sent", addr)

        #Closing communication with client
        connection_socket.close()

    stop_time = time.time() - start_time
    
    megabit = count*0.0078125
    #print("count: {}".format(count))
    rate = megabit/stop_time
    #print("time_window: {}".format(time_window))
    print('Sent = {} KB. Rate = {} Mbps'.format(count, rate))
    
     

elif sys.argv[1] == "-c":


	import socket
	import sys
	import time

	if len(sys.argv) > 5 or len(sys.argv) < 5:
    		sys.exit('Error: missing or additional arguments')
	if int(sys.argv[3]) < 1024 or int(sys.argv[3]) > 65535:
    		sys.exit('Error: port number must be in the range 1024 to 65535')
	#Create server
	#ServerName = sys.argv[2]
	ServerName = sys.argv[2]
	ServerPort = int(sys.argv[3])
	ServerAddress = (ServerName, ServerPort)

	time_window = float(sys.argv[4]) #elapsed in seconds, [0] is prog name

	clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	clientSocket.connect(ServerAddress)

#Create client socket

	clientSocket.settimeout(time_window)
#3-way handshake is performed => connection is established

	start_time = time.time()
	count = 0 #in KB
	while (time.time() - start_time) < time_window:
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




