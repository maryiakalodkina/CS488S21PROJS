import socket
import sys
import time

if sys.argv[1] == "-s":
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
    Serv_count = 0 #in Bytes
    connection_socket, addr = serverSocket.accept()  #move to while-lo$
    start_time2 = time.time()

    while 1:
        #Receiving message from client
      message = connection_socket.recv(1000)

      #by sending ascii 69 ('E') we notify the Server that Client closed its socket
      #so the Server will also shut down      
      if message[0] == 69:
        #connection_socket.close()
        stop_time2 = time.time()-start_time2
        connection_socket.close()
        break
      Serv_count+=1000

#    print('Count: {} and StopTime: {}'.format(Scount, stop_time2))
    serverSocket.close()

    megabit = Serv_count*0.000008
    Serv_count = Serv_count/1000 #now it's in KB
    rate = megabit/stop_time2

    print('received = {} KB. rate = {} Mbps'.format(Serv_count, rate))

else:

    if len(sys.argv) > 4 or len(sys.argv) < 4:
      print('Error: missing or additional arguments')
      sys.exit(1)
    if int(sys.argv[2]) < 1024 or int(sys.argv[2]) > 65535:
      print('Error: port number must be in the range 1024 to 65535')
      sys.exit(1)        

     #Create server
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
 
      size = 1000 
      message = bytearray(size)

      clientSocket.sendall(message)
      count += 1000
        
    messageEOF = 'E'
    clientSocket.send(messageEOF.encode('ascii'))

    megabit = count*0.000008
    count = count/1000
    rate = megabit/time_window

    print('sent = {} KB. rate = {} Mbps'.format(count, rate))

