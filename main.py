from Sentiment import SentiFeatures
import pandas as pd

df_post = pd.read_pickle("./data/0120post.p")
text = df_post[['post']].loc[128983]


def sentiment_detect(text, region_dict):
    """
    :param text: 所探测文本，数据格式：dataFrame,如df_content['content'],尺寸为(#content, 1)
    :param region_dict: 地域情感词计数器，数据格式：双重dict，例：region_dict[province][word]，每次查找到该次，词频会增加
    :return dist: 返回这段话攻击的地域，数据格式：list [location1, location2...]
    :return sentiment:返回正负向词汇统计信息三元组，数据格式：tuple (sentiment polar, #negative words, #positive words)
    """

    sentiment = SentiFeatures(text)


# test
# if __name__ == '__main__':
#     while True:
#         print(SentiFeatures(input()))
