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
# def log(func):
#     # wrapper可以传入任意个参数和任意的关键字参数
#     def wrapper(*args, **kw):
#         # 打印出function的名字，再返回function；等价于在function前面增加了print
#         print('call {}:'.format(func.__name__))
#         return func(*args, **kw)
#     return wrapper

# 这么做的好处是外层无法调用wrapper函数


# 示例：输入now函数，输出now函数的结果

# @log
# def now(a):
#     print(a, '2019-02-22')
#
#
# a = 'hello'
# now(a)


# 把@log 放到 now() 函数的定义处，相当于执行了语句：
# now = log(now)，@log会自动调用接下来的函数，并将其函数名作为参数传入

# 由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，预实调用now()将执行新函数，即在log()函数中返回的wrapper()函数。


# wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。在wrapper()函数内，首先打印日志，再紧接着调用原始函数。

# 如果decorator需要传入参数，那就需要再编写一个返回decorator的高阶函数，写出来会更复杂，比如，要自定义log的文本。
# def log(text):
#     def decorator(func):
#         def wrapper(*args, **kw):
#             print('call {} {}:'.format(text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator
#
#
# @log('我是你爸爸')
# def now():
#     print('2019-02-23')
#
#
# now()


# 上面的修饰器等价于now = log('我是你爸爸')(now)
'''
首先执行log('我是你爸爸')，返回decorator函数，再调用返回的函数，参数是now函数，返回值最终是wrapper函数。
第一次调用，log('text')，返回decorator函数，第二次调用decorator，传入参数now，返回wrapper，最后调用wrapper，传入参数是（text和now的参数？？？why）最终返回now的参数调用
'''

# 经过修饰器，now最终被替换成了wrapper函数，通过这个函数来执行now的功能
# print(now.__name__)

# 因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性也复制到wrapper函数中，否则，有些依赖函数签名的代码会出错。

# 不需要编写wrapper.__name__ = func.__name__，Python内置的functiontools.wraps就是就是干这个事的，所以，一个完整的decorator的写法如下：
import functools


def log(func):
    # 目前暂时不关注具体实现方式，只需要知道这个修饰器可以修改func的一些属性
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call {} {}:'.format(func.__name__))
        return func(*args, **kw)
    return wrapper

# 或者针对带参数的decorator
