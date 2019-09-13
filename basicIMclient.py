import argparse
import socket

def main():
    parser = argparse.ArgumentParser()

    # add first required argument, which can either be specified
    # via -s or --server. Store the result in a variable called servername
    parser.add_argument('-s', '--server', dest='servername', help='hostname of machine running BasicIM server', required=True)
    
    # add second required argument, which can either be specified
    # via -n or --nickname. Store the result in a variable called nickname
    parser.add_argument('-n', '--nickname', dest='nickname', help='alias chosen by user', required=True)

    args = parser.parse_args()    

    # create a socket for talking with another machine
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect to the host name specified by -s on port 9999 
    s.connect( (args.server,9999) )
    # let's send something
    for i in range(0,10):    
        s.send(b'hello world!\n')
    # close the connections.close()


#The client should first connect to the BasicIM server, which should already be running (more on the server below) and listening 
#for incoming connections on TCP port 9999.  Once connected, BasicIM should read from standard input (essentially, the keyboard) 
#and send all inputted text to the BasicIM server (which you'll also write).  It should also receive messages, which are serialized 
#with Google Protocol Buffers (Links to an external site.) -- thus, your program should deserialize these messages.  
#BasicIM messages, which are serialized with Google Protocol Buffers, consist of:
        #the nickname of the sender
        #the contents of the instant message
#Note that in BasicIM, all messages are "broadcast", meaning that if one client sends a message, all other online clients should 
#receive that message.  There are no direct messages in BasicIM.

#When your BasicIM client receives a message from the server, it should deserialize it to discern the nickname of the sender and 
#the contents of the instant message.  It should then print out (i.e., send to standard output) the following:
        #nickname: message 
#For example, if the user with the nickname "CoolMicah" typed a message, "Wow, COSC435 is REALLY great!", then all other BasicIM 
#clients should output:
        #CoolMicah: Wow, COSC435 is REALLY great!
        
if __name__ == '__main__':    
        main()