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
    count = 0 #in KB
    #connection_socket, addr = serverSocket.accept()
    while 1:
      connection_socket, addr = serverSocket.accept()  #move to while-lo$
      start_time = time.time()

        #Receiving message from client
      message = bytearray(connection_socket.recv(1000))
      if message[0] != 2:
        message[0] = 1
        #Modifying the message
        count+=1000
      else:
        break

  #Sending the modified message
      connection_socket.send(message)
      print("Reply sent", addr)
       
        #Closing communication with client
      connection_socket.close()
#    serverSocket.close()
    stop_time = time.time() - start_time

    megabit = count*0.000008
    #print("count: {}".format(count))
    rate = megabit/stop_time
    #print("time_window: {}".format(time_window))
    print('received = {} KB. rate = {} Mbps'.format(count, rate))

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
    count = 0 #in KB

    while (time.time() - start_time) < time_window:
      try:
        size = 1000
        message = bytearray(size)

#        while (time.time() - start_time) < time_window:
#          count += 1000
        try:
          clientSocket.sendall(message)
          count += 1000
        except:
          clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          clientSocket.connect(ServerAddress)
          clientSocket.sendall(message)
          count += 1000

     #   clientSocket.connect(ServerAddress)
      except socket.timeout as e:
        break
#    clientSocket.close()
    array = [2, 10]
    messageEOF = bytearray(array)
    clientSocket.sendall(messageEOF)

    clientSocket.close()   
    megabit = count*0.000008
    count = count/1000
#print("count: {}".format(count))
    rate = megabit/time_window
#print("time_window: {}".format(time_window))
    print('sent = {} KB. rate = {} Mbps'.format(count, rate))

