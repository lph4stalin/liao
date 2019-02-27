# 高级特性
# 这章比较短，就不做展开了。
# 掌握了Python的数据类型、语句和函数，基本上就可以编写出很多有用的程序了。
# 利用Python的高级特性，可以在完成同样功能的情况下减少代码量。代码量的减少不会减轻机器的负担，但会使代码更易读，对人更友好。
from collections.abc import Iterable

# 3.1切片
# 截取list、tuple、string的方法


# 迭代(iteration)
# for循环
# dict迭代：默认迭代key(for key in dict)，如果要迭代value，可以用 for value in dict.values()，同时迭代key和value，可以用 for k, v in dict.items()
# 字符串也是可迭代对象。


# enumerate函数可以把一个list变成索引-元素对

# 在for循环里可以同时引用两个变量进行循环，例如：
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)


"""
output:
1 1
2 4
3 9
"""


# 3.2列表生成式 List Comprehensions
# Python内置的创建list的生成式
# 例如，生成[1, 4, 9, ..., 100]这样的x²列表，可以用循环：
L = []
for x in range(1, 11):
    L.append(x * x)

# 用列表生成式可以用一行语句替代上面的循环：
[x * x for x in range(1, 11)]

# 二者表达的内容是一样的，后者是Python提供的一种方便的语法。

# for后面还可以加上if判断，或者是使用两层循环，例如
[x * x for x in range(1, 11) if x % 2 == 0]
# output: [4, 6, 36, 64, 100]
[m + n for m in 'ABC' for n in 'XYZ']
# output: ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

# 练习
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str) == True]
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')


# 3.3生成器 generator
# 定义：一边循环一边计算的机制
# 列表生成式：L = [x * x for x in range(10)]
# 生成器：g = (x * x for x in range(10))
# 这时generator保存的是一个算法（函数？），通过next()函数可以不断获取generator的返回值。也可以通过for循环来迭代

# 例子：斐波那契数列
# 输入斐波那契数列的第n项，输出它的值；如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield(b)
        a, b = b, a + b
        n = n + 1
    return 'done'


for n in fib(6):
    print(n)


# 如果将generator和yield理解为一种对象，这个对象的特定是，在循环时内存中只保存当前的元素，动态生成下一个元素。generator对象无法直接print，只能通过for循环一个个打印（迭代）
# 有点像range，range也是一种单独的对象，可以被迭代，本身打印出来只是指向一个内存地址。


# 3.4迭代器
# 可以直接作用于for循环的对象统称为可迭代对象：Iterable。有以下几种：
# 一类是集合数据类型，如list、tuple、dict、set、string
# 一类是generator，包括生成器和带yield的generator function。
# 可以用isinstance()判断一个对象是否是Iterable对象
print(isinstance([], Iterable), isinstance({}, Iterable), isinstance('abc', Iterable),
      isinstance((x for x in range(10)), Iterable), isinstance(100, Iterable))

# 生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，直到最后抛出StopIteration错误表示无法继续返回下一个值了。
# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
# 生成器都是Iterator对象，单list、dict、str虽然是Iterable，却不是Iterator
# Python的Iterator对象表示的是一个数据流，可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，单我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。（理论上生成器只需要有上一个状态和算法，就能够生成下一个状态？）
