import socket
import signal
import sys
import select
import struct

def handler(signum, frame):
    #print( "Bye!" )
    s.close()   # I'm assuming s is your bind/listen socket; replace with correct varname if necessary
    sys.exit(0)

signal.signal(signal.SIGINT, handler)

def send_data(soc, msg):
    for sock in connections:
        if sock is not s and sock is not soc:
            try:
                #msg_length = struct.pack('i', len(msg))
                # know that integer takes 4 bytes, so client should unpack and listen for 4 bytes
                sock.send(msg)
            except:
                #print("closing connection!")
                sock.close()
                connections.remove(sock)

if __name__ == "__main__":
    
    # create a socket FOR INCOMING CONNECTIONS
    RECV_BUFFER = 4096
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # tell the computer on what port to listen to
    s.bind(('', 9999))
    #how many connections (i.e. clients) should the server listen to?
    s.listen(100) 
    
    # keep track of connections, add server socket to list
    connections = [s]

    while True:
        read_sockets, write_socket, error_socket = select.select(connections,[],[]) 
        for sock in read_sockets:
            if sock is s:
                # new connection!
                conn, addr = s.accept()
                connections.append(conn)
            else:
                # we have new data from STDIN...
                #...so let's actually read it!
                try:
                    #print("in the try statement")
                    # packed msg_length is an int - list for 4 bytes
                    msg_len = sock.recv(4, socket.MSG_WAITALL)
                    #print(msg_len)
                    # unpack msg_length to get to actual # of bytes in the entered message
                    # unpacked struct is a list, take 1st element
                    msg_size = struct.unpack('i', msg_len)[0]
                    #print(msg_size)
                    message = sock.recv(msg_size, socket.MSG_WAITALL)
                    #print(message)
                    #leave = "exit"
                    #if(message.lower() == leave)
                    #    print("closing connection!")
                    #    soc.close()
                    #    connections.remove(sock)
                    #else:
                    send_data(sock, msg_len)
                    send_data(sock, message)
                except Exception as ex:
                    #print("in the except statement")
                    #print(ex)
                    send_data(sock, "Client (%s, %s) is offline" %addr)
                    #print "Client (%s, %s) is offline" % addr
                    sock.close()
                    connections.remove(sock)
                    continue      

# close the connection with the other party
#conn.close()
# and stop listening for connections
s.close()