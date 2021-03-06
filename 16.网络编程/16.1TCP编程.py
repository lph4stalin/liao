"""
Socket 是网络编程的一个抽象概念。通常我们用一个 Socket 表示”打开了一个网络链接“，而打开一个 Socket 需要知道目标计算机的 IP 地址和端口号，再指定协议类型即可。

客户端

大多数连接都是可靠的 TCP 连接。创建 TCP 连接时，主动发起连接的叫客户端，被动响应连接的叫服务器。
举个例子，当我们在浏览器访问新浪时，我们自己的计算机就是客户端，浏览器会主动向新浪的服务器发起连接。如果一切顺利，新浪的服务器接受了我们的连接，一个 TCP 连接就建立起来的，后面的通信就是发送网页内容了。
所以，我们要创建一个基于 TCP 连接的 Socket，可以这样做：
import socket
# 创建一个 socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接
s.connect(('www.sina.com.cn', 80))
创建 Socket 时，AF_INET 指定使用 IPv4 协议，如果要用更新的 IPv6，就指定为 AF_INET6。SOCK_STREAM 指定使用面向流的 TCP 协议，这样，一个 Socket 对象就创建成功，但是还没有建立连接。
客户端要主动发起 TCP 连接，必须知道服务器的 IP 地址和端口号。新浪网站的 IP 地址可以用域名 ‘www.sina.com.cn’ 自动地转换到 IP 地址，但是怎么知道新浪服务器的端口号呢？

答案是作为服务器，提供什么样的服务，端口号就必须固定下来。由于我们想要访问网页，因此新浪提供网页服务的服务器必须把端口号固定在 80 端口（https固定在443），因为 80 端口是 Web 服务的标准端口。其他服务都有对应的标准端口号，例如 SMTP 服务是 25 端口，FTP 服务是 21 端口，等等。端口号小于 1024 的是 Internet 标准服务的端口，端口号大于 1024 的，可以任意使用。

因此，我们连接新浪服务器的代码如下：
s.connect(('www.sina.com.cn', 80))
注意参数是一个tuple，包含地址和端口号。

建立 TCP 连接后，我们就可以向新浪服务器发送请求，要求返回首页的内容：
# 发送数据
s.send(b'GET / HTTP/1.1\r\n\Host: wwww.sina.com.cn\r\nConnection: close\r\n\r\n')

TCP 连接创建的是双向通道，双方都可以同时给对方发数据。但是谁先发，谁后发，怎么协调，要根据具体的协议来决定。例如，HTTP 协议规定客户端必须先发请求给服务器，服务器收到后才发数据给客户端。

发送的文本格式必须符合 HTTP 标准，如果格式没问题，接下来就可以接收新浪服务器返回的数据了：
# 接收数据：
buffer = []
while True:
    # 每次最多接收1k字节
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
接收数据时，调用 recv(max) 方法，一次最多接收指定的字节数，因此，在一个 while 循环中反复接收，直到 recv() 返回空数据，表示接收完毕，退出循环。

当我们接受完数据后，调用 close() 方法关闭 Socket，这样，一次完整的网络通信就结束了：
# 关闭连接：
s.close()
接收到的数据包括 HTTP 头和网页本身，我们只需要把 HTTP 头和网页分离一下，把 HTTP 头打印出来，网页内容保存到文件：
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
# 把接收的数据写入文件：
with open('sina.html','wb') as f:
    f.write(html)


服务器

和客户端编程相比，服务器编程就要复杂一些。

服务器进程首先要绑定一个端口并监听来自其他客户端的连接。如果某个客户端连接过来了，服务器就与该客户端建立 Socket 连接，随后的通信就靠这个 Socket 连接了。
所以，服务器会打开固定端口（比如80）监听，每来一个客户端连接，就创建该 Socket 连接。由于服务器会有大量来自客户端的连接，所以，服务器要能够区分一个 Socket 连接是和哪个客户端绑定的。一个 Socket 依赖 4 项：服务器地址、服务器端口、客户端地址、客户端端口来确定唯一的一个 Socket。

但是服务器还需要同时响应多个客户端的请求，所以，每个连接都需要一个新的进程或者新的线程来处理，否则，服务器一次就只能服务一个客户端了。

我们来编写一个简单的服务器程序，它接收客户端连接，把客户端发过来的字符串加上 Hello 再发回去。
首先，创建一个基于 IPv4 和 TCP 协议的 Socket：
s = socket.socket()
然后，我们要绑定监听的地址和端口。服务器可能有多块网卡，可以绑定到某一块网卡的 IP 地址上，也可以用 0.0.0.0 绑定到所有的网络地址，还可以用 127.0.0.1 绑定到本机地址。127.0.0.1 是一个特殊的 IP 地址，表示本机地址，如果绑定到这个地址，客户端必须同时在本机运行才能连接，也就是说，外部的计算机无法连接进来。
端口号需要预先指定。因为我们写的这个服务不是标准服务，所以用9999这个端口号。请注意，小于 1024 的端口号必须要有管理员权限才能绑定：
# 监听端口：
s.bind(('127.0.0.1', 9999

紧接着，调用 listen() 方法开始监听端口，传入的参数指定等待连接的最大数量：
s.listen(5)
print('Waiting for connection')

接下来，服务器通过一个永久循环来接受来自客户端的连接，accept() 会等待并返回一个客户端的连接：
while True:
    # 接受一个新连接
    sock, addr = s.accept()
    # 创建新线程来处理 TCP 连接
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
每个连接都必须创建新线程（或者进程）来处理，否则，单线程在处理连接的过程中，无法接受其他客户端的连接：
def tcplink(sock, addr)
    prnt('Accept new connection from {}...'.format(addr))
    sock.send(b'Welcome')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, {}!'.format(data.decode('utf-8')).endode('utf-8'))
    sock.close()
    print('Connection from {} closed.'.format(addr))
连接建立后，服务器首先发一条欢迎消息，然后等待客户端数据，并加上 Hello 再发送给客户端。如果客户端发送了 exit 字符串，就直接关闭连接。

要测试这个服务器程序，我们还需要编写一个客户端程序：


小结

用 TCP 协议进行 Socket 编程在 Python 中十分简单，对于客户端，要主动连接服务器的 IP 和指定端口，对于服务器，要首先监听指定端口，然后，对每一个新的连接，创建一个线程或进程来处理。通常，服务器程序会无限运行下去。
同一个端口，被一个 Socket 绑定了以后，就不能被别的 Socket 绑定了。
"""
