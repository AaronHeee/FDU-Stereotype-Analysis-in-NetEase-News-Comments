# @Time        : 2018/5/15
# @Author      : Zhankui (Aaron) He
# @File        : Region.py
# @Description : Region Dictionary construction and Regions Detection

import pandas as pd
from multiprocessing import Pool, cpu_count
import requests

ID_NUM = 3
WORDPOOL = None
WORD2REGION = None

def _region_detect(row):
    """ 单句地域探测，由于需要用于多进程，故使用全局变量，写在Region Class外部

    :param row: 单句文本，数据格式：str
    :return: 探测的地域结果，数据格式：list, 数据尺寸:(1, ID_NUM)
    """
    global ID_NUM, WORDPOOL, WORD2REGION
    region_set = set([])
    for word in WORDPOOL:
        if row.find(word) != -1:
            for r in WORD2REGION[word]:
                region_set.add(r)
    r = [region for region in list(region_set)[:ID_NUM]]
    if len(r) < ID_NUM:
        r += [0 for _ in range(ID_NUM - len(r))]
    return r

def _ip_detect(ip):
    URL = 'http://freeipapi.17mon.cn/' + ip
    r = requests.get(URL, timeout=3)
    json_data = r.json()
    return(json_data[1])

class Region(object):

    def __init__(self, path):
        """ 初始化Region类

        :param path: 地域字典的绝对路径
        """
        self.region2word = {}
        self.word2region = {}
        with open(path, "r") as f:
            for line in f:
                regions = line.strip().split("\t")
                self.region2word[regions[0]] = [r for r in regions]
                for r in regions:
                    if r not in self.word2region:
                        self.word2region[r] = [regions[0]]
                    else:
                        self.word2region[r].append(regions[0])
        self.wordPool = set(self.word2region.keys())

        global WORDPOOL, WORD2REGION
        WORDPOOL = self.wordPool
        WORD2REGION = self.word2region

    def region_detect(self, data, on, id_num = 3):
        """ 在dataFrame中批量添加region探测字段

        :param data: 输入的dataFrame，数据格式：dataFrame，如df_post
        :param on: dataFrame中探测的字段名，数据格式：list，如["post", "title"]
        :param id_num: 探测的region数量，未探测则为0，数据格式：int，默认为3
        :return: 返回已经添加了region探测字段的dataFrame
        """
        global ID_NUM
        ID_NUM = id_num

        rows = [" ".join([row[i] for i in on]) for _, row in data.iterrows()]

        pool = Pool(cpu_count())
        res = pool.map(_region_detect, rows)
        pool.close()
        pool.join()

        data = pd.concat([data, pd.DataFrame(data = res, columns=["region_%d" % (i+1) for i in range(id_num)])], axis=1)
        return data

    def ip_detect(self, data, on):
        """ 在dataFrame中批量添加src探测字段

        :param data: 输入的dataFrame，数据格式：dataFrame，如df_post
        :param on: dataFrame中探测的字段名，数据格式：list，通常为["ip"]
        :return:  返回已经添加了src探测字段的dataFrame
        """
        rows = [" ".join([row[i] for i in on]) for _, row in data.iterrows()]

        pool = Pool(cpu_count())
        res = pool.map(_ip_detect, rows)
        pool.close()
        pool.join()

        data = pd.concat([data, pd.DataFrame(data=res, columns=["src"])], axis=1)
        return data

if __name__ == "__main__":

    # 初始化Region Class
    path = "/Users/aaronhe/Documents/NutStore/Aaron He/FDU/Big-Data-Communication/Stereotype-Analysis-in-NetEase-News-Comments/Dict/region_dict/region.txt"
    r = Region(path)

    # 构造输入数据
    text = [
        "潮汕人很帅，湖北人挺会做生意的！",
        "老铁牛逼！",
        "我觉得很好吃啊"
        ]
    df = pd.DataFrame(text, columns=["text"])
    print(df.head())

    # 单句地域探测
    print(_region_detect("老铁牛逼"))

    # dataFrame中批量添加region字段
    print(r.region_detect(df, on=["text"]))

    print(_ip_detect("202.104.15.102"))
