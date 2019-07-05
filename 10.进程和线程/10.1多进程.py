"""
要让 Python 程序实现多进程（multiprocessing），我们先了解操作系统相关知识。

Unix/Linux 操作系统提供了一个 fork() 系统调用，它非常特殊。普通的函数调用，调用一次，返回一次，但是 fork() 调用一次，返回两次，因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后分别在父进程和子进程内返回。

子进程永远返回 0，而父进程返回子进程的 ID。这样做的理由是，一个父进程可以 fork 出很多子进程，所以父进程要几下每个子进程的 ID，而子进程只需要调用 getppid() 就可以拿到父进程的 ID。

Python 的 os 模块封装了常见的系统调用，其中就包括 fork，可以在 Python 程序汇总轻松创建子进程：
import os
print('Process ({}) start...' .format(os.getpid()))
# Only works on Unix/Linux/Mac:
pid = os.fork()
if pid == 0:
    print('I am child process ({}) and my parent is {}.'.format((os.getpid(), os.getppid())))
else:
    print('I ({}) just created a child process ({}).'.format(os.getpid(), pid))

有了 fork 调用，一个进程在接到新任务时就可以复制出一个子进程来处理新任务，常见的 Apache 服务器就是由父进程监听端口，每当有新的 http 请求时，就 fork 出子进程来处理新的 http 请求。

multiprocessing
如果你打算编写多进程的服务程序，Unix/Linux 无疑是正确的选择。由于 Windows 没有 fork 调用，难道在 Windows 上没法用 Python 编写多进程的程序？

由于 Python 是跨平台的，自然也应该提供一个跨平台的多进程支持。multiprocessing 模块就是跨平台版本的多进程模块。

multiprocessing 模块提供了一个 Process 类来代表一个进程对象，下面的例子演示了启动一个子进程并等待其结束：
from multiprocessing import Process
import os

def run_proc(name):
    print('Run child process {}({})...'.format(name, os.getpid()))

if __name__ == '__main__':
    print('Parent process {}.'.format(os.getpid()))
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')

创建子进程时，只需要传入一个执行函数和函数的参数，创建一个 Process 实例，用 start() 方法启动，这样创建进程比 fork() 还要简单。
join() 方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。

Pool
如果要启动大量的子进程，可以用进程池的方式批量创建子进程：
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
        print('Run task {}({})...'.format(name, os.getpid()))
        start = time.time()
        time.sleep(random.random() * 3)
        end = time.time()
        pritn('Task {} runs {} seconds.'.format(name, (end - start)))

if __name__=='__main__':
    print('Parent process {}.'.format(os.getpid()))
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')

代码解读：
对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。

请注意输出的结果，task 0，1，2，3 是立刻执行的，而 task 4 要等待前面某个 task 完成后才执行，这是因为 Pool 的默认大小在我的电脑上是 4，因此，最多同时执行 4 个进程。这是 Pool 有意设计的限制，并不是操作系统的限制。
Pool 的默认大小是 CPU 的核数。

子进程
很多时候，子进程并不是自身，而是一个外部进程。我们创建了子进程后，还需要控制子进程的输入和输出。

进程间通信



小结

在Unix/Linux下，可以使用fork()调用实现多进程。

要实现跨平台的多进程，可以使用multiprocessing模块。

进程间通信是通过Queue、Pipes等实现的。
"""
