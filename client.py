import socket               # Import socket module

s = socket.socket()         # Create a socket object
s.connect(('localhost', 5000))
z = 'Im Here'
s.sendall(z.encode())    
s.close()                     # Close the socket when done
