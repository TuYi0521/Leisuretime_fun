import itchat
import re
import jieba

# 先登录，扫二维码登录微信
itchat.login()
# 获取好友列表，返回的是json信息
friends = itchat.get_friends(update=True)[0:]
# 打印好友列表信息
# print(friends)
tList = []
male = female = other = 0
for i in friends:
    # # 获取个性签名,替换掉span，class，emoji
    # signature = i["Signature"].replace(" ", "").replace("span", "").replace("class", "").replace("emoji", "")
    # # 正则匹配过滤掉emoji表情，例如emoji1f3c3等
    # rep = re.compile("1f\d.+")
    # signature = rep.sub("", signature)
    # tList.append(signature)
    sex = i['Sex']
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other += 1
total = len(friends[1:])

# from pyecharts import Pie
#
# attr = ['男', '女', '其他']
# vl = [int(male),int(female),int(other)]
# pie = Pie('sex')
# pie.add("",attr,vl, is_label_show= True)
# pie.render()

print("男性好友： %.2f%%" % (float(male) / total * 100) + "\n" +
      "女性好友： %.2f%%" % (float(female) / total * 100) + "\n" +
      "不明性别好友： %.2f%%" % (float(other) / total * 100))


def get_var(var):
    variable = []
    for i in friends:
        value = i[var]
        variable.append(value)
    return variable


# 调用函数得到各变量，并把数据存到csv文件中，保存到桌面
NickName = get_var("NickName")
UserName = get_var("UserName")
Sex = get_var('Sex')
Province = get_var('Province')
City = get_var('City')
Signature = get_var('Signature')
from pandas import DataFrame

data = {'NickName': NickName, 'UserName': UserName, 'Sex': Sex, 'Province': Province,
        'City': City, 'Signature': Signature}
frame = DataFrame(data)
frame.to_csv('ty.csv', index=True)

siglist = []
for i in friends:
    signature = i["Signature"].strip().replace("span", "").replace("class", "").replace("emoji", "")
    rep = re.compile("1f\d+\w*|[<>/=]")
    signature = rep.sub("", signature)
    siglist.append(signature)
text = "".join(siglist)

wordlist = jieba.cut(text, cut_all=True)
word_space_split = " ".join(wordlist)


import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import numpy as np
import PIL.Image as Image
coloring = np.array(Image.open("C:/Users/#TUYI#/Desktop/1.jpg"))
my_wordcloud = WordCloud(width=1024, height=600,
                         font_path='‪C:/Windows/Fonts/simsun.ttc',
                         background_color="white", max_words=200,
                         mask=coloring, max_font_size=60, random_state=42, scale=1,
                         ).generate(word_space_split)

image_colors = ImageColorGenerator(coloring)
plt.imshow(my_wordcloud.recolor(color_func=image_colors))
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()