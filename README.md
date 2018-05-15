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

占魁：数据读取 + 数据预处理

小花：文本极性分析 + 主题模型(因为接口不变，所以很快)

之之：准备PPT：比如我们这README上的信息，我们以前讨论的论文，以及我们数据还没来所以自己造、以及咱们计划用的方法等。

Update 2018.05.14

