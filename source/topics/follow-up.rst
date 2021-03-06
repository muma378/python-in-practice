.. topics_followup:

===========
Release(Are we ready?)
===========

单元测试
---------------------

* 基础：
    * 不同于功能测试或集成测试，单元测试每次只关注一小块功能的正确性，这样一个测试单元被称为测试用例（test case）；
    * 测试单元之间应该是相互独立的，不受彼此调用顺序的影响，一组相关的测试用例组成测试套件（test suite）；
    * 测试过程中可能需要创建临时文件、建立代理数据库或服务，这一系列相关的准备和清理工作，被称为test fixture；
    * 实践中，根据实际情况不断调整你的test suite：
        * 比如在开始和结束开发的时候各运行一次完整的test suite保证你的修改没有对过去的功能产生影响；
        * 在编码的时候，分离出与之相关的测试用例，并且尽可能频繁地运行（甚至当你保存的时候自动化运行）；
        * 即使属于同一个功能块的测试用例，也可以根据花费时间来组织成不同的test suite，以保证更快地获得反馈；
    * 好的单元测试不仅能帮助开发者保证代码的正确性，也是其他维护者了解具体实现的重要入口；
    * unittest_

::

    import unittest
    from widgets import Widget

    class WidgetTestCase(unittest.TestCase):
        def setUp(self):
            self.widget = Widget('The widget')

        def test_default_widget_size(self):
            self.assertEqual(self.widget.size(), (50,50),
                             'incorrect default size')

        def test_widget_resize(self):
            self.widget.resize(100,150)
            self.assertEqual(self.widget.size(), (100,150),
                             'wrong size after resize')


    def suite():
        suite = unittest.TestSuite()
        suite.addTest(WidgetTestCase('test_default_widget_size'))
        suite.addTest(WidgetTestCase('test_widget_resize'))
        return suite

    if __name__ == '__main__':
        runner = unittest.TextTestRunner()
        runner.run(suite())



* 工具：
    * py.test_ : super straight forward
        * pytest-cov_ : unittest coverage report

::

    $py.test --cov=myproj tests/


::

    -------------------- coverage: platform linux2, python 2.6.4-final-0 ---------------------
    Name                 Stmts   Miss  Cover
    ----------------------------------------
    myproj/__init__          2      0   100%
    myproj/myproj          257     13    94%
    myproj/feature4286      94      7    92%
    ----------------------------------------
    TOTAL                  353     20    94%

*
    * mock_ : a library allows you to replace parts of your system under test with mock objects and make assertions about how they have been used. As of Python 3.3, it is available in the standard library.

::

    >>> from mock import MagicMock
    >>> thing = ProductionClass()
    >>> thing.method = MagicMock(return_value=3)
    >>> thing.method(3, 4, 5, key='value')
    3
    >>> thing.method.assert_called_with(3, 4, 5, key='value')

*
    * tox_: a tool to automate and standardize testing in Python. It is part of a larger vision of easing the packaging, testing and release process of Python software.
..    .. image:: /ystatic/tox.png

::
    # content of: tox.ini , put in same dir as setup.py
    # generated by tox-quickstart
    [tox]
    envlist = py27,py36
    [testenv]
    deps=pytest       # install pytest in the venvs
    commands=pytest  # or 'nosetests' or ...

参考阅读：`Testing Your Code`_

-----------------------------------------------------

重构（Refactoring）
----------------------

* 软件演化是无法避免且具有重要意义的现象，一旦开始就充满危险，但同时也是你的软件开发接近完美的天赐良机；

.. image:: /ystatic/refactoring-eines.jpg


::

    在不改变软件外部行为的前提下，对其内部结构进行改变，使之更容易理解并便于修改。
                                            -- Martin Fowler

* 重构的理由——代码的“坏味道”：
    * 代码重复
    * 循环过长或嵌套过深
    * 内聚性低/耦合性高
    * 大段的注释
    * ...
* 重构的方法：
    * 将相似的代码结合起来放到基类中
    * 多态替代条件语句
    * 提取子程序或者方法
    * 使变量名/函数名/类名更清晰
    * ...
* 不宜重构的情况：
    * 不要把重构当成先写后改的代名词
    * 避免用重构代替重写


参考阅读：《 `重构：改善既有代码的设计`_ 》

-----------------------------------------------------

CI（Continuous Integration）
----------------------------

* Travis_
    * Continuous Integration is the practice of merging in small code changes frequently - rather than merging in a large change at the end of a development cycle. The goal is to build healthier software by developing and testing in smaller increments.
    *
::

    language: python
    sudo: false
    branches:
      only:
        - master
        - /^\d\.\d+$/
        - /^\d\.\d+\.\d+(rc\d+|\.dev\d+)?$/
    matrix:
      include:
        - python: 2.7
          env: TOXENV=py27
        - python: 3.6
          env: TOXENV=py36
    install:
      - pip install -U tox twine wheel codecov
    script: tox
    after_success:
      - codecov
    cache:
      directories:
        - $HOME/.cache/pip
    deploy:
      provider: pypi
      distributions: "sdist bdist_wheel"
      user: scrapy
      password:
      on:
        tags: true
        repo: scrapy/scrapy
        condition: "$TOXENV == py27 && $TRAVIS_TAG =~ ^[0-9]+[.][0-9]+[.][0-9]+(rc[0-9]+|[.]dev[0-9]+)?$"

* Jenkins_

-----------------------------------------------------

文档
---------
* Markdown_
    * markdown-cheatsheet_
* reStructText_
* sphinx_

::

    $ sphinx-quickstart

* `Read The Docs`_


-----------------------------------------------------


.. _unittest: https://docs.python.org/3/library/unittest.html
.. _changes in python3: https://docs.python.org/3.0/whatsnew/3.0.html
.. _py.test: http://pytest.org/
.. _pytest-cov: https://pypi.python.org/pypi/pytest-cov/
.. _Testing Your Code: http://docs.python-guide.org/en/latest/writing/tests/
.. _mock: http://www.voidspace.org.uk/python/mock/
.. _tox: https://tox.readthedocs.io/en/latest/
.. _重构：改善既有代码的设计: https://www.amazon.cn/dp/B003BY6PLK
.. _Travis: https://docs.travis-ci.com/user/getting-started/
.. _Jenkins: https://jenkins.io/
.. _sphinx: http://www.sphinx-doc.org/en/master/
.. _Markdown: https://en.wikipedia.org/wiki/Markdown
.. _markdown-cheatsheet: https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet
.. _reStructText: http://docutils.sourceforge.net/docs/user/rst/quickref.html
.. _Read The Docs: https://docs.readthedocs.io/en/latest/
