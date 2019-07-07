"""
datetime 是 Python 处理日期和时间的标准库。

获取当前日期和时间
我们先看如何获取当前日期和时间：
from datetime import datetime
now = datetime.now()
print(now)
print(type(now))

注意到 datetime 是模块，datetime 模块还包含一个 datetime 类，通过 from datetime import datetime 导入的才是 datetime 这个类

如果仅导入 import datetime，则必须引用全名 datetime.datetime
datetime.now() 返回当前日期和时间，其类型是 datetime


collections

collections 是 Python 内建的一个集合模块，提供了许多有用的集合类。


"""
