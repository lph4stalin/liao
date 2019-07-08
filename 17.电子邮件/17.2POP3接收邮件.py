"""
SMTP 用于发送邮件，收取邮件则需要编写一个 MUA 作为客户端，从 MDA 把邮件获取到用户的电脑或者手机上。收取邮件最常用的协议是 POP 协议，目前版本号是 3，俗称 POP3。
Python 内置一个 poplib 模块，实现了 POP3 协议，可以直接用来收邮件。
注意到 POP3 协议收取的不是一个已经可以阅读的邮件本身，而是邮件的原始文本，这和 SMTP 协议很像，SMTP 发送的也是经过编码后的一大段文本。
要把 POP3 收取的文本变成可以阅读的邮件，还需要用 email 模块提供的各种类来解析原始文本，变成可阅读的邮件对象。

所以，收取邮件分两步：
第一步：用 poplib 把邮件的原始文本下载到本地；
第二步：用 email 解析原始文本，还原为邮件对象。


通过 POP3 下载邮件

POP3 协议本身很简单，以下面代码为例，我们来获取最新的一封邮件内容：
import poplib
# 这里 Parser 函数需要 import，原文并没有写
from email.parser import Parser


# 输入邮件地址，口令和 POP3 服务器地址：
email = 'lph4stalin@tom.com'
password = 'lipeihua@'
pop3_server = 'pop.tom.com'

# 连接到 POP3 服务器
server = poplib.POP3(pop3_server)
# 可以打开或关闭调试信息
server.set_debuglevel(1)
# 可选：打印 POP3 服务器的欢迎文字
print(server.getwelcome().decode('utf-8'))

# 身份认证
server.user(email)
server.pass_(password)

# stat() 返回邮件数量和占用空间：
print('Messages: {}. Size: {}'.format(server.stat())
# list() 返回所有邮件的编号
resp, mails, octets = server.list()
# 可以查看返回的裂变类似[b'1 82923',b'2 2184', ...]
print(mails)

# 获取最新一封邮件，注意索引号从 1 开始：
index = len(mails)
resp, lines, octets = server.retr(index)

# lines 存储了邮件的原始文本的每一行
# 可以获得整个邮件的原始文本
msg_content = b'\r\n'.join(lines).decode('utf-8')
# 稍后解析出邮件
msg = Parser().parsestr(msg_content)

# 可以根据邮件索引号直接从服务器删除邮件
# server.dele(index)
# 关闭连接
server.quit()

用POP3获取邮件其实很简单，要获取所有邮件，只需要循环使用retr()把每一封邮件内容拿到即可。真正麻烦的是把邮件的原始内容解析为可以阅读的邮件对象。


解析邮件

解析邮件的过程和上一节构造邮件正好相反，因此，先导入必要的模块：
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

import poplib


只需要一行代码就可以把邮件内容解析为 Message 对象：
msg = Parser().parsestr(msg_content)
但是这个 Message 对象本身可能是一个 MIMEMutipart 对象，即包含嵌套的其他 MIMEBase 对象，嵌套可能还不止一层。
所以我们要递归地打印出 Message 对象的层次结构：
省略



小结

用 Python 的 poplib 模块收取邮件分两步：第一步是用 POP3 协议把邮件获取到本地，第二步是用 email 模块把原始邮件解析为 Message 对象，然后，用适当的形式把邮件内容展示给用户即可。
"""
