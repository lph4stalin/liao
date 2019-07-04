"""
如果我们要操作文件、目录，可以在命令行下面输入操作系统提供的各种命令来完成。比如 dir、cp 等命令。

如果要在 Python 程序中执行这些目录和文件的操作怎么办？其实操作系统提供的命令只是简单地调用了操作系统提供的接口函数，Python 内置的 os 模块也可以直接调用操作系统提供的接口函数。

打开 Python 交互式命令行，我们来看看如何使用 os 模块的基本功能：
import os
os.name # 操作系统类型
>>> 'nt'
如果是 posix，说明系统是 Linux、Unix 或 Mac OS X，如果是 nt，就是 Windows 系统。

要获取详细的系统信息，可以调用 uname() 函数：
os.uname()
注意uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的。


环境变量

在操作系统中定义的环境变量，全部保存在 os.environ 这个变量中，可以直接查看：


操作文件和目录

操作文件和目录的函数一部分放在 os 模块中，一部分放在 os.path 模块中，这一点要注意一下。查看、创建和删除目录可以这么调用：
# 查看当前目录的绝对路径
os.path.abspath('.')
>>> 'C:\\'
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来
os.path.join('/Users/michael', 'testdir')
# 然后创建一个目录
os.mkdir('/Users/michael/testdir')
# 删掉一个目录
os.rmdir('/Users/michael/testdir')
把两个路径合成一个时，不要直接拼接字符串，而要通过 os.path.join() 函数，这样可以正确处理不同操作系统的路径分隔符。在Linux/Unix/Mac下，os.path.join()返回这样的字符串：
part-1/part-2
而Windows下会返回这样的字符串：
part-1\part-2

同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过 os.path.split() 函数，这样可以把一个路径拆分成两部分，最后一部分总是最后级别的目录或文件。
os.path.splitext() 可以直接让你得到文件扩展名，很多时候非常方便。

这些合并、拆分路径的函数并不要求目录和文件都要真实存在，它们只对字符串进行操作。

文件操作使用下面的函数。假定当前目录下有一个 test.txt 文件：
# 对文件重命名
os.rename('test.txt', 'test.py')
# 删掉文件
os.remove('test.py')

但是复制文件的函数 os 模块中不存在。原因是复制文件并非由操作系统提供的系统调用。理论上讲，我们通过上一节的读写文件就可以完成文件复制，只不过要多写很多代码。
幸运的是 shutil 模块提供了 copyfile() 的函数，你还可以在 shutil 模块中找到很多实用函数，它们可以看做 os 模块的补充。

最后看看如何利用 Python 的特性来过滤文件。比如我们要列出当前目录下的所有目录，只需要一行代码：
[x for x in os.listdir('.') if os.path.isdir(x)]
要列出所有的.py文件，也只需一行代码：
[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']


小结

Python 的 os 模块封装了操作系统的目录和文件操作，要注意这些函数有的在 os 模块中，有的在 os.path 模块中。
"""
