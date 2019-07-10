"""
了解了 HTTP 协议和 HTML 文档，我们其实就明白了一个 Web 应用的本质就是：
    1.浏览器发送一个 HTTP 请求；
    2.服务器收到请求，生成一个 HTML 文档；
    3.服务器把 HTML 文档作为 HTTP 响应的 Body 发送给浏览器；
    4.浏览器收到 HTTP 响应，从 HTTP Body 取出 HTML 文档并显示。
所以，最简单的 Web 应用就是先把 HTML 用文件保存好，用一个现成的 HTTP 服务器软件，接收用户请求，从文件中读取 HTML，返回。Apache、Nginx、Lighttpd 等常见的静态服务器就是干这件事情的。

如果要动态生成 HTML，就需要把上述步骤自己来实现。不过，接受HTTP请求、解析HTTP请求、发送HTTP响应都是苦力活，如果我们自己来写这些底层代码，还没开始写动态HTML呢，就得花个把月去读HTTP规范。
正确的做法是底层代码由专门的服务器软件实现，我们用 Python 专注于生成 HTML 文档。因为我们不希望接触到 TCP 连接、HTTP 原始请求和响应格式，所以，需要一个统一的接口，让我们专心用 Python 编写 Web 业务。
这个接口就是 WSGI：Web Server Gateway Interface

WSGI 接口定义非常简单，它只要求 Web 开发者实现一个函数，就可以响应 HTTP 请求。我们来看一个最简单的Web版本的“Hello, web!”：
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, web!</h1>']
上面的 application() 函数就是符合 WSGI 标准的 HTTP 处理函数，它接收两个参数：
    · environ：一个包含所有 HTTP 请求信息的 dict 对象；
    · start_response：一个发送 HTTP 响应的函数
在application()函数中，调用：

start_response('200 OK', [('Content-Type', 'text/html')])
就发送了HTTP响应的Header，注意Header只能发送一次，也就是只能调用一次start_response()函数。start_response()函数接收两个参数，一个是HTTP响应码，一个是一组list表示的HTTP Header，每个Header用一个包含两个str的tuple表示。

通常情况下，都应该把Content-Type头发送给浏览器。其他很多常用的HTTP Header也应该发送。

然后，函数的返回值b'<h1>Hello, web!</h1>'将作为HTTP响应的Body发送给浏览器。

有了WSGI，我们关心的就是如何从environ这个dict对象拿到HTTP请求信息，然后构造HTML，通过start_response()发送Header，最后返回Body。

整个application()函数本身没有涉及到任何解析HTTP的部分，也就是说，底层代码不需要我们自己编写，我们只负责在更高层次上考虑如何响应请求就可以了。

不过，等等，这个application()函数怎么调用？如果我们自己调用，两个参数environ和start_response我们没法提供，返回的bytes也没法发给浏览器。

所以application()函数必须由WSGI服务器来调用。有很多符合WSGI规范的服务器，我们可以挑选一个来用。但是现在，我们只想尽快测试一下我们编写的application()函数真的可以把HTML输出到浏览器，所以，要赶紧找一个最简单的WSGI服务器，把我们的Web应用程序跑起来。

好消息是Python内置了一个WSGI服务器，这个模块叫wsgiref，它是用纯Python编写的WSGI服务器的参考实现。所谓“参考实现”是指该实现完全符合WSGI标准，但是不考虑任何运行效率，仅供开发和测试使用。


运行 WSGI 服务

我们先编写hello.py，实现Web应用程序的WSGI处理函数：
# hello.py

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, web!</h1>']

然后，再编写一个server.py，负责启动WSGI服务器，加载application()函数：

from wsgiref.simple_server import make_server
# 导入我们自己编写的 application 函数：
from hello import application

# 创建一个服务器，IP 地址为空，端口是 8000，处理函数是 application：
httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')
# 开始监听HTTP请求:
httpd.serve_forever()


小结

无论多么复杂的 Web 应用程序，入口都是一个 WSGI 处理函数。HTTP 请求的所有输入信息都可以通过 environ 获得，HTTP 响应的输出都可以通过 start_response() 加上函数返回值作为 Body。
复杂的 Web 应用程序。光靠一个 WSGI 函数来处理还是太底层了，我们需要在 WSGI 之上再抽象出 Web 框架，进一步简化 Web 开发。


"""
