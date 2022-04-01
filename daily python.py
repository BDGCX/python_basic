# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 14:32:00 2022

@author: bdgcx
"""

'''
输出函数,由程序员提问，计算机作答
'''
print('Hello world')

'''
赋值
'''
num=100
num

'''
变量：数值变量、字符串变量和逻辑变量
'''
'''
输入函数，由计算机提问程序员作答得到的任何回答类型都是str
'''
age=input('你几岁了？')
#在出现你几岁了?后输入20
print(age)
#就会输出20
type(age)
#发现20的数据类型是str，也就是字符串，需要转换为数值时
age=int(age)

'''
分支结构(选择)
'''
#以ATM取款为例
balance=1000 #银行卡余额
money=input('请输入取款金额:')
money=int(money) #将输入的金额由str转换为int类型
#判断取款金额与银行卡余额，一定记住冒号
if money <=balance:
    balance=balance-money  #计算新的余额
    print('交易成功，余额为：'+str(balance))
else: 
    print('交易失败，余额不足，余额为：'+str(balance))

#根据BMI判断身材 是否合理
height = float(input("输入身高（米）："))
weight = float(input("输入体重（千克）："))
bmi = weight / (height * height)  #计算BMI指数

if bmi<18.5:
    print("BMI指数为："+str(bmi))
    print("体重过轻")
elif bmi>=18.5 and bmi<24.9:
    print("BMI指数为："+str(bmi))
    print("正常范围，注意保持")
elif bmi>=24.9 and bmi<29.9:
    print("BMI指数为："+str(bmi))
    print("体重过重")
else:
    print("BMI指数为："+str(bmi))
    print("肥胖")

#判断游戏用户是否未成年    
import sys
age = int( input("请输入你的年龄：") )
if age < 18 :
    print("警告：你还未成年，不能使用该软件！")
    print("未成年人应该好好学习，读个好大学，报效祖国。")
    sys.exit() #sys 模块的 exit() 函数用于退出程序
else:
    print("你已经成年，可以使用该软件。")
    print("时间宝贵，请不要在该软件上浪费太多时间。")
print("软件正在使用中...")

'''
循环结构
'''
#for..in..循环,for循环会遍历数据集中的每一个元素，与while有放行条件不同
for i in range(1,6):
    print(i)

for ch in "python":
    print(ch)
#while循环，有放行条件，直到满足条件循环停止
a=1
while a<=5:#放行条件
    print(a)
    a=a+1

v='Hello world'
cnt=2
while cnt<7:
    print(v)
    cnt=cnt+1
#break中断循环
while True: #True代表无条件放行
    answer=input('还能卷吗？')
    if answer=='yes':
        print('加油')
    else:
        print('那就躺平吧')
        break#就此停止不再发问

#continue继续循环
#能不能跑圈为例
circle=0
for i in range(1,11):
    answer=input('能跑吗')
    if answer!='yes':
        continue
    #circle=circle+1，简写见下
    circle+=1
#print('一共跑了'+str(circle)+'圈')
print('一共跑了',circle,'圈')

day=0
for i in range(1,8):
     answer=input('还能卷吗?:')
     if answer!='yes':
         continue
     day+=1
     
print('本周你共卷了',str(day),'天','，','躺平',7-day,'天','哈哈哈')
     
'''
列表
''' 
lst=[40,41,42,43,44]
print(lst)
lst[1]#输出lst中的第2个元素
lst.append(100)#添加元素
lst 
lst[1]=100#修改lst中的第2个元素为100
lst
lst.remove(42)#删除lst中42
lst
#列表元素的遍历        
for i in range(0,len(lst)):
    print(lst[i])

for item in lst:
    print(item)

#索引
lst[1]#输出lst中的第2个元素，正索引为从左往右进行索引，且标号从0开始
lst=[40,41,42,43,44]
lst1=lst[2:]#从标号（索引）的位置开始一直切到最后
lst1
lst2=lst[1:4]#从标号（索引）的位置开始一直切到终止标号的左侧，因为python不包含右侧边界
lst2
lst3=lst[-1]#python中负索引代表从右往左索引，且标号从-1开始
lst4=lst[-3:-1]
lst4

'''
字典{'key':value,'key':value}其中key不可重复，value可重复
其中的元素排列没有顺序，不能进行指定顺序的索引，只能根据key进行索引
'''       
dictionary={'41':10,'42':8,'43':2}
dictionary['41'] 
dictionary['44']=100  #在字典中新增
del dictionary['42']
dictionary
#字典遍历
for i in dictionary:
    print(i,dictionary[i])

'''
集合,其中的元素排列没有顺序，不能进行指定顺序的索引
'''    
aggregate={'41','42','43'}
aggregate.add('44')
aggregate
aggregate.remove('42')
aggregate
#集合遍历
for item in aggregate:
    print(item)
s=list(aggregate)#转换成列表就可以索引了
'''
元组，不能新增、修改和删除，只能查看
'''
tuple1=('41','42','43','44')
tuple1[1]
#元组遍历
for i in tuple1:
    print(i)

'''
函数
'''
#定义一个函数
def fun(x):
    #函数体
    print(x)
fun(10)
def fun(x):
    print(x/10)
fun(20)

def calc(a,b):
    return a+b
x=calc(10, 20)
x

'''
类和对象，定义在类里的函数是属性、方法
'''
#女孩类
class Girl:
    def __init__(self,hair,name,age):
        self.hair=hair
        self.name=name
        self.age=age
    def eat(self):
        print(self.name,'小女孩，在吃金拱门')
#创建对象
girl=Girl('long hair', 'Marry', 5)
girl.name
girl.eat()

class human: #定义一个human类 
    def __init__(self,name,height,weight):#定义对象的方法
        self.name=name#对象的属性
        self.height=height
        self.weight=weight
    def shot(self):#定义对象的方法
        print(self.name,'slam dunk')
#创建对象        
Jordan=human('Jordan', 188, 90)
#查看对象的方法
Jordan.shot()
#查看对象的属性
Jordan.height
Jordan.weight

'''
模块
一个.py的文件就是一个模块
在.py文件里定义类，可以定义函数
'''
num=10
#num直接写在.py文件中是全局变量
def fun(x):#函数体
    k=100#局部变量
    print(x)
#如何使用别人写好的模块
#下载模块
pip install openpyxl
#加载模块
import openpyxl

def calc (a,b):
    return a+b
#上述函数以主程序运行
if __name__=='__main__':
    c=calc(10, 20)
    print(c)
#当要在别的.py文件中运行calc时，只会运行calc函数，而不运行主程序运行的代码

'''
os模块简介_路径操作
'''   
import os
#获取当前工作目录
os.getcwd()
#windows系统目录结构："C:\\Users\\xxx\\Desktop" 使用\\反斜线,也可以/
#Linux系统目录结构："/home/xxx/"
#Mac系统目录结构"/Users/xxx/Desktop/"

#python路径连接
os.path.join('C:\\Users\\bdgcx\\OneDrive', 'python')
#绝对路径和相对路径，绝对路径就是windows系统目录结构显示，相对路径就好比绝对路径里的文件的位置
#例：跟快递员说公司的位置，跟单位同事说自己在2楼是相对于自己工作单位的2楼
#更换工作目录
os.chdir('Desktop/python/datasets')#换成自己的工作目录
#查看当前目录下所有文件和文件夹
os.listdir()
#文件遍历
lst=os.listdir()
for item in lst:
    print(item,type(item),len(item))
#也可以查看指定目录下的文件和文件夹
os.listdir('C:/Users/bdgcx/OneDrive')
os.listdir('../Rdata')

lst=os.scandir()
for file in lst:
    print(file, type(file),file.name,file.path,file.is_dir())
#file.is_dir()是查看是否是文件夹

#遍历文件夹下所有文件及其子文件
os.walk('./')
for dirpath,dirnames,files in os.walk('./'):
    print('发现文件夹',dirpath)#当前目录下的文件夹
    print(dirnames)#获取dirpath下的子文件夹
    print(files)#获取dirpath下的子文件夹中的文件
    
'''
搜索文件
'''
#搜索匹配文件
#1.字符串内置方法
import os
lst=os.listdir()
lst
for item in lst:
    if item.endswith('.py'):#从众多文件中查找结尾为.py的文件
        print(item)

for item in lst:
    if item.startswith('no'):#从众多文件中查找开头为no的文件
        print(item)

for item in lst:
    if item.startswith('no') and item.endswith('.txt'):#从众多文件中查找开头为no结尾为.txt的文件
        print(item)

#2.使用glob模块
# *通配符，匹配所有0个-多个字符
# ?匹配任意单个字符
# [seq]匹配seq中的任何字符
# [!seq]匹配任何不在seq中的字符
import glob
glob.glob('*.py')#以.py结尾的所有文件
glob.glob('demo*.py')#以demo开头.py结尾的所有文件
glob.glob('demo?.py')#以demo开头+任意1个字符+.py结尾的所有文件
glob.glob('demo[1-5].py')#以demo开头+1-5中任意一个字符+.py结尾的所有文件
glob.glob('demo[!1-5].py')#以demo开头+1-5中任意一个字符+.py结尾的所有文件
glob.glob('demo[1，3，5，7].py')#以demo开头+1，3，5，7中任意一个字符+.py结尾的所有文件
glob.glob('**/*.py'，recursive=True)#以.py结尾的所有文件及文件夹中的子文件
#**/表示任意层文件夹

#3.fnmatch模块,验证文件名是否符合某种模式
import fnmatch
fnmatch.fnmatch('demo8.py', 'demo?.py')

'''
查询文件详细信息
'''
import os
for file in os.scandir():
    print(file.stat())
'''
st_size 文件体积大小(bytes)
st_atime 文件最近的访问时间
st_ctime windows下表示创建时间
st_birthtime Mac下表示创建时间
st_mtime 文件最近的修改时间
'''
#时间转换
import time
time.ctime(1591943466)#1591943466是Unix时间戳，单位是second

import datetime
that_time=datetime.datetime.fromtimestamp(1591943466)
print(that_time)
type(that_time)
print(that_time.year,that_time.second)

import os
os.stat('python study.py')

#从指定路径下找到今天下午2点之前创建的文件
import os
import datetime
for file in os.scandir():
    that=file.stat()
    start_time=that.st_ctime
    user_time=datetime.datetime.fromtimestamp(start_time)
    hour=user_time.hour
    if hour<14:
        print(that)

'''
读入和写入文件，实际中直接用pandas,openpyxl等模块
'''
#读入文件
f=open('mtcars.csv','r',encoding='utf-8')
text=f.readlines()
print(text)
f.close()
#with... as .. 上下文管理器，'r'表示读取，'w'表示写入，'a'表示追加写入
with open('mtcars.csv','r',encoding='utf-8') as f:
    print(f.readlines())
   
#写入文件
with open('a.txt','w',encoding='utf-8') as file:#如果a文件无内容，直接写入内容，a文件已存在内容则清空内容重新写入
    file.write('Hello'\n)
    file.write('world')

with open('a.txt','a',encoding='utf-8') as file:#a文件已存在内容在原文件基础上继续追加
    file.write('Hello'\n)
    file.write('world') 



    

    









        


