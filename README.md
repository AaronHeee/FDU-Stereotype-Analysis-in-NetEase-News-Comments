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

评论内容table: XXXXcontent.p

| 帖ID tie_id   | 评论帖的唯一键值 |
| ------------ | -------- |
| 评论内容 content | 评论帖的正文   |

#### +  数据预处理 

```python
def region_detect(text):
    """
    :param text: 所探测文本，数据格式：dataFrame,如df_content['content'],尺寸为(#content, 1)
    :return id: 返回相关地域id, 上限为3个，数据格式：dataFrame,方便和原始数据拼接，尺寸为(#content, 3)
    """
```

## 建立模型

#### + 文本极性分析

```python
def sentiment_detect(text, region_dict):
    """
    :param text: 所探测文本，数据格式：dataFrame,如df_content['content'],尺寸为(#content, 1)
    :param region_dict: 地域情感词计数器，数据格式：双重dict，例：region_dict[province][word]，每次查找到该次，词频会增加
    :return dist: 返回这段话攻击的地域，数据格式：list [location1, location2...]
    :return sentiment:返回正负向词汇统计信息三元组，数据格式：tuple (sentiment polar, #negative words, #positive words)
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

