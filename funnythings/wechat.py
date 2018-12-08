import itchat
import jieba
import re
import os

# 登录微信
itchat.login()

# 获取好友信息
friends = itchat.get_friends(update=True)[0:]
siglist = []
# 获取个性签名，并去除里面的span，class，emoji等
for i in friends:
    signature = i['City'].strip().replace('span', '').replace('class', '') \
        .replace('emoji', '')
    rep = re.compile('1f\d+\w*|[<>/=""\n]')
    signature = rep.sub('', signature)
    siglist.append(signature + '\n')
text = ''.join(siglist)
# 分词
wordlist = jieba.cut(text, cut_all=True)
word_space_split = ''.join(wordlist)
# 开始画词云
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import numpy as np
import PIL.Image as Image

coloring = np.array(Image.open(os.path.join("C:/Users/#TUYI#/Desktop/1.jpg")))
my_wordcloud = WordCloud(font_path='‪C:/Windows/Fonts/simsun.ttc',
                         background_color='black', max_words=2000,
                         mask=coloring, max_font_size=60, random_state=42,
                         scale=2).generate(word_space_split)
image_colors = ImageColorGenerator(coloring)
plt.imshow(my_wordcloud.recolor(color_func=image_colors))
plt.imshow(my_wordcloud)
plt.axis('off')
plt.show()