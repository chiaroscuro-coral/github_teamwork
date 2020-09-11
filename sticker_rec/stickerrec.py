 #!/usr/bin/env python
# coding: utf-8

from snownlp import SnowNLP
from gensim.test.utils import common_texts
from gensim.models import Word2Vec
from gensim.test.utils import get_tmpfile
from gensim.models import KeyedVectors
from gensim.test.utils import datapath
import glob as glob

wv_from_text = KeyedVectors.load_word2vec_format('/Users/files/Desktop/sgns.weibo.bigram-char', binary=False)


def stickersrecommendation(input_sentence):
    


    # In[78]:



    # In[8]:



    # In[80]:



    # In[12]:


    similarity = wv_from_text.similarity('快乐', '开心')


    # In[11]:


    wv_from_text.n_similarity(['难过'], ['开心'])


    # In[ ]:



    


    # In[29]:


    # seperating out characters and create a list, excluding stopwords. To be integrated into the following function
    #stopwords_list = []

    #with open("/Users/files/Desktop/stopwords-master/cn_stopwords.txt") as f:
        #for line in f:
            #stopwords_list.append(line)
            

    #stopwords_list_c = []
            
                    
    #for stopword in stopwords_list:
        #stopwords_list_c.append(stopword.replace('\n',''))

    #stopwords_list_cc = []

    #for stopword in stopwords_list_c:
        #if len(stopword) == 1:
            #stopwords_list_cc.append(stopword)


    stopwords_list = ['$', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_', '“', '”', '、','《', '》','个','仍','从','但','之','乎', '乘', '也','于','些', '亦', '人','今','们','俺','兮','其','则','将','就','并','当','很','我','或','他','她','才','所','把','拿','故','既','是','替','最','有','本','某','此','每','各','比','沿','由','的','着','者','而','自','虽','，', '：', '；',]



    #charlist=[]
    #for i in range(0,len(input_sentence)):
    #    charlist.append(input_sentence[i])
    #print(charlist)


    # In[24]:


    def seperate_sentence_into_chars (sentence):
        charlist = []
        for char in sentence:
            charlist.append(char)
        return charlist


    # In[38]:


    # In[67]:



    def compare_input_emoji_sim (input_sentence, emoji_tags_list):
        #seped_input_sentence stands for input sentenced seperated by snowNLP
      
        # trans_input_sentence=translation(input_sentence)
        trans_input_sentence=input_sentence
        input_chars_list = seperate_sentence_into_chars(trans_input_sentence)
        seped_input_sentence = SnowNLP(trans_input_sentence)
        input_words_list = seped_input_sentence.words
        
        
        # delete elements not in the vocab
        for char in input_chars_list:
            if (char not in wv_from_text.wv.vocab.keys()) or (char in stopwords_list):
                input_chars_list.remove(char)
                
        for word in input_words_list:
            if word not in wv_from_text.wv.vocab.keys():
                input_words_list.remove(word)
                    
        
        
       
        emoji_chars_list = []
        
        for tag in emoji_tags_list:
            for char in tag:
                if (char not in wv_from_text.wv.vocab.keys()) or (char in stopwords_list):
                    tag = tag.replace('char', '')
            emoji_chars_list += seperate_sentence_into_chars(tag)

        emoji_words_list = []
        
        for tag in emoji_tags_list:
            tag = SnowNLP(tag)
            tag_words = tag.words
            # delete elements not in the vocab
            for word in tag_words:
                if word not in wv_from_text.wv.vocab.keys():
                    tag_words.remove(word)
            
            emoji_words_list += tag_words
            
            
            
            
        sim = wv_from_text.n_similarity(input_words_list + input_chars_list, emoji_words_list + emoji_chars_list)
        return sim
        #return input_words_list


    # In[71]:


    # 60 emoji tags

    list_1 =['疑惑','困惑','迷茫','不懂','疑问','????','？？？？']
    list_2 =['为啥','为什么','困惑','好迷','迷惑','????','？？？？']
    list_3 =['太迷了','很迷','问题','提问','无语','????','？？？？']
    list_4 =['非常迷惑','难以置信','无法想象','没法相信','天哪','????','？？？？']
    list_5 =['什么','嗯','很奇怪','异常','？','?']
    list_6 =['就这','这','无语','语塞','。。。。。。','我无话可说']
    list_7 =['无言以对','无语了','很无语','啊这','心情复杂','。。']
    list_8 =['无奈','额','无语','不想说话','无言以对','。。']
    list_9 =['美女语塞','无语辽','不想回复','呃','额','。。']
    list_10 =['流汗','难说','不想说','尴尬','郁闷','。。。。。。。']
    list_11 =['尴尬','无语','心情复杂','难说','额','。。']
    list_12 =['很无语','非常尴尬','唉','无言以对','不想说话']
    list_13 =['滚!','滚吧','走开','讨厌','滚开']
    list_14 =['生气','走开','气愤','瞪','眼神']
    list_15 =['讨厌','恶心','别过来','走开','起开','这么可怕么','吓死宝宝了']
    list_16 =['嫌弃','厌恶','不喜欢','难受','离远点','呵呵','哼','呵呵']
    list_17 =['很嫌弃','很讨厌','滚','有病','有毒','哼']
    list_18 =['眼神','嫌弃','垃圾','菜','你不行啊','爬吧']
    list_19 =['白眼','讨厌','走开','滚','无语了','这都行']
    list_20 =['极度嫌弃','非常讨厌','泥奏凯','太不行','斜眼','就这吗？']
    list_21 =['伤心死了','悲痛欲绝','伤心欲绝','哭了','大哭','呜呜呜呜呜']
    list_22 =['无语了','没事','没事才怪','哭唧唧','挺伤心','呜呜呜呜呜']
    list_23 =['委屈','超想哭','难受','大哭','流泪','呜呜呜呜呜','我好冤啊']
    list_24 =['悲伤','不快乐了','难过','伤感','痛苦','呜呜呜呜呜']
    list_25 =['哭了','枯了','难受','抱住自己','有点难过','呜呜']
    list_26 =['高兴','开心','快乐','幸福','满足','哇塞','真的吗哈哈']
    list_27 =['嗨','非常开心','期待','欧耶','棒','啊啊啊啊','哈哈哈哈','太爽了']
    list_28 =['开心鸭','很快乐','嘻嘻','哈哈','开森']
    list_29 =['温暖','幸福','满足','笑脸','舒服']
    list_30=['开心','高兴','好消息','好事情','真的开心']
    list_31 =['天呐','妈呀','难以置信','等不及','激动','真的吗哇哇哇']
    list_32 =['天呐','快乐','难以置信','冲！！','激动','啊啊啊啊啊啊啊']
    list_33 =['快乐','激动','好奇','八卦','啊什么','唠这个我可不困了','嗯？！']
    list_34 =['兴奋到模糊','开心','好激动','等不及','啊啊啊']
    list_35=['冲','啊啊啊','上','别怕','加油！','你能行的']
    list_36=['害怕','妈呀','可怕','天','救命','好怕怕']
    list_37=['害怕','好可怕','天','救命','瑟瑟发抖']
    list_38 =['害怕','好可怕','天','抱住自己','瑟瑟发抖']
    list_39 =['害怕','好可怕','天','惊恐','瑟瑟发抖']
    list_40 =['害怕','好可怕','天','惊恐','啥','吓傻了','啊天哪！']
    list_41 =['害怕','好可怕','天','哭了','瑟瑟发抖','呜呜我好怕']
    list_42=['弄死','再说一遍','砍你','气死','生气','我生气了','哼你敢','胆子真肥']
    list_43=['不想和你说话','懒得理你','再说一遍','友尽','拜拜']
    list_44=['打','再说一遍','气死','弄死','拜拜','打死你哦']
    list_45=['啥','没睡醒','再说一遍','你没事吧','气死','你认真的吗','？']
    list_46=['滚','再说一遍','气死','出去','你走']
    list_47=['我生气了','不气才怪','没事是不可能的','我忍不了了','你敢？']
    list_48=['冷漠','不管','不关心','不关我事','才不管你','呵呵']
    list_49=['好的','没问题','可以','接受','同意']
    list_50 =['好的','没问题','可以','接受','好呀','嗯嗯']
    list_51=['好的','可以','同意','开心','啦啦啦啦','就是高兴']
    list_52=['嗯','好','不想回','行吧','都可以','随你便吧']
    list_53=['嗯嗯','好','没问题','可以','好主意']
    list_54=['同意','对','没问题','不反对','支持','我也觉得','附议']
    list_55=['没意见','可以','随便','随意','都可以']
    list_56=['好的','没问题','可以','好主意','同意']
    list_57=['随便你','都可以','随意','不管','好的','没问题']
    list_58=['好吧','行吧','这样','原来如此','这']
    list_59=['谢谢','感谢','大佬','鸣谢','感激']
    list_60=['好的','没问题','可以','好主意','同意']
    list_61 =['中秋快乐！','端午节快乐！','春节快乐！','同乐','节日快乐！']
    list_62 =['同乐','哈哈哈','笑死我了','好扯','那祝它节日快乐！']
    list_63 =['开心','可爱','小猪佩奇','过生日','祝本宝宝生日快乐！']
    list_64 =['真心的祝福','开心','幸福','生日快乐','天天开心']
    list_65 =['祝生日快乐！','这是一个特别的日子','生日快乐','送你蛋糕','幸福开心','生快']
    list_66 =['生日快乐','开心','高兴','蛋糕','礼物','祝生日快乐！','生快']
    list_67 =['节日快乐','开心','祝福','高兴','兴奋']
    list_68 =['过节','同乐','今天是个特殊的日子','节日快乐','快乐']
    list_69 =['节日快乐','比心','幸福','爱心','母亲节快乐！']
    list_70 =['捧花','一束鲜花','送花','谢谢','祝福你']
    list_71 =['小兔子','可爱','嗨','打招呼','你好呀！']
    list_72 =['嗨','打招呼','招手','您好','你好']
    list_73 =['你好','很高兴认识你','嗨','伙伴们','挥手']
    list_74 =['抱拳','嗨','给一个问候','在','你好']
    list_75 =['可爱的问候','嗨','在','你好','哈喽']
    list_76 =['很开心认识你','开心','可爱','你好','嗨']
    list_77 =['晚安','早睡','好梦','睡了','回聊']
    list_78 =['早安安','早上好','早','小宝贝','小可爱']
    list_79 =['早上好','早','起床','阳光','太阳']
    list_80 =['晚安','睡觉','早点休息','不早了','困']
    list_81 =['感谢','谢谢','感激','开心','感恩']
    list_82 =['谢谢你','撒花','感恩','谢谢！','献花']
    list_83 =['谢谢你','感谢','谢谢','不客气','快乐']
    list_84 =['饿了吗','想吃饭吗','吃饭吗','到底吃不吃','一起吃吗？？']
    list_85 =['快点回复','不回复？','狗不理','不回消息吗？','在干嘛']
    list_86 =['随便都行','没意见','爱咋咋地','不知道','都可以']
    list_87 =['你是猪','煞笔','打电话','蠢货','欠揍']
    list_88 =['丑','想得美','你真丑','演戏','调戏']
    list_89 =['紧张','沉默','凝重','缓解尴尬','尴尬气氛','空气突然安静']
    list_90 =['穷','嘲讽','嘲笑','没钱了','你没有钱','别做梦了']
    list_91 =['看戏','看热闹','吃瓜','好奇','闲得很']
    list_92 =['爱你','热爱','比心','爱情','红心']
    list_93 =['傻','笨','蠢','二百五','废物']
    list_94 =['拜拜就拜拜，下一个更乖','结束聊天','无语','再也不见','丢手雷']
    list_95 =['怎么办又想你了','想念','喜欢','想见你','唉']
    list_96 =['收到了假红包','运气真差','没钱','穷','收红包','再发一次红包']
    list_97 =['发红包','瞎扯淡','等待红包','废话太多','该发红包了']
    list_98 =['红包','发钱','抢红包','大方','该发红包了']
    list_99 =['发红包','不要脸','妖娆','厚脸皮','调皮']
    list_100 =['饿死了','饥饿','厚脸皮','太饿了','贪心']
    list_101 =['饿死了','饥饿','厚脸皮','太饿了','贪心']
    list_102 =['吃饭','吃了吗','约饭','请客','饿了吗']
    list_103 =['午餐','吃什么','饿了','约饭','请客','关心']
    list_104 =['快点','吃饭','冲','饿死了', '终于吃饭']
    list_105 =['没钱','穷','买不起','哭泣','枯了']
    list_106 =['嘲笑','哈哈哈','穷','没钱','浪费']
    list_107 =['丑','自恋','难看','哭泣','丑哭','滚']
    list_108 =['吐血','无语','难受','难过','有毒','气死']
    list_109 =['平安','小心','嘲讽','没事','没关系']
    list_110 =['可爱','萌','我好可爱','期待','喵喵','小激动']
    list_111 =['懂','了解','知道','噢','原来如此']
    list_112 =['略略略','轻松','拿我怎么样','惬意','吐舌','垃圾']
    list_113 =['有病','智障','有毒','傻','嫌弃','蠢']
    list_114 =['聪明','机智如我','开心','我好棒','哈哈哈']
    list_115 =['呵呵','无语','闭嘴','不会聊天','无言以对']
    list_116 =['八卦', '吃瓜','吃瓜群众','分享','哈哈','偷笑']
    list_117 =['干杯','太棒了','庆祝','赞同','妙啊','一拍即合']
    list_118 =['嫌弃','就知道吃','减肥','体重','胖']
    list_119 =['啥','再说一遍?','没听见','不懂','真的吗']
    list_120 =['知识就是力量','去学习！','努力','好学不倦','好好学习']



    # In[76]:

    sim_list = []
    for i in range(120):
        emoji_tags_list = eval('list_' + str(i+1))
        sim = compare_input_emoji_sim (input_sentence, emoji_tags_list)
        sim_list.append(sim)



    # In[ ]:


    sim_indexes = []
    slc = []
    for i in range(len(sim_list)):
        slc.append((sim_list[i], i))
    slc = sorted(slc, key=lambda x: x[0], reverse=True)
    sim_indexes = []
    for i in range(4):
        sim_indexes.append(slc[i][1])

    '''
    for i in range(4):
        sim_index = sim_list.index(max(sim_list))
        print(sim_index, sim_list[sim_index])
        sim_list[sim_index] = -1
        sim_indexes.append(sim_index) 
        
    print(sim_indexes)
    '''
    stickers=sorted(glob.glob('/Users/files/Desktop/emojis/???.jpg'))
    assert len(stickers) == 120
    fileNames=[]
    for sim_index in sim_indexes:
        assert sim_index < 120
        assert sim_index >= 0
        file_path = stickers[sim_index]
        file_path = '/' + '/'.join(file_path.split('/')[-2:])
        fileNames.append(file_path)
    #print
    return(fileNames)
  







