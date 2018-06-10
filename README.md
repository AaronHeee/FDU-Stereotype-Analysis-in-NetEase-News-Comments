# 大数据视角下的网络新闻跟帖地域歧视现象分析

## 数据

正文信息table: ./data/post.p

| 文章ID   docid  | 新闻的唯一键值 |
| ------------- | ------- |
| 频道名 channel   | 新闻所属板块  |
| 文章日期 realtime | 新闻的发出日期 |
| 文章正文 post     | 新闻的正文内容 |
| 文章标题 title    | 新闻的标题   |

评论信息table: ./data/XXXX.p

| 文章ID docid       | 所评论新闻唯一键值                                |
| ---------------- | ---------------------------------------- |
| **帖ID tie_id**   | **评论帖的唯一键值**                             |
| 用户ID passport    | 发帖用户的唯一键值                                |
| 楼层数 floor        | 发帖的楼层，默认为1                               |
| 发帖人 Ip           | 发帖人的IP明码(用来获得地域信息)                       |
| 第一楼ID f1_tie_id  | 本帖的第一楼ID                                 |
| 上一楼ID ptie_id    | 本帖的上一楼ID                                 |
| 发帖时间 realtime    | 发帖的时间                                    |
| 用户状态 userprofile | 用户状态的五位数值：\[是否有头像\]\[是否匿名]\[是否认证]\[是否VIP]\[是否红名] |
| 发帖来源 source      | 发帖来源： wb即pc发贴，ph-ios即iphone端发贴，<br />ph-android即安卓端发贴，其他无法确认的默认均为ph。 |

评论内容table: ./data/XXXXcontent.p

| 帖ID tie_id   | 评论帖的唯一键值 |
| ------------ | -------- |
| 评论内容 content | 评论帖的正文   |

#### 数据读入
```python
import pandas as pd
df_post = pd.read_pickle("./data/post.p")
......
```



## 建立模型

#### 地域探测: Region.py

```python
class Region(object):
    def __init__(self, path):
        """ 初始化Region类
        :param path: 地域字典的绝对路径
        """
        
    def region_detect(self, data, on, id_num = 3):
        """ 在dataFrame中批量添加region探测字段
        :param data: 输入的dataFrame，数据格式：dataFrame，如df_post
        :param on: dataFrame中探测的字段名，数据格式：list，如["post", "title"]
        :param id_num: 探测的region数量，未探测则为0，数据格式：int，默认为3
        :return: 返回已经添加了region探测字段的dataFrame
        """
        
     def ip_detect(self, data, on):
        """ 在dataFrame中批量添加src探测字段
        :param data: 输入的dataFrame，数据格式：dataFrame，如df_post
        :param on: dataFrame中探测的字段名，数据格式：list，通常为["ip"]
        :return:  返回已经添加了src探测字段的dataFrame
        """
```



#### 文本极性分析: Sentiment.py

```python
class Sentiment(object):
    def sentiment_detect(self, data, on, srcs=None, dists=None):
        """ 在dataFrame中批量添加"polar", "pos-words", "neg-words"字段
        分别代表该条评论的情感极性、正向词汇个数、反向词汇个数
        另外维护一个本地成员self.record，用来记录src->dist的评价词汇词频
        :param data: 输入的dataFrame，数据格式：dataFrame，如df_post
        :param on: dataFrame中探测的字段名，数据格式：list，通常为["content"]
        :param srcs: dataFrame中表示评论用户所在地的字段名，数据格式：list,通常为["src"]
        :param dists: dataFrame中表示被评论地区的字段名，数据格式：list,通常为["region_1", "region_2",...]
        :return:  返回已经添加了polar, pos-words, neg-words探测字段的dataFrame
        """
```



#### + 主题模型

```python
def topic_detect(text):
  """
  与LDA的接口相同
  """
```



## 任务安排

**大体** 

- 三个人去手动判断模型的表现
  - 占魁负责把数据抽样出来，用Excel发给小花和之之进行判断
  - 两个方面
    - 准确率：选取的地域评论中，真正的地域评论所占比例（包括正负向）
    - 召回率：（抽样）所有地域评论中，被我们探测出来的比例

**占魁**

- 手机端/wb端数据的筛选：是否安卓端更容易歧视
- 标题和新闻对评论的影响：用新的数据，忽略ip，仅仅考虑评论的情感和地域即可
- 地域矩阵，查询是不是有省份间的异常波动

**小花**

- 本地ip定位函数
- 期末报告、考虑如何利用结果进行舆论引导和省份正面形象宣传(旅游片等)

**之之**

- 等大概的统计数据跑出来之后
  - 发生的比较大的一些地域相关的新闻
- 查询人口流动有关数据、各个省份的经济水平/人口数量、网络普及度

- 画网络结构图，根据网络的基本信息进行相关分析

  - 规定方向：每两个结点间两条线（代表正负向），中心结点最(不)受喜爱
  - 完全图，每两个结点间的两条线进行叠加，最终只有一条线，**偏爱度**

  




## 中期报告

**周葆华老师：**

- 数据（再催下数据！！）
- 考虑一下偏差度 比如：会不会春节出去旅游啊之类的
- 除了互黑地图，还可以做一个网络结构图
- 增加标题和新闻的作用！看会不会引导新闻

**周雅倩老师：** 

- ~~ip离线数据库：qqwry.dat~~
- 评价metric，可以考虑抽样人工判定，给出准确率。
  两个人判断 给出两个人评价的一致性，把平均值作为ground truth。

**阳德青老师：**

- 可以探讨更多社会意义的现象 比如：上海为什么没有安徽路
- 人口输入输出要考虑 还有什么接壤



Update 2018.05.16

