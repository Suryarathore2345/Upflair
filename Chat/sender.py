import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip_add = "192.168.217.75"
port=1234
complete = (ip_add,port)
message = input("Hello Somya the vlogger !!")
encode_msg=message.encode('ascii')
s.sendto(encode_msg,complete)
