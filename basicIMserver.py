import argparse
import socket

# create a socket FOR INCOMING CONNECTIONS
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# tell the computer on what port to listen to
s.bind(('', 9999))

s.listen(1)

# wait until we ACCEPT a connection from another host
# and return a socket ("conn") we can use to talk to it
conn, addr = s.accept()

# if we got here, then someone is talking to us.
# (we could accept another connection by calling
# s.accept() again, but we won't do that in this example)

print('Connected by', addr)

# infinite loop time!
while True:    
# receive UP TO 1024 bytes    
    data = conn.recv(1024)    
    if not data: break   # if data is None, then connection is closed    
    print( 'We got something:\n\n%s' % data.decode('utf-8') ),
    
# close the connection with the other partyconn.close()
# and stop listening for connections
s.close()