"""
在 OOP 程序设计中，当我们定义一个 class 的时候，可以从现有的某个 class 继承，新的 class 称为子类（Subclass），而被继承的 class 称为基类、父类或者超类（Base class、Super class）。

比如，我们已经编写了一个名为 Animal 的 class，有一个 run() 方法可以直接打印：
class Animal(object):
    def run(self):
        print('Animal is running...')

当我们需要编写 Dog 和 Cat 类时，就可以直接从 Animal 类继承：
class Dog(Animal):
    pass

class Cat(Animal):
    pass
对于 Dog 来说，Animal就是它的父类，对于 Animal 来说，Dog 就是它的子类。 Cat 和 Dog 类似。

继承有什么好处？最大的好处是子类获得了父类的全部功能。由于 Animal 实现了 run() 方法，因此，Dog 和 Cat 作为它的子类，也自动拥有了 run() 方法。

也可以对子类单独添加一些方法。
当子类和父类都存在相同的方法时，子类的方法会覆盖父类的方法。在代码运行的时候，总会调用子类的方法。这样，我们就获得了继承的另一个好处：多态。
要理解什么是多态，我们首先要对数据类型再作一点说明。当我们定义一个class的时候，我们实际上就定义了一种数据类型。我们定义的数据类型和Python自带的数据类型，比如str、list、dict没什么两样：
a = list() # a是list类型
b = Animal() # b是Animal类型
c = Dog() # c是Dog类型

所以，在继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类。但是，反过来就不行。
Dog可以看成Animal，但Animal不可以看成Dog。

要理解多态的好处，我们需要再编写一个函数，这个函数接受一个 Animal 类型的变量：
def run_twice(animal):
    anmial.run()
    animal.run()

当我们传入 Animal()类型的实例时，run_twice()就打印出：
>>> run_twice(Animal())
Animal is running...
Animal is running...
当我们传入 Dog 的实例时，run_twice()就打印出：
>>> run_twice(Dog())
Dog is running...
Dog is running...
Cat 同理。

你会发现，新增一个 Animal 的子类，不必对 run_twice() 做任何修改，实际上，任何依赖 Animal 作为参数的函数或者方法都可以不加修改地正常运行，原因就在于多态。

对于一个变量，我们只需要知道它是 Animal 类型，无需确切地知道它的子类型，就可以放心地调用 run()方法，而具体调用 run()方法是作用在 Animal、Dog 还是 Cat对象上，由运行该对象时确切类型决定，这就是多态真正的威力：调用方只管调用，不管细节，而当我们新增一种 Animal 子类时，只要确保 run()方法编写正确，不用管原来的代码是如何调用的。这就是著名的”开闭原则“：
对扩展开放：允许新增 Animal 子类；
对修改封闭：不需要依赖 Animal 类型的 run_twice() 等函数。

继承还可以一级一级地继承下来，就好比从爷爷到爸爸、再到儿子这样的关系。而任何类，最终都可以追溯到根类object，这些继承关系看上去就像一颗倒着的树。


小结

继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写。
动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的。


"""
