.. topics_setup:

===========
准备工作
===========

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
* 安全性/可伸缩性/性能 ...

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
* virtualenv
* svc

.. _流行协议简介: https://paulmillr.com/posts/simple-description-of-popular-software-licenses/
.. _选择协议: http://www.lanceyan.com/tech/arch/opensource_permission.html
.. _PEP8: https://www.python.org/dev/peps/pep-0008/
.. _REST vs SOAP: https://blog.smartbear.com/apis/understanding-soap-and-rest-basics/
