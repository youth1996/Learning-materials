#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
print()
'''
2.写一个ATM管理系统：
功能：登陆，开户，查询，存款，取款，退出等

1.首先进入欢迎页面：
**********************
*                    *
*  welcome to bank   *
*                    *
**********************
2.让用户选择要操作：
**********************
*  1.登陆   2.开户    *
*  3.查询   4.取款    *
*  5.存款   6.退出    *
**********************
3.在执行登陆需要输入卡号并且输入密码，当卡号与密码一致的时候
进入系统。

4.当用户名不存在的时候，需要先开户的时候，
输入1.身份证号码 2.用户名  3.电话号码  4.预存款  5.密码  6.重复确认密码
开户成功之后，返回一个卡号，随机的，并且不重复的【6位0~9组成】

5.查询的时候要求先登陆【登陆的时候要保存卡号】
'''
import time
import random


def welcome():
    print('''
**********************
*                    *
*  welcome to bank   *
*                    *
**********************
    ''')

def choice():
    print('''
**********************
*  1.登陆   2.开户    *
*  3.查询   4.取款    *
*  5.存款   6.退出    *
*  7.转账   8.改密    *
*  9.锁卡   0.解锁    *
**********************
    ''')
    num = input("请输入您要选择的项目：")
    return num

def getCardNum(userDict):
    cardlist = list(userDict)
    while True:
        cardnum = ""
        for x in range(6):
            cardnum += str(random.randrange(10))
        if cardnum in cardlist:
            continue
        else:
            break

    return cardnum

def kaihu(userDict):
    idcard = input("请输入您的身份证号码：")
    name = input("请输入您的姓名：")
    phonenum = input("请输入您的电话号码：")
    money = int(input("请输入您的预存款："))
    if money>0:
        psd = input("请设置您的密码：")
        psd2 = input("请重复确认您的密码：")
        if psd == psd2:
            #获取卡号
            cardnum = getCardNum(userDict)
            #创建字典【用户信息】
            return {"idcard":idcard,"name":name,"phonenum":phonenum,"money":money,"psd":psd,"cardnum":cardnum,"isLock":False}
        else:
            print("两次输入密码不一致，开户失败！！！")
            return
    else:
        print("预存款不能小于0，开户失败！！！")
        return

def login(userDict):
    cardnum = input("请输入您的卡号：")
    user = userDict.get(cardnum)
    if  user == None:
        print("用户名不存在，请查证后登陆")
        return
    else:
        if user["isLock"]:
            print("此卡已锁定，请解锁后登陆。。。")
            return
        for x in range(1,4):
            password = input("请输入您的密码：")
            if password == user.get("psd"):
                print("登陆成功")
                return cardnum
            else:
                print("密码错误,您还剩%d次机会"%(3-x))
                continue
        else:
            print("三次密码错误，此卡已被锁定。。。")
            userDict[cardnum]["isLock"] = True
            return

def search(userDict,cardnum):
    print("您当前的余额为%d"%userDict[cardnum]["money"])


def unLock(userDict):
    cardnum = input("请输入卡号：")
    user = userDict.get(cardnum)
    if user :
        idcard = input("请输入本人身份证号码：")
        phonenum = input("请输入预留电话号码：")
        name = input("请输入本人姓名：")
        if idcard == user["idcard"] and phonenum == user["phonenum"] and name==user["name"]:
            #解锁
            userDict[cardnum]["isLock"] = False
            print("恭喜你，解锁成功！！！")
        else:
            print("信息有误，解锁失败。。。。")
    else:
        print("此卡不存在。。。")
        return



welcome()
userDict = {}
islogin = None
while True:
    time.sleep(1)
    num = choice()
    if num == "1":
        print("登陆")
        islogin = login(userDict)
    elif num == "2":
        print("开户")
        user = kaihu(userDict)
        if user !=None:
            #获取到用户的卡号
            cardnum = user["cardnum"]
            #将用户存储到用户字典中
            userDict[cardnum] = user
            print("恭喜你开户成功！，您的卡号为%s，请牢记"%cardnum)

    elif num == "3":
        if islogin:
            print("查询")
            search(userDict,islogin)
        else:
            print("未登录，请登陆后查询")
    elif num == "4":
        print("取款")
    elif num == "5":
        print("存款")
    elif num == "6":
        print("退出")
        break
    elif num == "7":
        print("转账")
    elif num == "8":
        print("改密")
    elif num == "9":
        print("锁卡")
    elif num == "0":
        print("解锁")
        unLock(userDict)


    else:
        print("输入选项有误，请重新选择；")

