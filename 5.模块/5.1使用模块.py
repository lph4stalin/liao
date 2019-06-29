#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a test module'

__author__ = 'Phil Lee'

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()


"""
第1行和第2行是标准注释，第1行注释可以让这个hello.py文件直接在Unix/Linux/Mac上运行，第2行注释表示.py文件本身使用标准UTF-8编码；
第 4 行是一个字符串，表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释
第 6 行使用 __author__ 变量把作者写进去，这样当你公开源代码后别人就可以瞻仰你的大名；
以上就是Python模块的标准文件模板，当然也可以全部删掉不写，但是，按标准办事肯定没错。

后面开始就是真正的代码部分。

import sys，导入 sys 模块。sys模块有一个argv变量，用list存储了命令行的所有参数。argv至少有一个元素，因为第一个参数永远是该.py文件的名称。

if __name__=='__main__':
    test()
当我们在命令行运行当前模块文件时，Python解释器把一个特殊变量 __name__置为 __main__，而如果在其他地方导入该模块时，__name__ 就不是 __main__，if判断将为False。因此，这种 if 测试可以让一个模块通过命令行运行执行一些额外的代码，最常见的就是运行测试。


作用域

在一个模块中，我们可能会定义很多函数和变量，但有的函数和变量我们希望给别人使用，有的函数和变量我们希望仅仅在模块内部使用。在 Python 中，是通过前缀 _ 实现。

正常的函数和变量名是公开的（public），可以被直接引用，比如：abc，x123，PI等；类似 __xxx__ 这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的 __author__，__name__ 就是特殊变量，模块定义的文档注释也可以用特殊变量 __doc__ 访问，我们自己的变量一般不要用这种变量名；类似 _xxx 和 __xxx 这样的函数或变量就是非公开的（private），不应该被直接引用，比如 __abc，_abc等。
之所以说是“不应该”被直接引用，而不是“不能被直接引用”，是因为 Python 并没有一种方法可以完全限制访问 private 函数或变量，但是，从习惯上来说，我们不应该这样做。

private函数或变量的用途：
def _private_1(name):
    return 'Hello, {}'.format(name)

def _private_2(name):
    return 'Hi, {}'.format(name)

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)
我们在模块里公开 greeting() 函数，而把内部逻辑用 private 函数隐藏起来了，这样，调用 greeting() 函数不用关心内部的 private 函数的细节，这也是一种非常有用的代码封装和抽象的方法，即：
外部不需要引用的函数全部定义成 private，只有外部需要引用的函数才定义为 public。

"""
