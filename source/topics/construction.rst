.. topics_construction:

===========
开始构建
===========

变量
------------
* 描述
    * 作用域（scope）
    * 持续性（persistence）
    * 绑定时间（binding-time）
* 好名字 坏名字
    * 当前日期：
        * currentDate, todayDate
        * x, current, cd, dateRecordedWhenLoginSystem
    * 表状态：
        * dataReady, found, success
        * flag, status
    * 常量：
        * CYCLES_NEEDED
        * FIVE
    * 循环下标：
        * teamIndex, iEvent
        * i, j

-----------------------------------------------------

类（Class）
-------------
* `Magic Method`_
    * __new__, __init__, __del__
    * __str__, __unicode__, __repr__
    * Binary Operators: __add__, __mod__
    * Comparison Operators: __lt__, __eq__

* 访问修饰符（Access Modifiers）

::

    class A(object):
        def public_method(self):
            print "I am a public method"

        def _try_not_use(self):
            print "You shall not call me from outside"

        def __unable_to_use(self):
            print ("You cannot call me from outside,"
                "well... if you are not going to use"
                "obj._A__double_underscore_method()."
                )

* getter, setter

::

    class C(object):
        def __init__(self):
            self._x = None

        @property
        def x(self):
            """I'm the 'x' property."""
            print("getter of x called")
            return self._x

        @x.setter
        def x(self, value):
            print("setter of x called")
            self._x = value

    c = C()
    c.x = 'foo'  # setter called
    foo = c.x    # getter called


* 其他的装饰器：
    * @classmethod: 类方法，以cls为第一个参数；
    * @staticmethod: 类似于一个全局函数；


* 接口 - Contract-oriented Programming
    * zope.interface_
    * abc_

::

    from abc import ABCMeta, abstractmethod

    class A(metaclass=ABCMeta):
        @abstractmethod
        def foo(self): pass

    A()  # raises TypeError

    class B(A):
        pass

    B()  # raises TypeError

    class C(A):
        def foo(self): print(42)

    C()  # works

*Unlike Java's abstract methods or C++'s pure abstract methods, abstract methods as defined here may have an implementation.*

::

    import zope.interface

    class IFoo(zope.interface.Interface):
        x = zope.interface.Attribute("""X blah blah""")

        def bar(q, r=None): pass

    class Foo:
        zope.interface.implements(IFoo)

        def __init__(self, x=None):
            self.x = x

        def bar(self, q, r=None):
            return q, r, self.x

-----------------------------------------------------

包（Package)
-------------------
*
* 创建：

::

    process/
        __init__.py
        image/
            __init__.py
            draw.py
            pallet.py
        video.py

* 组织：

::

    # process/image/__init__.py
    from .draw import draw_rectangle, draw_circle

    __all__ = ['draw_rectangle', 'draw_circle']

-----------------------------------------------------

设计模式（Design Pattern）
------------------------------------

* A general, reusable solution to a commonly occurring problem within a given context in software design;
* "`Gang of Four`_" published in 1994, described 23 classic software design patterns;
* `patterns in python`_
    * factory_method_
    * builder_


-----------------------------------------------------

调试（Debug）
-------------------
策略：

工具：

* IDE: PyCharm, PyDev
* pdb_
* logging_

参考阅读：《`Python 代码调试技巧`_》


-----------------------------------------------------

优化（Optimization）
--------------------
性能分析工具：

* timeit

::

    import time

    def timeit(f):
        def f_timer(*args, **kwargs):
            start = time.time()
            result = f(*args, **kwargs)
            end = time.time()
            print f.__name__, 'took', end - start, 'time'
            return result
        return f_timer


* cProfile

::

    import cProfile

    def do_cprofile(func):
        def profiled_func(*args, **kwargs):
            profile = cProfile.Profile()
            try:
                profile.enable()
                result = func(*args, **kwargs)
                profile.disable()
                return result
            finally:
                profile.print_stats()
        return profiled_func

    def get_number():
        for x in xrange(5000000):
            yield x

    @do_cprofile
    def expensive_function():
        for x in get_number():
            i = x ^ x ^ x
        return 'some result!'

    # perform profiling
    result = expensive_function()


::

    5000003 function calls in 1.626 seconds

    Ordered by: standard name

    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    5000001    0.571    0.000    0.571    0.000 timers.py:92(get_number)
          1    1.055    1.055    1.626    1.626 timers.py:96(expensive_function)
          1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


* line_profiler_

::

    import random

    @profile
    def random_sort2(n):
        l = [random.random() for i in range(n)]
        l.sort()
        return l

    if __name__ == "__main__":
        random_sort2(2000000)

::

    $ kernprof -l -v timing_functions.py


::

    Timer unit: 1e-06 s

    Total time: 2.11665 s
    File: timing_functions.py
    Function: random_sort2 at line 3

    Line #      Hits         Time  Per Hit   % Time  Line Contents
    ==============================================================
         3                                           @profile
         4                                           def random_sort2(n):
         5   2000001     795420.0      0.4     37.6      l = [random.random() for i in range(n)]
         6         1    1321221.0 1321221.0     62.4      l.sort()
         7         1          4.0      4.0      0.0      return l


* memory_profiler

::

    $ python -m memory_profiler timing_functions.py


::

    Filename: timing_functions.py

    Line #    Mem usage    Increment   Line Contents
    ================================================
         3   31.844 MiB   31.844 MiB   @profile
         4                             def random_sort2(n):
         5   33.148 MiB    1.305 MiB       l = [random.random() for i in range(n)]
         6   33.148 MiB    0.000 MiB       l.sort()
         7   33.148 MiB    0.000 MiB       return l


参考阅读： 《`7 tips to Time Python scripts and control Memory & CPU usage`_》

策略：



-----------------------------------------------------



.. _Magic Method: https://minhhh.github.io/posts/a-guide-to-pythons-magic-methods
.. _zope.interface: https://zopeinterface.readthedocs.io/en/latest/
.. _abc:  https://www.python.org/dev/peps/pep-3119/
.. _Design Pattern: https://en.wikipedia.org/wiki/Software_design_pattern
.. _Gang of Four: https://en.wikipedia.org/wiki/Design_Patterns
.. _patterns in python: https://github.com/faif/python-patterns
.. _Python 代码调试技巧: https://www.ibm.com/developerworks/cn/linux/l-cn-pythondebugger/index.html
.. _pdb: https://docs.python.org/2/library/pdb.html
.. _logging: https://docs.python.org/2/library/logging.html
.. _factory_method: https://github.com/faif/python-patterns/blob/master/creational/factory_method.py
.. _builder: https://github.com/faif/python-patterns/blob/master/creational/builder.py
.. _line_profiler: https://github.com/rkern/line_profiler
.. _7 tips to Time Python scripts and control Memory & CPU usage: http://www.marinamele.com/7-tips-to-time-python-scripts-and-control-memory-and-cpu-usage?utm_source=Python%20Weekly%20Newsletter&utm_campaign=2bbc6ad4bc-Python_Weekly_Issue_167_November_27_2014&utm_medium=email&utm_term=0_9e26887fc5-2bbc6ad4bc-312702461
