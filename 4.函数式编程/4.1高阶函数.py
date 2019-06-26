# 高阶函数 High-order function

# 变量可以指向函数
from functools import reduce
"""
abs(-10)
# >>> 10
abs
# >>> <built-in function abs>

可见，abs(-10)是函数调用，而abs是函数本身。
要获得函数调用结果，我们可以把结果赋值给变量：
x = abs(-10)
x
# >>> 10

但是，如果把函数本身赋值给变量呢？
f = abs
f
# >>> <built-in function abs>
结论：函数本身也可以赋值给变量，即：变量可以指向函数。
如果一个变量指向了一个函数，那么，可否通过该变量来调用这个函数？
f = abs
f(-10)
# >>> 10
成功！说明变量f已经指向了abs函数本身。直接调用abs()函数和调用变量f()完全相同。
"""

# 函数名也是变量
"""
函数名就是指向函数的变量！对于abs()这个函数，完全可以把函数名abs看成变量，它指向一个可以计算绝对值的函数！
如果把abs指向其他对象，就不能通过abs()调用函数了。

"""


# 传入函数
"""
既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。
"""


# 一个最简单的高阶函数：
# def add(x, y, f):
#     return f(x) + f(y)
# 当我们调用add(-5, 6, abs)时，参数x，y和f分别接收-5,6和abs，根据函数定义，我们可以推导计算过程为：abs(-5) + abs(6) = 5 + 6 = 11


# 一些理解：
# 面向对象：一类有诸多技能的工人，可以让其中一个工人去干一件完整的事情，把解决问题的能力都封装在一类人的神色。
# 面向过程：流水线作业，需要某个工具就取某个工具来用，不关心谁来做，只关心过程
# 函数式编程：调用函数就是取用工具，传入函数的参数可以指明用何种工具
# 高阶函数：函数式编程的具体实现方式。

# 以五子棋为例来说明面向对象和面向过程：
# 面向过程：1.开始游戏；2.黑子先走；3.绘制画面；4.判断输赢；5.轮到白子；6.绘制画面；7.判断输赢；8.返回步骤2；9.输出最后结果
# 面向对象：1.黑白双方；2.棋盘系统，负责绘制画面；3.规则系统，负责判断输赢。第一类对象接收玩家输入，并告知第二类对象棋子布局变化，同时利用第三类对象判断棋局。

# map/reduce
# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。

# 举例，比如有f(x) = x²，要把这个函数作用在一个list[1,2,3,4,5,6,7,8,9]上，就可以用map实现
# def f(x):
#     return x * x
#
#
# r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
# list(r)
# >>>[1, 4, 9, 16, 25, 36, 49, 64, 81]

# 写一个循环也可以实现
# L = []
# for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
#     L.append(f(n))
# print(L)

# map函数实质上就是一个简写

# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果和序列的下一个元素做累积计算，其效果就是：
# reduce(f,[x1, x2, x3, x4)] = f(f(f(x1, x2), x3), x4)


# filter
# Python内建的filter()函数用于过滤序列
# 和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False觉得保留还是丢弃该元素。

# 例如，在一个list中，删掉偶数，只保留奇数，可以这么写：
# def is_odd(n):
#     return n % 2 == 1
#
#
# list(filter(is_odd, [1, 2, 4, 5, 6, 9, 19, 15]))


# sorted
# Python内置的sorted()函数就可以对list进行排序。
# 此外，sorted函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
# sorted([36, 5, -12, -9, -21], key=abs)
# 要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True


# 练习1
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']
def normalize(name):
    return name.capitalize()


# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)


# 练习2
# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(L):
    # def po(x, y): return x * y
    return reduce(lambda x, y: x * y, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


# 练习3
# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
# 把字符串的每一位都转换成数字列表，再用reduce做加工。
def str2float(s):
    digits = {
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '0': 0
    }

    def f(x, y):
        return x * 10 + y

    def char2int(str):
        return digits[str]

    d = s.find('.')
    if d != -1:
        s = s[0:d] + s[d + 1:]
    s = list(map(char2int, s))
    r = reduce(f, s)
    r = r / (10 ** d)
    return r


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')


# 练习4
# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：(返回一个判断，true or false)
def is_palindrome(n):
    L = []
    n = str(n)
    n1 = n[::-1]
    return n == n1


# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')


# 练习5
# 假设我们用一组tuple表示学生名字和成绩，请用sorted()对上述列表分别按名字排序
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[0]


def by_score(t):
    return -t[1]


L2 = sorted(L, key=by_name)
print(L2)
L2 = sorted(L, key=by_score)
print(L2)
