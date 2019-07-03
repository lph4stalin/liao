"""
程序能一次写完并正常运行的概率很小，基本不超过 1%。总会有各种各样的 bug 需要修正。有的 bug 很简单，看看错误信息就知道，有的 bug 很复杂，我们需要知道出错时，哪些变量的值是正确的，哪些变量的值是错误的，因此，需要一整套调试程序的手段来修复 bug。

第一种方法简单直接粗暴有效，就是用 print() 把可能有问题的变量打印出来看看：
def foo(s):
    n = int(s)
    print('>>> n = {}'.format(n))
    return 10 / n

def main():
    foo('0')

main()

执行后在输出中查找打印的变量：
$ python err.py
>>> n = 0
Traceback (most recent call last):
  ...
ZeroDivisionError: integer division or modulo by zero

用print()最大的坏处是将来还得删掉它，想想程序里到处都是print()，运行结果也会包含很多垃圾信息。所以，我们又有第二种方法。


断言

凡是用 print() 来辅助查看的地方，都可以用断言（assert）来替代。
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')

asset 的意思是，表达式 n != 0 应该是 True，否则，根据程序运行的逻辑，后面的代码肯定会出错。
如果断言失败，assert 语句本身就会抛出 AssertionError：
Traceback (most recent call last):
  ...
AssertionError: n is zero!

程序中如果到处充斥着assert，和print()相比也好不到哪去。不过，启动Python解释器时可以用-O参数来关闭assert。
注意：断言的开关“-O”是英文大写字母O，不是数字0。
关闭后，你可以把所有的assert语句当成pass来看。


logging

把 print() 替换为 logging 是第 3 种方式，和 assert 比，logging 不会抛出错误，而且可以输出到文件：
import logging

s = '0'
n = int(s)
logging.info('n = {}'.format(n))
print(10 / n)

logging.info()就可以输出一段文本。运行，发现除了ZeroDivisionError，没有任何信息。怎么回事？

别急，在import logging之后添加一行配置再试试：

import logging
logging.basicConfig(level=logging.INFO)
看到输出了：

$ python err.py
INFO:root:n = 0
Traceback (most recent call last):
  File "err.py", line 8, in <module>
    print(10 / n)
ZeroDivisionError: division by zero
这就是logging的好处，它允许你指定记录信息的级别，有debug，info，warning，error等几个级别，当我们指定level=INFO时，logging.debug就不起作用了。同理，指定level=WARNING后，debug和info就不起作用了。这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。

logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件。

小结
写程序最痛苦的事情莫过于调试，程序往往会以你意想不到的流程来运行，你期待执行的语句其实根本没有执行，这时候，就需要调试了。

虽然用IDE调试起来比较方便，但是最后你会发现，logging才是终极武器。
"""
