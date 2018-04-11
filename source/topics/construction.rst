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

    .. image:: /ystatic/factory_method.jpg

    * state_

    .. image:: /ystatic/state.jpg

参考阅读：《 `设计模式 可复用面向对象软件的基础`_ 》

-----------------------------------------------------

调试（Debug）
-------------------
策略：

1. 将错误状态稳定下来；
2. 确定错误来源——
    a. 收集产生缺陷的相关数据，
    b. 分析所收集的数据，并构造对缺陷的假设，
    c. 确定怎样去证实或证伪这个假设，可以对程序进行测试或是通过检查代码，
    d. 按照2（c）确定的方法对假设做出最终结论；
3. 修补缺陷；
4. 对所修补的地方进行测试；
5. 查找是否还有类似错误。

*《代码大全》23.2 寻找缺陷*

工具：

* IDE: PyCharm, PyDev
* pdb_
* logging_

::

    import logging
    LOG1=logging.getLogger('b.c')
    LOG2=logging.getLogger('d.e')
    filehandler = logging.FileHandler('test.log','a')
    formatter = logging.Formatter('%(name)s %(asctime)s %(levelname)s %(message)s')
    filehandler.setFormatter(formatter)
    filter=logging.Filter('b')
    filehandler.addFilter(filter)
    LOG1.addHandler(filehandler)
    LOG2.addHandler(filehandler)
    LOG1.setLevel(logging.INFO)
    LOG2.setLevel(logging.DEBUG)
    LOG1.debug('it is a debug info for log1')
    LOG1.info('normal infor for log1')
    LOG1.warning('warning info for log1:b.c')
    LOG1.error('error info for log1:abcd')
    LOG1.critical('critical info for log1:not worked')
    LOG2.debug('debug info for log2')
    LOG2.info('normal info for log2')
    LOG2.warning('warning info for log2')
    LOG2.error('error:b.c')
    LOG2.critical('critical')


::

    b.c 2011-11-25 11:07:29,733 INFO normal infor for log1
    b.c 2011-11-25 11:07:29,733 WARNING warning info for log1:b.c
    b.c 2011-11-25 11:07:29,733 ERROR error info for log1:abcd
    b.c 2011-11-25 11:07:29,733 CRITICAL critical info for log1:not worked


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
    * Pareto法则
    * 多线程 多进程
    * C语言扩展_：
        * ctypes
        * SWIG_


-----------------------------------------------------



.. _Magic Method: https://minhhh.github.io/posts/a-guide-to-pythons-magic-methods
.. _zope.interface: https://zopeinterface.readthedocs.io/en/latest/
.. _abc:  https://www.python.org/dev/peps/pep-3119/
.. _Design Pattern: https://en.wikipedia.org/wiki/Software_design_pattern
.. _Gang of Four: https://en.wikipedia.org/wiki/Design_Patterns
.. _设计模式 可复用面向对象软件的基础: https://www.amazon.cn/dp/B001130JN8
.. _patterns in python: https://github.com/faif/python-patterns
.. _Python 代码调试技巧: https://www.ibm.com/developerworks/cn/linux/l-cn-pythondebugger/index.html
.. _pdb: https://docs.python.org/2/library/pdb.html
.. _logging: https://docs.python.org/2/library/logging.html
.. _factory_method: https://github.com/faif/python-patterns/blob/master/creational/factory_method.py
.. _state: https://github.com/faif/python-patterns/blob/master/behavioral/state.py
.. _builder: https://github.com/faif/python-patterns/blob/master/creational/builder.py
.. _line_profiler: https://github.com/rkern/line_profiler
.. _7 tips to Time Python scripts and control Memory & CPU usage: http://www.marinamele.com/7-tips-to-time-python-scripts-and-control-memory-and-cpu-usage?utm_source=Python%20Weekly%20Newsletter&utm_campaign=2bbc6ad4bc-Python_Weekly_Issue_167_November_27_2014&utm_medium=email&utm_term=0_9e26887fc5-2bbc6ad4bc-312702461
.. _Pareto法则: https://en.wikipedia.org/wiki/Pareto_principle
.. _C语言扩展: https://python3-cookbook.readthedocs.io/zh_CN/latest/chapters/p15_c_extensions.html
.. _SWIG: http://www.swig.org/
