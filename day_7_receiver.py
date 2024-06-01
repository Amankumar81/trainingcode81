
#   receiver address 
import socket 
# try:
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip_address='192.168.0.182'
port=8888
target=(ip_address,port)
s.bind(target)  # bind data in s 
while True:
    message=s.recvfrom(120) # receive from limit 120 
    print(message)
    data=message[0]
    data='\n'
    print(data.encode('ascii'))
# ecept Exception as e:
#    print(" hello i have sent the msg") 
         
