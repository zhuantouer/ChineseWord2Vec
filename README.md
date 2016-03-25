#中文word2vector词向量实现

nlp小白一枚，网上没有找到中文训练好的word2vec模型，自己动手丰衣足食

说明：[word2vector](https://code.google.com/p/word2vec/)背后的原理

暂时不做深究，这个项目的主要目的就是尽可能快的训练一个中文词向量模型，训练好的

模型主要用于“CNN在NLP中的应用(成型后再push更新链接)”这个项目。

后期我会把模型文件上传到云盘供大家玩玩，也会做一个在线的api，敬请期待。。。

【nlp门外汉，大神轻喷，文中有什么错误，或者有什么更好的方法，望发issue告知，不胜感激！】


### 环境
- ubuntu14.04lts(VM)
- python 2.7.11
- 依赖：numpy, scipy, gensim, opencc, jieba


from scratch

### 1.获取语料库
- 搜狗实验室 http://www.sogou.com/labs/resources.html?v=1 (反正我是下载不下来)
- 维基百科   https://dumps.wikimedia.org/zhwiki/latest/zhwiki-latest-pages-articles.xml.bz2 (办了信用卡我就去捐钱！！！)
原始语料文件：`zhwiki-latest-pages-articles.xml.bz2`   wiki最后更新时间：06-Mar-2016 21:00          大小：1.2G


### 2.语料库预处理
- gensim解析语料库
 gensim解析bz2语料(不用解压)，参见脚本： 。。。。。。。。。。
 
 ```python
 python parse_wiki.py zhwiki-latest-pages-articles.xml.bz2 corpus.zhwiki.txt
 ```
 
 生成 `corpus.zhwiki.txt` 889.4M
 
- 简繁体转换(opencc)
 把语料中的繁体转换成简体，台湾同胞请跳过此步骤【握手】
 
```
sudo apt-get install opencc
opencc -i corpus.zhwiki.txt -o corpus.zhwiki.simplified.txt -c zht2zhs.ini
```

- 去除英文和空格
文档中还是有很多英文的，一般是文章的reference。里面还有些日文,罗马文等，这些对模型影响效果可以忽略吧，
我没做实验，只是简单的去除了空格和英文。

```
python remove_en_blank.py corpus.zhwiki.simplified.txt corpus.zhwiki.simplified.done.txt 
```
生成 corpus.zhwiki.simplified.done.txt （766.6M）

- 分词
这里以 空格 做分割符  `-d ' '`

```
pip install jieba
python -m -d ' ' jieba corpus.zhwiki.simplified.done.txt > corpus.zhwiki.segwithb.txt
```

生成 `corpus.zhwiki.segwithb.txt` （901.3M）

虚拟中训练估计要好久，而且会把电脑拖瘫，先告一段落，去作腾讯的笔试题，晚上有个在线笔试~
恩，对，还要全程视频监控【微笑】
