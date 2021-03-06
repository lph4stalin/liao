"""
在计算机程序的开发过程中，随着程序代码越写越多，在一个文件里代码会越来越长，越来越不容易维护。

为了编写可维护的代码，我们把很多函数分组，分别放到不同的文件里。这样，每个文件包含的代码就相对较少，很多编程语言都采用这种组织代码的方式。在 Python 中，一个 .py 文件就称为一个模块(Moduel)。

使用模块有什么好处？

最大的好处是大大提高了代码的可维护性。其次，编写代码不必从零开始。当一个模块编写完毕，就可以被其他地方引用。我们在编写程序的时候，也经常引用其他模块，包括 Python 内置的模块和来自第三方的模块。

使用模块还可以避免函数名和变量名冲突。相同名字的函数和变量完全可以存储在不同模块中，因此，我们自己在编写模块时，不必考虑名字会与其他模块冲突。但也要注意，尽量不要与内置函数名字冲突。

如果不同的人编写的模块名相同怎么办？为了避免模块名的冲突，Python 引入了按目录来组织模块的方法，称为包(Package)。

举个例子，一个名为 abc.py 的文件就是一个名叫 abc 的模块，一个 xyz.py 的文件就是一个名叫 xyz 的模块。

现在，我们假设 abc 和 xyz 这两个模块名字与其他模块冲突了，于是我们可以通过包来组织模块，避免冲突。方法是选择一个顶层包名，比如 mycompany，按照如下目录存放：
mycompany
├─ __init__.py
├─ abc.py
└─ xyz.py

引入了包以后，只要顶层的包名不与别人冲突，那所有的模块都不会与别人冲突。现在，abc.py 模块的名字就变成了 mycompany.abc，类似的，xyz.py 的模块名变成了 mycompany.xyz。

每个包目录下面都有一个 __init__.py 的文件，这个文件是必须存在的，否则，Python就把这个目录当成一个普通目录，而不是一个包。__init__.py 可以是一个空文件，也可以有 Python 代码，因为 __init__.py 本身就是一个模块，而它的模块名就是 mycompany。

类似的，可以有多级目录，组成多级层次的包结构。比如如下的目录结构：
mycompany
 ├─ web
 │  ├─ __init__.py
 │  ├─ utils.py
 │  └─ www.py
 ├─ __init__.py
 ├─ abc.py
 └─ utils.py

 文件 www.py 的模块名就是 mycompany.web.www，两个文件 utils.py 的模块名分别是 mycompany.utils 和 mycompany.web.utils。

 创建自己的模块要注意：
    · 模块名要遵守 Python 变量命名规范，不要使用中文和特殊字符。
    · 模块名不能和系统模块名冲突，最好先查看系统是否已存在该模块，检查方法是在 Python 交互环境执行 import abc，如果成功则说明系统存在 abc 模块。
"""
