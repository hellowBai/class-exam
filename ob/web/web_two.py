import socket
sock = socket.socket()
sock.bind(('127.0.0.1',8800))
sock.listen(5)

while 1:
    print('server waiting')
    conn,addr = sock.accept() #请求
    data = conn.recv(1024) #拿到请求信息
    print("data",data)
   # <h1> Hello luffycity </h1>
    conn.send(b"HTTP/1.1 200 OK\r\n\r\nHello luffycity!")  #与浏览器的通讯，要遵循HTTP协议去发送请求数据，浏览器也会按这种协议进行解析；200是显示状态码，
    conn.close()  #前面为响应首行，后边是响应体，以\r\n两个空格隔开。



"""
打印：
server waiting
data b'GET / HTTP/1.1\r\nHost: 127.0.0.1:8800\r\nConnection: keep-alive\r\nUser-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36\r\nUpgrade-Insecure-Requests: 1\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: zh-CN,zh;q=0.9\r\nCookie: csrftoken=Mrqe5gm2pfaQy6LqXAJDqcWWU3BfTFrB0LMMhAEv2Pi0STKVn95bR6ODrDPZn34j\r\n\r\n'
server waiting
data b'GET /favicon.ico HTTP/1.1\r\nHost: 127.0.0.1:8800\r\nConnection: keep-alive\r\nUser-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36\r\nAccept: image/webp,image/apng,image/*,*/*;q=0.8\r\nReferer: http://127.0.0.1:8800/\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: zh-CN,zh;q=0.9\r\nCookie: csrftoken=Mrqe5gm2pfaQy6LqXAJDqcWWU3BfTFrB0LMMhAEv2Pi0STKVn95bR6ODrDPZn34j\r\n\r\n'
server waiting

"""