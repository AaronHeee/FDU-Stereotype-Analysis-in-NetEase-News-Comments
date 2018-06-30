from Sentiment import Sentiment
from Region import Region
import pandas as pd
import sys
import os


# df_post = pd.read_pickle("./data/0120post.p")
# text = df_post[['post']].loc[128983]

# test
def test():
    s = Sentiment()
    r = Region("/Users/aaronhe/Documents/NutStore/Aaron He/FDU/Big-Data-Communication/Stereotype-Analysis-in-NetEase-News-Comments/Dict/region_dict/region.txt")

    # 构造输入数据
    text = [
        ["潮汕人很帅，湖北人挺会做生意的！", "上海"],
        ["老铁牛逼！", "重庆"],
        ["我觉得很好吃啊", "北京"],
        ]

    df = pd.DataFrame(text, columns=["text", "src"])
    print(df.head())

    df = r.region_detect(df, on=["text"])

    # dataFrame中批量添加region字段
    print(s.sentiment_detect(df, on=["text"], srcs=["src"], dists=["region_1", "region_2", "region_3"]))
    print(s.output_record(src = "北京"))

def preprocess():

    # MySQL设定
    # engine = create_engine('mysql://root:qwert12345@localhost:3306/netease', convert_unicode=True, encoding='utf-8',
    #                        connect_args={"charset": "utf8"})

    # 数据读入
    date = sys.argv[1]
    path_prefix = "./new_data"
    df = pd.read_pickle(os.path.join(path_prefix, "%s.p" % date))
    df_content = pd.read_pickle(os.path.join(path_prefix, "%scontent.p" % date))
    df_post = pd.read_pickle(os.path.join(path_prefix, "%spost.p" % date))

    print(len(df))
    df = pd.merge(df, df_content, on="tie_id")
    print(df.head())
    df = df.dropna(axis=0)
    print(len(df))

    # 模型加载
    path_region_dict = "./Dict/region_dict/region_new.txt"
    r = Region(path_region_dict)
    # df = r.ip_detect(df.iloc[:10], on=["ip"])
    df = r.region_detect(df, on=["content"])
    df_select = df[df["region_1"] != 0]
    print(len(df_select))
    print(df_select)

    df_select = r.ip_detect(df_select.iloc[:], on=["ip"], nbworker=8)
    print(df_select.head())

    # 模型存储
    df_select.to_pickle(os.path.join(path_prefix, "%s_select_comments.p" % date))
    # df_select.to_sql("%s_select_comments" % date, engine, index=False, if_exists="replace")


def main():
    # 数据加载
    date = sys.argv[1]
    path_prefix = "./new_data"
    df = pd.read_pickle(os.path.join(path_prefix, "%s_select_comments.p" % date))

    # 模型加载
    s = Sentiment()
    df = s.sentiment_detect(df, on=["content"], srcs=["province"], dists=["region_1", "region_2", "region_3"])
    df_freq = s.table_record()

    # 结果保存
    df.to_pickle(os.path.join(path_prefix, "%s_sentiment.p" % date))
    df_freq.to_pickle(os.path.join(path_prefix, "%s_senti_freq.p" % date))
    print(df)
    print(df_freq)


if __name__ == '__main__':
    preprocess()
    main()

