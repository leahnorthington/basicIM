import argparse
import socket
import struct
import sys
import select
import string
import basicIM_pb2

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # add first required argument, which can either be specified
    # via -s or --server. Store the result in a variable called servername
    parser.add_argument('-s', '--server', dest='server', help='hostname of machine running BasicIM server', required=True)
    
    # add second required argument, which can either be specified
    # via -n or --nickname. Store the result in a variable called nickname
    parser.add_argument('-n', '--nickname', dest='nickname', help='alias chosen by user', required=True)

    args = parser.parse_args()    

    # create a socket for talking with another machine
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect to the host name specified by -s on port 9999 
    try:
        s.connect( (args.server,9999) )
    except:
        #print("Unable to connect")
        sys.exit()

    #print("Connected to server! Start sending messages now...")

    #name = args.nickname

    while True:
        socket_list = [sys.stdin, s]
        read_sockets, write_socket, error_socket = select.select(socket_list,[],[]) 
        for sock in read_sockets:
            # data coming from another connection
            if sock is s:
                msg_len = sock.recv(4, socket.MSG_WAITALL)
                #print("packed message length")
                #print(msg_len)
                msg_size = struct.unpack('i', msg_len)[0]
                #print("unpacked message length")
                #print(msg_size)
                message = basicIM_pb2.basicIMmessage()
                #message = sock.recv(msg_size, socket.MSG_WAITALL) # gives serialized protobuf
                message.ParseFromString(sock.recv(msg_size, socket.MSG_WAITALL)) # gives int num of bytes of protobuf
                print( "%s: %s\n" % (message.name, message.contents), flush=True )
                #print("serialized message")
                #print(serialized_message)
                #print(message.ParseFromString(sock.recv(msg_size, socket.MSG_WAITALL)))
                #print(message.name) # prints out num bytes
            # this user has entered a message
            else:
                message = basicIM_pb2.basicIMmessage()
                message.name = args.nickname
                message.contents = sys.stdin.readline()
                # know that integer takes 4 bytes, so server should unpack and listen for 4 bytes
                serialized = message.SerializeToString()   # convert to bytes
                #print("seralized message")
                #print(serialized)
                msg_length = struct.pack('i', len(serialized))
                #print("message length")
                #print(msg_length)
                s.send(msg_length)
                s.send(serialized)

    