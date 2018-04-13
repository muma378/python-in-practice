.. topics_setup:

===========
准备工作
===========

概要设计
---------
* 主要构造块（building blocks）
    * 功能的内聚性
    * 层次结构（hierarchy)
    * 调用关系
* 用户界面设计
* 惯例约定
    * Layout
        * Code Style(PEP8_)
    * Naming
        * 缩写（abbreviation）
        * 注释
        * 常量
    * Error Handling
    * Encode/Decode
    * File Structure

::

    # a general layout of python project
    project_name/
        doc/
        examples/
        project_name/
        tests/
        .travis.yml
        LICENCE
        MANIFEST.in
        NEWS
        README.md
        requirements.txt
        setup.py
        tox.ini


* 安全性/可伸缩性/性能 ...
* Checklist-Architecture_

-----------------------------------------------------

协议选择
----------

.. image:: /ystatic/open-source-licenses-en.png

(`流行协议简介`_)

* **GPL** 使用该协议的产品的软件产品也必须是开源和免费的
* **LGPL** GPL的宽松版（lesser），允许商业软件引用但不允许修改
* **BSD/Apache License 2** 允许修改和重新发布，但是带有一系列限制，以BSD为例：
    * 如果再发布的产品中包含源代码，则在源代码中必须带有原来代码中的BSD协议；
    * 如果再发布的只是二进制类库/软件，则需要在类库/软件的文档和版权声明中包含原来代码中的BSD协议；
    * 不可以用开源代码的作者/机构名字和原来产品的名字做市场推广。
* **MIT** 限制最少的协议，只需要在修改后的代码和发行包中包含作者许可即可

-----------------------------------------------------

.. not mentioned
    详细设计
    ---------
    * 通讯
        * IPC: socket, shared-memory, queue, mutex
        * Web service: `REST vs SOAP`_
    * 持久化
        * file system: pickle, HDFS, FastDFS
        * database: SQL, NoSQL, in-memory
    * 交互
        * B/S vs C/S

编码之前
-----------

* Virtualenv_
* `Version Control`_
    * gitlab_
* packaging_
    * setup.py

::

    from setuptools import setup

    with open(join(dirname(__file__), 'scrapy/VERSION'), 'rb') as f:
        version = f.read().decode('ascii').strip()

    setup(
        name='Scrapy',
        version=version,
        url='http://scrapy.org',
        description='A high-level Web Crawling and Web Scraping framework',
        long_description=open('README.rst', 'rb').read(),
        author='Scrapy developers',
        maintainer='Pablo Hoffman',
        maintainer_email='pablo@pablohoffman.com',
        license='BSD',
        packages=find_packages(exclude=('tests', 'tests.*')),
        include_package_data=True,
        zip_safe=False,
        entry_points={
            'console_scripts': ['scrapy = scrapy.cmdline:execute']
        },
        classifiers=[
            'Framework :: Scrapy',
            'Development Status :: 5 - Production/Stable',
            'Environment :: Console',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Topic :: Internet :: WWW/HTTP',
            'Topic :: Software Development :: Libraries :: Application Frameworks',
            'Topic :: Software Development :: Libraries :: Python Modules',
        ],
        install_requires=[
            'Twisted>=13.1.0',
            'w3lib>=1.17.0',
            'queuelib',
            'lxml',
            'pyOpenSSL',
            'cssselect>=0.9',
            'six>=1.5.2',
            'parsel>=1.1',
            'PyDispatcher>=2.0.5',
            'service_identity',
        ],
        extras_require=extras_require,
    )


::

    $ python setup.py sdist bdist_wheel

* * PyPI_

::

    $ python setup.py upload


.. _流行协议简介: https://paulmillr.com/posts/simple-description-of-popular-software-licenses/
.. _选择协议: http://www.lanceyan.com/tech/arch/opensource_permission.html
.. _PEP8: https://www.python.org/dev/peps/pep-0008/
.. _REST vs SOAP: https://blog.smartbear.com/apis/understanding-soap-and-rest-basics/
.. _Checklist-Architecture: https://github.com/muma378/python-in-practice/blob/master/extra/checklist-on-architecture.md
.. _Virtualenv: https://virtualenv.pypa.io/en/stable/
.. _packaging: https://packaging.python.org/tutorials/distributing-packages/
.. _PyPI: https://pypi.python.org/pypi
.. _Version Control: https://en.wikipedia.org/wiki/Version_control
.. _gitlab: https://about.gitlab.com/
