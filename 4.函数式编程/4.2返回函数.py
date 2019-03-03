# 函数作为返回值


# 高阶函数除了可以接收函数作为参数外，还可以把函数作为结果值返回。
# 我们来实现一个可变参数的求和。通常情况下，求和的函数是这样定义的：
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax


# 但是，如果不需要立即求和，而是在后面的代码中，根据需要再计算字母表？可以不返回求和的结果，而是返回求和的函数:
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum


# 当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数：
# f = lazy_sum(1, 3, 5, 7, 9)
# f
# >>> <function lazy_sum.<locals>.sum at 0x101c6ed90>
# 调用函数f时，才真正计算求和的结果
# f()
# 25

# 在这个例子中，我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为"闭包(Closure)"的程序结构拥有极大的威力。

# 请再注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数。


# 闭包！
# 注意到返回的函数在其定义内部引用了局部变量args，所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用，所以，闭包用起来简单，实现起来可不容易。
# 另一个需要注意的是，返回的函数并没有立刻执行，而是直到调用了f()才执行。我们来看一个例子：
def count():
    # 一个空list
    fs = []
    for i in range(1, 4):
        # f函数返回i的平方
        def f():
            return i * i
        # 把f的返回值添加到list中（为什么不直接将i²作为一个变量？）
        # 这里append的是f而不是f的调用
        fs.append(f)
    # 最后返回列表
    return fs


f1, f2, f3 = count()
# 为什么f1，f2，f3返回的是function？
# 因为列表里append的是函数，而不是函数调用的结果
# 这里i的最终状态是3，所以在调用的时候，f1()、f2()、f3()都是9(当调用函数时，函数才会去寻找参数i的值，这时找到的是3)
print(f1(), f2(), f3())

# 如果要引用循环变量，可以再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：


def count():
    def f(j):
        def g():
            return j * j
        return g
    fs = []
    for i in range(1, 4):
        # 虽然列表里保存的还是函数，但是i的值已经被固定下来了。
        fs.append(f(i))
    return fs


# 练习
# 利用闭包返回一个计数器函数，每次调用它返回递增整数：
# 第一次调用返回1，第2次调用返回2
def createCounter():
    f = 0

    def counter():
        nonlocal f
        f = f + 1
        return f
    return counter


# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')


"""
写在最后
闭包实在是太复杂了，真希望能有视频教程学习，不然根本学不会，就算学会了用法，也无法理解其内涵。
"""
