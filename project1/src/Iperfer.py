import socket
import sys
import time

if sys.argv[1] == "-s":
    #pass
    #Iperfer should operate in server mode

    #python3 Iperfer.py -s <listen port>
    if len(sys.argv) > 3 or len(sys.argv) < 3:
      print('Error: missing or additional arguments')
      sys.exit(1)
    if int(sys.argv[2]) < 1024 or int(sys.argv[2]) > 65535:
      print('Error: port number must be in the range 1024 to 65535')
      sys.exit(1)

    #Creating server
    ServerName = 'localhost'
    ServerPort = int(sys.argv[2])
    ServerAddress = (ServerName, ServerPort)

 #Creating server socket
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Associating server port number with the socket
    serverSocket.bind(ServerAddress)

    #Waiting for some client to knock on the door
    serverSocket.listen(1) #maximum number of queued connections (at lea$

    print('The server is ready to listen')
    #Creating connection socket
    #It is blocked and don't go to while-loop if no one connects
    Scount = 0 #in Bytes
    #connection_socket, addr = serverSocket.accept()
    start_time2 = time.time()
    while 1:
      connection_socket, addr = serverSocket.accept()  #move to while-lo$
      #start_time2 = time.time()
      while 1:
        #Receiving message from client
        message = connection_socket.recv(1000)
      
      #Scount+=1000
        if message[0] == 69:
        #connection_socket.close()
          stop_time2 = time.time()-start_time2
          connection_socket.close()
        #print(stop_time2)
          break
        Scount+=1000
      break
        #Closing communication with client
     # connection_socket.close()
   # print(stop_time2)
    #stop_time2 = time.time() - start_time2
    print('Count: {} and StopTime: {}'.format(Scount, stop_time2))
    serverSocket.close()
    megabit = Scount*0.000008
    Scount = Scount/1000 #now it's in KB
    #print("count: {}".format(count))
    rate = megabit/stop_time2
    #print("time_window: {}".format(time_window))
    print('received = {} KB. rate = {} Mbps'.format(Scount, rate))

else:

    if len(sys.argv) > 4 or len(sys.argv) < 4:
      print('Error: missing or additional arguments')
      sys.exit(1)
    if int(sys.argv[2]) < 1024 or int(sys.argv[2]) > 65535:
      print('Error: port number must be in the range 1024 to 65535')
      sys.exit(1)        
#Create server
        #ServerName = sys.argv[2]
    ServerName = sys.argv[1]
    ServerPort = int(sys.argv[2])
    ServerAddress = (ServerName, ServerPort)

    time_window = float(sys.argv[3]) #elapsed in seconds, [0] is prog na$

    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect(ServerAddress)

#Create client socket

    clientSocket.settimeout(time_window)
#3-way handshake is performed => connection is established

    start_time = time.time()
    count = 0 #in B

    while (time.time()-start_time) < time_window:
#      print('Time: {}'.format(clientSocket.settimeout))
 
      size = 1000 
      message = bytearray(size)

      try:
        clientSocket.sendall(message)
        count += 1000
      except clientSocket.timeout as e:
        break
        
      #  clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      #  clientSocket.connect(ServerAddress)
      #  clientSocket.sendall(message)
      #  count += 1000
 
   # clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   # clientSocket.connect(ServerAddress)
    messageEOF = 'E'
    clientSocket.send(messageEOF.encode('ascii'))

  #  clientSocket.close()   
    print(count)
    megabit = count*0.000008
    count = count/1000
    rate = megabit/time_window
    print('sent = {} KB. rate = {} Mbps'.format(count, rate))

