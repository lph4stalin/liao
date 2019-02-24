# 由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数


# def now(a):
#     print(a, '2019-2-22')
#
#

# f = now
# f(a)
#
#
# # 函数对象有一个__name__属性，可以拿到函数的名字：
# print('now', now.__name__)
# print('f', f.__name__)


# 现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器(Decorator)”。

# 本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator，可以定义如下：
# 传入一个函数对象（func代表存储函数的地址）作为参数，返回一个函数
def log(func):
    # wrapper可以传入任意个参数和任意的关键字参数
    def wrapper(*args, **kw):
        # 打印出function的名字，再返回function；等价于在function前面增加了print
        print('call {}:'.format(func.__name__))
        return func(*args, **kw)
    return wrapper

# 这么做的好处是外层无法调用wrapper函数


# 示例：输入now函数，输出now函数的结果

@log
def now(a):
    print(a, '2019-02-22')


a = 'hello'
now(a)


# 把@log 放到 now() 函数的定义处，相当于执行了语句：
# now = log(now)

# 由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，预实调用now()将执行新函数，即在log()函数中返回的wrapper()函数。


# wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。在wrapper()函数内，首先打印日志，再紧接着调用原始函数。
