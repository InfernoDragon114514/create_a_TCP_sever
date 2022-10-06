#coding:utf-8
import socket
host='你的主机IP' #主机IP
port=8080        #默认端口号
web=socket.socket() #创建socket对象
web.bind((host,port))#绑定端口
web.listen(1)   #设置最多连接数
while True:
    conn,addr=web.accept
    data=conn.recv(1024)
    print(data)
    conn.sendall(b'http/1.1 200 OK\r\n\r\nHelloWorld")
    conn.close()
