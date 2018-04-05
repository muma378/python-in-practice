CHECKLIST ON ARCHITECTURE
---

## 针对各架构主题
* 程序的整体组织架构是否清晰？是否包含一个良好的架构全局观（及其理由）？
* 是否明确定义了主要构造块（包括每个构造块的职责范围及其他构造块的接口）？
* 是否明显涵盖了“需求”中列出的所有功能（每个功能对应的构造块不太多也不太少）？
* 是否描述并论证了那些最关键的类？
* 是否详细定义了数据库的组织结构和内容？
* 是否指出了所有关键的业务规则，并描述其对系统的影响？
* 是否描述了用户界面设计的策略？
* 是否估算了稀缺资源（如线程、数据库连接、句柄、网络带宽等）的使用量，是否描述并论证了资源管理的策略？
* 是否描述了架构的安全需求？
* 架构是否为每个类、每个子系统、或每个功能域提出空间与时间预算？
* 架构是否描述了如何达到伸缩性？
* 架构是否关注互操作性？
* 是否描述了国际化/本地化策略？
* 是否提供了一套内聚的错误处理策略？
* 是否规定了容错办法（如果需要）？
* 是否证实了系统各个部分的技术可行性？
* 是否详细描述了过度工程的办法？
* 是否包含了必要的“买  vs. 造”的决策？
* 架构是否描述了如何加工被复用的代码，使之符合其他架构目标？
* 是否将架构设计得能够适应和可能出现的变更？


## 架构的总体质量
* 架构是否解决了全部需求？
* 有没有哪个部分是“过度架构”或“欠架构”的？是否明确选不了在这方面的预期指标？
* 整个架构是否在概念上协调一致？
* 顶层设计是否独立作用于实现它的机器和语言？
* 是否说明了所有主要的决策的动机？
* 你，作为一名实现该系统的程序员，是否对这个架构感觉良好？