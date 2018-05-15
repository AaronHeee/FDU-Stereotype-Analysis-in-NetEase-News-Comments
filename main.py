from Sentiment import Sentiment
from Region import Region
import pandas as pd

# df_post = pd.read_pickle("./data/0120post.p")
# text = df_post[['post']].loc[128983]

# test
if __name__ == '__main__':
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


