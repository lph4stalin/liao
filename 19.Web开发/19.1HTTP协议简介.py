"""
在 Web 应用中，服务器把网页传给浏览器，实际上就是把网页的 HTML 代码发送给浏览器，让浏览器显示出来。而浏览器和服务器之间的传输协议是 HTTP，所以：
    · HTML 是一种用来定义网页的文本，会 HTML，就可以编写网页
    · HTTP 是在网络上传输 HTML 的协议，用于浏览器和服务器的通信

例：www.sina.com.cn 请求

最主要的头两行分析如下，第一行：
GET / HTTP/1.1
GET 表示一个读取请求，将从服务器获得网页数据，/ 表示 URL 的路径，URL 总是以 / 开头，/ 就表示首页，最后的 HTTP/1.1 知识采用的 HTTP 协议版本是 1.1。目前 HTTP 协议的版本就是 1.1，但是大部分服务器也支持 1.0 版本，主要区别在于 1.1 版本允许多个 HTTP 请求复用一个 TCP 连接，以加快传输速度。
从第二行开始，每一行都类似于 XXX：abcdefg：
Host: www.sina.com.cn
表示请求的域名是 www.sina.com.cn。如果一台服务器有多个网站，服务器就需要通过 Host 来区分浏览器请求的是哪个网站。


Response Headers

HTTP/1.1 200 OK
协议版本，200表示一个成功的响应，后面的 OK 是说明。失败的响应有 404 Not Found：网页不存在，500 Internal Server Error：服务器内部出错，等等。
Content-Type: text/html
Content-Type 知识响应的内容，这里是 text/html 表示的 HTML 网页。请注意，浏览器就是依靠 Content-Type 来判断响应的内容是网页还是图片，是视频还是音乐。浏览器并不靠 URL 来判断响应内容。

HTTP 响应的 Body 就是 HTML 源码。

当浏览器读取到新浪首页的HTML源码后，它会解析HTML，显示页面，然后，根据HTML里面的各种链接，再发送HTTP请求给新浪服务器，拿到相应的图片、视频、Flash、JavaScript脚本、CSS等各种资源，最终显示出一个完整的页面。所以我们在Network下面能看到很多额外的HTTP请求。


HTTP 请求
HTTP 请求的流程总结如下：
步骤1：浏览器首先向服务器发送 HTTP 请求，请求包括：
方法：GET/POST，路径，域名
步骤2：服务器向浏览器返回 HTTP 响应，响应包括：
响应代码：200表示成功，3xx表示重定向，4xx表示客户端发送的请求有误，5xx表示服务器端处理时发生了错误；
响应类型：由 Content-Type 指定
通常服务器的 HTTP 响应会携带内容，也就是有一个 Body，网页的源码就在 Body 中。
步骤3：如果浏览器还需要继续向服务器请求其他资源，比如图片，就再次发出 HTTP 请求，重复步骤 1、2。

Web 采用的 HTTP 协议采用了非常简单的请求-响应模式，从而大大简化了开发。当我们编写一个页面时，我们只需要在 HTTP 响应中把 HTML 发送出去，不需要考虑如何附带图片、视频等，浏览器如果需要请求图片和视频，它会发送另一个 HTTP 请求，因此，一个 HTTP 请求只处理一个资源。

HTTP 协议同时具备极强的扩展性，虽然浏览器请求的是新浪的首页，但是新浪在 HTML 中可以链入其他服务器的资源，从而将请求压力分散到各个服务器上，并且，一个站点可以链接到其他站点，无数个站点互相链接起来，就形成了 World Wide Web。


HTTP 格式

每个 HTTP 请求和响应都遵循相同的格式，一个 HTTP 包含 Header 和 Body 两部分，其中 Body 是可选的。
HTTP 协议是一种文本协议，所以，它的格式也非常简单。


HTTP GET 请求的格式：
GET /path HTTP/1.1
Header1: Value1
Header2: Value2
Header3: Value3

body data goes here...
当连续遇到两个\r\n时，Header 部分结束，后面的数据全部是 Body。


HTTP 响应的格式：
HTTP/1.1 200 OK
Header1: Value1
Header2: Value2
Header3: Value3

body data goes here...
HTTP 响应如果包含 body，也是通过 \r\n\r\n 来分隔的。请再次注意，Body 的数据类型由 Content-Type 来确定，如果是网页，Body 就是文本，如果是图片，Body 就是图片的二进制数据。

当存在Content-Encoding时，Body数据是被压缩的，最常见的压缩方式是gzip，所以，看到Content-Encoding: gzip时，需要将Body数据先解压缩，才能得到真正的数据。压缩的目的在于减少Body的大小，加快网络传输。
"""
