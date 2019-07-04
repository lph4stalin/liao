"""
在程序运行的过程中，所有的变量都是在内存中，比如，定义一个 dict：
d = dict(name='Bob', age=20, score=88)
可以随时修改变量，比如把 name 改成 'Bill'，但是一旦程序结束，变量所占用的内存就被操作系统全部回收。如果没有把修改后的 'Bill' 存储到磁盘上，下次重新运行程序，变量又被初始化为 'Bob'。

我们把变量从内存中变成可存储或者传输的过程称之为序列化，在 Python 中叫 pickling，在其他语言中也被称之为 serialization，marshalling，flattening等等，都是一个意思。

序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。

反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即 unpickling。

Python 提供了 pickle 模块来实现序列化。
首先，我们尝试把一个对象序列化并写入文件：
import pickle
d = dict(name='Bob', age=20, score=88)
pickle.dumps(d)

pickle.dumps() 方法把任意对象序列化成一个 bytes，然后，就可以把这个 bytes 写入文件。或者用另一个方法 pickle.dump() 直接把对象序列化后写入一个 file-like Object：
f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()
看着写入的 dump.txt 文件，一堆乱七八糟的内容，这些都是 Python 保存的对象内部信息。
当我们要把对象从磁盘读到内存时，可以先把内容读到一个 bytes，然后用 pickle.loads() 方法反序列化出对象，也可以直接用 pickle.load() 方法从一个 file-like Object 中直接反序列化出对象。我们打开另一个 Python 命令行来反序列化刚才保存的对象：
f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()

Pickle 的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于 Python，并且可能不同版本的 Python 彼此都不兼容，因此，只能用 Pickle 保存那些不重要的数据，不能成功地反序列化也没关系。


JSON

如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如 XML，但更好的方法是序列化为 JSON，因为 JSON 表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。JSON 不仅是标准格式，而且比 XML 更快，而且可以直接在 Web 页面中读取，非常方便。
JSON 表示的对象就是标准的 JavaScript 语言的对象，JSON 和 Python 内置的数据类型对应如下：
JSON类型	 Python类型
{}	         dict
[]	         list
"string"	 str
1234.56	     int或float
true/false	 True/False
null	     None
Python 内置的 json 模块提供了非常完善的 Python 对象到 JSON 格式的转换。我们先看看如何把 Python 对象变成一个 JSON：
import json
d = dict(name='Bob', age=20, score=88)
json.dumps(d)
>>> '{'age': 20, 'score': 88, 'name': 'Bob'}'
dumps() 方法返回一个 str，内容就是标准的 JSON。类似的，dump() 方法可以直接把 JSON 写入一个 file-like Object。
要把 JSON 反序列化为 Python 对象，用 loads() 或者对应的 load() 方法，前者把 JSON 的字符串反序列化，后者从 file-like-Object 中读取字符串并反序列化：
json_str = '{'age': 20, 'score': 88, 'name': 'Bob'}'
json.loads(json_str)
>>> {'age': 20, 'score': 88, 'name': 'Bob'}
由于 JSON 标准规定 JSON 编码是 UTF-8，所以我们总是能正确地在 Python 的 str 与 JSON 的字符串之间转换。


JSON 进阶

Python 的 dict 对象可以直接序列化为 JSON 的 {}，不过，很多时候，我们更喜欢用 class 表示对象，比如定义 Student 类，然后序列化：
import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Stduent('Bob', 20, 88)
print(json.dumps(s))
运行代码，得到TypeError。
错误的原因是 Student 对象不是一个可序列化为 JSON 的对象。
可选参数default就是把任意一个对象变成一个可序列为JSON的对象，我们只需要为Student专门写一个转换函数，再把函数传进去即可：
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }
这样，Student实例首先被student2dict()函数转换成dict，然后再被顺利序列化为JSON：
>>> print(json.dumps(s, default=student2dict))
{"age": 20, "name": "Bob", "score": 88}

或者，class 实例有一个 __dict__ 属性，它就是一个 dict，用来存储实例变量。
print(json.dumps(s, default=lambda obj: obj.__dict__))

同样的到来，如果我们要把 JSON 反序列化为一个 Student 实例对象，loads() 方法首先转换出一个 dict 对象，然后，我们传入的 object_hook 函数负责把 dict 转换为 Student 实例：
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])


练习
对中文进行JSON序列化时，json.dumps()提供了一个ensure_ascii参数，观察该参数对结果的影响：
>>> {"name": "\u5c0f\u660e", "age": 20}
If ensure_ascii is True (the default), the output is guaranteed to have all incoming non-ASCII characters escaped. If ensure_ascii is False, these characters will be output as-is.

如果ensure_ascii为True(默认值)，则输出保证将所有输入的非ASCII字符转义。如果确保ensure_ascii为False，这些字符将原样输出。


小结
Python 语言特定的序列化模块是 pickle，但如果要把序列化搞得更通用、更符合 Web 标准，就可以使用 json 模块。
json 模块的 dumps() 和 loads() 函数时定义得非常好的接口的典范。当我们使用时，只需要传入一个必须的参数，但是，当默认的序列化或反序机制不满足我们的要求时，我们又可以传入更多的参数来定制序列化或反序列化的规则，既做到了接口简单易用，又做到了充分的扩展性和灵活性。
"""
import json


obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)

print(s)
