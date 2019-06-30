"""
面对对象最重要的概念就是类（Class）和实例（instance），必须牢记类是抽象的模板，比如 Student 类，而实例是根据类创建出来的一个个具体的“对象”，每个对象都拥有相同的方法，但各自的数据可能不同。

仍以 Student 类为例，在 Python 中，定义类是通过 class 关键字：
class Student(object):
    pass
class 后面紧接类名，即 Student，类名通常是大写开头的单词，紧接着是 (object)，表示该类是从哪个类继承下来的。所有的父类都继承自 object 类。

定义好了类，就可以通过类创建实例。创建实例是通过类名 + () 实现的。
bart = Student()
可以自由地给一个实例变量绑定属性，比如，给实例 bart 绑定一个 name 属性：
bart.name = 'Bart Simpson'

由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。通过定义一个特殊的 __init__ 方法，在创建实例的时候，就把 name，score 等属性绑上去：
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
注意到 __init__ 方法本身的第一个参数永远是 self，表示创建实例本身，因此，在 __init__ 方法内部，就可以把各种属性绑定到 self，因为 self 就指向创建的实例本身。
有了 self 方法，在创建实例的时候，就不能传入空参数了，必须传入与 __init__ 方法匹配的参数，但 self 不需要传， Python 解释器会自己把实例变量传进去：
bart = Student('Bart Simpson', 59)

和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量 self，并且，调用时，不用传递该参数。除此之外，类的方法和普通函数没什么区别，所以，你仍可以用默认参数、可变参数、关键字参数和命名关键字参数。


数据封装
面向对象编程的一个重要特点就是数据封装。在上面 Student 类中，每个实例就拥有各自的 name 和 score 这些数据。我们可以通过函数来访问这些数据，比如打印一个学生的成绩：
def print_score(std):
    print('{}: {}'.format(std.name, std.score))

但是，既然Student实例本身就拥有这些数据，要访问这些数据，就没有必要从外面的函数去访问，可以直接在Student类的内部定义访问数据的函数，这样，就把“数据”给封装起来了。这些封装数据的函数是和Student类本身是关联起来的，我们称之为类的方法：
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def print_score(self):
        print('{}: {}'.format(self.name, self.score))
要定义一个方法，除了第一个参数是 self 外，其他和普通函数一样。要调用一个方法，只需要在实例变量上直接调用，除了 self 不用传递，其他参数正常传入：
bart.print_score()

这样一来，我们从外部看 Student 类，就只需要知道，创建实例需要给出 name 和 score，而如何打印，都是在 Student 类的内部定义的，这些数据和逻辑被”封装“起来了，调用很容易，但却不知道内部实现的细节。

封装的另一个好处是可以给 Student 类增加新的方法，比如 get_grade：
class Student(object):
    ...
    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'
同样的，get_grade方法可以直接在实例变量上调用，不需要知道内部实现细节。


小结

类是创建实例的模板，而实例是一个一个具体对象，各个实例拥有的数据都互相独立，互不影响；
方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据；
通过在实例中调用方法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现细节。

和静态语言不同，Python 允许对实例绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但是拥有的变量名称都可能不同：
>>> bart = Student('Bart Simpson', 59)
>>> lisa = Student('Lisa Simpson', 87)
>>> bart.age = 8
>>> bart.age
8
>>> lisa.age
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute 'age'
"""
