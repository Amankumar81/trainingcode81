#  send msg the command
# the port limit is 0 to 65536
 # ip4 used for 32 nad 64 bit
# ip 6 uesd for 36 bit
# ip_address=192.168.0.182
# port=8888
import socket   # by cli send a msg then use socket library and work as a network communication 

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)    # DGRAM used for send msg mean use as a
ip_address='192.168.231.1'
port=8888
target=(ip_address,port)
message=input("what will send you:")
encript_message=message.encode('ascii')  # encript send msg
s.sendto(encript_message,target)
  # exception use due to if any error occur from user then it handle it
# print("i did not send any msg")
# print("code is run ")