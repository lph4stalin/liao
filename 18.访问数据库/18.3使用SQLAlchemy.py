"""
使用SQLAlchemy

数据库是一个二维表，包含多行多列。把一个表的内容用 Python 的数据结构表示出来的话，可以用一个 list 表示多行，list 的每一个元素是 tuple，表示一行记录，比如，包含 id 和 name 的 user 表：
[
('1', 'Michael')
('2', 'Bob')
('3', 'Adam')
]
Python 的 DB-API 返回的数据结构就是像上面这样表示的。
但是用 tuple 表示一行很难看出表的结构。如果把一个 tuple 用 class 实例来表示，就可以更容易地看出表的结构来：
class User(object):
    def __init__(self, id, name):
        self.id = id
        self.name = dirname
[
User('1', 'Michael')
User('2', 'Bob')
User('3', 'Adam')
]
这就是传说中的 ORM 技术：Object-Relational Mapping，把关系数据库的表结构映射到对象上。

但是由谁来做这个转换呢？所以 ORM 框架应运而生。
在 Python 中，最有名的 ORM 框架是 SQLAlchemy。

"""
