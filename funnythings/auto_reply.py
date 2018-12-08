#coding=utf-8
import itchat,time
from itchat.content import *

'''
##自动回复的功能
@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    return msg['Text']
'''
# @itchat.msg_register([TEXT,MAP,CARD,NOTE,SHARING])
# def text_reply(msg):
#     itchat.send('%s: %s'%(msg['Type'],msg['Text']),msg['FromUserName'])

# @itchat.msg_register([PICTURE,RECORDING,ATTACHMENT,VIDEO])
# def download_files(msg):
#     msg['Text'](msg['FileName'])
#     return '@%s@%s'%({'Picture':'img','Video':'vid'}.get(msg['Type'],'fil'),msg['FileName'])

@itchat.msg_register(FRIENDS)
def add_friend(msg):
    itchat.add_friend(**msg['Text'])# 该操作将自动将好友的消息录入，不需要重载通讯录
    itchat.send_msg('Nice to meet you!',msg['RecommendInfo']['UserName'])

# @itchat.msg_register(TEXT,isGroupChat=True)
# def text_reply(msg):
#     if msg['isAt']:
#         itchat.send(u'@%s\u2005I received: %s '%(msg['ActualNickName'],msg['Content']),msg['FromUserName'])

@itchat.msg_register([PICTURE,TEXT])
def simple_reply(msg):
    if msg['Type'] == TEXT:
        ReplyContent = 'I received message, and I will response ASAP: '+msg['Content']
    if msg['Type'] == PICTURE:
        ReplyContent = 'I received picture: '+msg['FileName']
    itchat.send_msg(ReplyContent,msg['FromUserName'])

# @itchat.msg_register([PICTURE,TEXT],isGroupChat=True)
# def simple_reply(msg):
#     users = itchat.search_friends(name=u'测试23')#通讯录中好友备注名
#     userName = users[0]['UserName']
#     if msg['Content'] == "+1":
#         itchat.send(u'%s\u2005: %s '%(msg['ActualNickName'],msg['Content']),toUserName=userName)

itchat.auto_login(hotReload=True)
#向文件助手发送消息
#itchat.send('Hello filehelper',toUserName='filehelper')
itchat.run()