"""
使用 SQLite

SQLite 是一种嵌入式数据库，它的数据库就是一个文件。由于 SQLite 本身是 C 写的，而且体积很小，所以，经常被集成到各种应用程序中，甚至在 iOS 和 Android 的 App 中都可以集成。

Python 就内置了 SQLite3，所以，在 Python 中使用 SQLite，不需要安装任何东西，直接使用。

在使用 SQLite 前，我们要先搞清楚几个概念：
表是数据库中存放关系数据的集合，一个数据库里通常都包含多个表，比如学生的表，班级的表，学校的表，等等。表和表之间通过外键关联。
要操作关系数据库，首先需要连接到数据库，一个数据库连接称为 Connection；
连接到数据库后，需要打开游标，称之为 Cursor，通过 Cursor 执行 SQL 语句，然后，获得执行结果。

Python 定义了一套操作数据库的 API 接口，任何数据库要连接到 Python，只需要提供符合 Python标准的数据库驱动即可。

由于 SQLite 的驱动内置在 Python 标准库中，所以我们可以直接来操作 SQLite 数据库。

我们在 Python 交互式命令行实践一下：
import sqlite3
# 连接到 SQLite 数据库
# 数据库文件是 test.db
# 如果文件不存在，会自动在当前目录创建
conn = sqlite3.connect('test.db')
# 创建一个 Cursor：
cursor = conn.cursor()
# 执行一条 SQL 语句，创建 user 表：
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 继续执行一条 SQL 语句，插入一条记录
cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
# 通过rowcount获得插入的行数:
cursor.rowcount
# 关闭Cursor:
cursor.close()
# 提交事务:
conn.commit()
# 关闭Connection:
conn.close()

conn = sqlite3.connect('test.db')
cursor = conn.cursor()
# 执行查询语句:
cursor.execute('select * from user where id=?', ('1',))
# 获得查询结果集:
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()


使用Python的DB-API时，只要搞清楚Connection和Cursor对象，打开后一定记得关闭，就可以放心地使用。

使用Cursor对象执行insert，update，delete语句时，执行结果由rowcount返回影响的行数，就可以拿到执行结果。

使用Cursor对象执行select语句时，通过featchall()可以拿到结果集。结果集是一个list，每个元素都是一个tuple，对应一行记录。

如果SQL语句带有参数，那么需要把参数按照位置传递给execute()方法，有几个?占位符就必须对应几个参数，例如：

cursor.execute('select * from user where name=? and pwd=?', ('abc', 'password'))
SQLite支持常见的标准SQL语句以及几种常见的数据类型。具体文档请参阅SQLite官方网站。

小结

在 Python 中操作数据库时，要先导入数据库对应的驱动，然后，通过 Connection 对象和 Cursor 对象操作数据。
要确保打开的 Connection 对象和 Cursor 对象都正确地被关闭，否则，资源就会泄露。
如何才能确保出错的情况下也关闭掉 Connection 对象 和 Cursor 对象呢？ try:...except:...finally:...

执行数据库操作
 n=cursor.execute(sql,param)

练习
请编写函数，在Sqlite中根据分数段查找指定的名字：

# -*- coding: utf-8 -*-

import os, sqlite3

db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)

# 初始数据:
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()

def get_score_in(low, high):
    ' 返回指定分数区间的名字，按分数从低到高排序 '
----
    pass
----
# 测试:
assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)

print('Pass')
"""
"""
练习
请编写函数，在Sqlite中根据分数段查找指定的名字：
"""

# -*- coding: utf-8 -*-

import os, sqlite3

# 输出 'test.db' 所在的完整路径
db_file = os.path.join(os.path.dirname(__file__), 'test.db')
print('db_file', db_file)
# 判断路径是否为文件
if os.path.isfile(db_file):
    print('true')
    # 删除指定路径文件
    os.remove(db_file)

# 初始数据:
# 这里会新建一个表表
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()

def get_score_in(low, high):
    ' 返回指定分数区间的名字，按分数从低到高排序 '
    try:
        conn=sqlite3.connect('test.db')
        cursor=conn.cursor()
        cursor.execute('select * from user where score>=? and score<=? order by score',(low,high))
        values=cursor.fetchall()
    finally:
        cursor.close()
        conn.close()
    return [value[1] for value in values]

# 测试:
assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)

print('Pass')
