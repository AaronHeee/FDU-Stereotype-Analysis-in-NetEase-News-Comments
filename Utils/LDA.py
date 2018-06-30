
import sys
import jieba
from os import path
import gensim
from gensim import corpora

class LDA():
    def preprocess(self, text):
        # use jieba Package to do Chinese word tokenize
        seg_list = list(jieba.cut(text.strip(), cut_all=False))

        # read stop word dictionary
        stopwords = []
        f_stop = open('Dict/stopwords.txt', 'r')
        for word in f_stop.readlines():
            stopwords.append(word.strip())
        f_stop.close()

        # remove stopwords
        mywordlist = []
        for myword in seg_list:
            if not myword in stopwords:
                mywordlist.append(myword)
        return mywordlist


    def lda(self, docs, num_topics=5, num_words=5):
        """
        Implement LDA model
        ref: https://blog.csdn.net/allenalex/article/details/56510618

        @param:
            docs: [['在线', '社交', '网络', 'Facebook', 'Twitter', '个体', '关系网', '中', '发现', '人类', '认知', '约束'], 
            ['线下', '社交', '网络', '之外', '圈子'], ['电子商务', '管理', '社交', '网络', '视角', '原书', '版'], 
            ['在线', '社交', '网络', '关键', '用户', '挖掘', '方法', '研究'], 
            ['社交', '网站', '数据挖掘', '分析'], ['做'], ['赢', '社交', '商务', '企业', '社交', '网络', '构建', '之道'], 
            ['商业', '名片', '商业', '关系', '创建', '商业', '社交', '网络', '66', '技巧'], 
            ['热点', '技术', '专利', '预警', '分析', '社交', '网络', '分册'], 
            ['网红', '揭秘', '电子商务', '零售业', '社交', '网络', '盈利', '故事']]
        """
        # creating the term dictionary of our courpus, where every unique term is assigned an index
        dictionary = corpora.Dictionary(docs)

        # converting list of documents (corpus) into Document Term Matrix using dictionary prepared above
        doc_term_matrix = [dictionary.doc2bow(doc) for doc in docs]

        # creating the object for LDA model using gensim library
        Lda = gensim.models.ldamodel.LdaModel

        # running and Trainign LDA model on the document term matrix.
        ldamodel = Lda(doc_term_matrix, num_topics=num_topics, id2word = dictionary)
        # topic = ldamodel.print_topics(num_topics=num_topics, num_words=num_words)
        label = []
        for i in range(num_topics):
            label.append(ldamodel.show_topic(topicid=i, topn=num_words))

        # show the result
        return label


    def label_detect(self, text_list, num_topics=5, num_words=5):
        # read the selected titles
        docs = []
        for text in text_list:
            docs.append(self.preprocess(text))
        label = self.lda(docs, num_topics, num_words)
        return label

# how to use it
if __name__ == "__main__":
    text_list = ['在线社交网络：在Facebook和Twitter个体关系网中发现的人类认知约束', '线下社交：网络之外，才是真正属于你的圈子']
    l = LDA()
    print(l.label_detect(text_list, num_topics=5, num_words=5))
