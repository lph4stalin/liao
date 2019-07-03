"""
如果你听说过“测试驱动开发”（TDD:Test-Driven Development），单元测试就不陌生。
单元测试是用来对一个模块、一个函数或者一个类来进行正确性检验的测试工作。
比如对函数 abs()，我们可以编写出以下几个测试用例：
1. 输入正数，比如 1、1.2、0.99，期待返回值与输入相同；
2. 输入负数，比如 -1、-1.2、-0.99，期待返回值与输入相反；
3. 输入 0，期待返回 0；
4. 输入非数值类型，比如 None、[]、{}，期待抛出 TypeError。
把上面的测试用例放到一个测试模块里，就是一个完整的单元测试。

如果单元测试通过，说明我们测试的这个函数能够正常工作。如果单元测试不通过，要么函数有 bug，要么测试条件输入不正确，总之，需要修复使单元测试能够通过。
单元测试通过后由什么意义呢？如果我们对 abs() 函数做了修改，只需要再跑一遍单元测试，如果通过，说明我们的修改不会对 abs() 函数原有行为造成影响，如果测试不通过，说明我们的修改与原有行为不一致，要么修改代码，要么修改测试。

这种以测试为驱动的开发模式最大的好处就是确保一个程序模块的行为符合我们设计的测试用例。在将来修改的时候，可以极大程度地保证该模块行为仍然是正确的。

我们来编写一个 Dict 类，这个类的行为和 dict 一致，但是可以通过属性来访问，用起来就像下面这样。
>>> d = Dict(a=1, b=2)
>>> d['a']
1
>>> d.a
1

mydict.py代码如下：

class Dict(dict):

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


为了编写单元测试，我们需要引入Python自带的unittest模块，编写mydict_test.py如下：

import unittest

from mydict import Dict

class TestDict(unittest.TestCase):

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty


小结
单元测试可以有效地测试某个程序模块的行为，是未来重构代码的信心保证。

单元测试的测试用例要覆盖常用的输入组合、边界条件和异常。

单元测试代码要非常简单，如果测试代码太复杂，那么测试代码本身就可能有bug。

单元测试通过了并不意味着程序就没有bug了，但是不通过程序肯定有bug。
"""
