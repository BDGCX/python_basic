# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 13:43:18 2022

@author: bdgcx
"""
'''
python从0开始，且不包含右侧边界
Tab:自动补齐
Esc:取消本行代码
!:调用系统命令，！shell命令
?：查看对象属性信息
??:查看源代码
output=!cmd args :执行cmd并赋值
ipython -pylab启动可集成绘图窗口

魔术操作符
%run script.py:执行script.py
%time statement:测试statement的执行时间
%hist :显示历史命令，很多可选参数，可用于制作命令说明
%hist -f filename.py:保存ipython历史记录
%quickref:显示Ipython快速参考
%magic:显示所有命令的详细文档
%debug:从最新的异常跟踪的底部进入交互式调试器
%pdb:在异常发生后自动进入调试器
%reset:删除interactive命名空间中的全部变量
%prun statement:通过cProfile执行对statement的逐行性能分析
%timeit statement:多次测试statement的执行时间并计算平均值
%dhist:显示历史目录，用cd -n可以直接跳转
%who、%who_ls、%whos 显示interactive命名空间中定义的变量，信息级别/冗余度可变
%xdel variable:删除variable，并尝试清除其在Ipython中的对象上的一切引用
%bookmark:使用Ipython的目录书签系统
%cd directory:切换工作目录
%pwd:返回当前工作目录（字符串形式）
%env:返回当前系统变量（以字典形式）
'''
#绘图演示
import seaborn as sns
tips=sns.load_dataset('tips')
sns.catplot(x='day', y=('total_bill'),data=tips)
#取消抖动
sns.catplot(x='day', y=('total_bill'),jitter=False,data=tips)
'''
基本语法
'''
a=1
b=2
c=a+b
x=[1,2,3,4,5,6,7]
'''
变量：1.一般使用小写字母表示
     2.变量不能是数字开头 
     3.变量很长的字符中间可以加下划线 total_of_array
     4.定义变量时不要用一些关键字 例，sum如果定义成一个变量容易引起歧义，因为其本身还是一个求和函数
     5.变量赋值使用=即可，而R语言一般推荐<-进行变量赋值
     6.变量中不要有点号
'''
#python循环：不使用大括号，而使用冒号和缩进
for i in [1,2,3,4,5,6]:
    i=i+1
    print(i)
    
#加载模块的3种方法
import os
import pandas as pd #给pandas模块重新定义一个名字为pd，拼写方便
from pandas import read_csv #从pandas模块中只导入读取csv文件的函数

#特殊符号

'''
+ - * \
# #后的内容不会运行，只对语句进行注释，写一些语句的描述信息
''' 
#注释信息太多可以前加用3个单引号或双引号，就可以换行注释了
a='''He
llo'''
a
'''
\t   制表符
\n  换行符，相当于回车
() 主要用来表示函数
[] 表示一个数组或列表或用于数据索引
{} 用来表示哈希这种数据结构
'''

#基本语法演示
import numpy as np
x=np.random.randint(1,100,size=100000)
len(x)
sum(x)

'''
面向对象编程：是把构成问题事务分解成几个对象，建立对象的目的不是
为了完成一个步骤，而是为了描述某个事物在整个解决问题的步骤中的行为

面向过程编程：是分析出解决问题的所有步骤，然后用函数把这些步骤一个一个的实现，
使用的时候一个一个的依次调用就可以了

面向对象编程：
类：人类
数据中的类有集合、数组、列表、字典、ndarray类、
Series类、DataFrame类……
实例化：篮球运动员
对象：乔丹
方法：投篮，背身单打，三分，突破……
属性：身高，体重，臂展，弹跳……

通过点号访问类的属性和方法，变量名称
以及数据集的行列名都不要有点号
1.定义一个类 class obj()
class human: #定义一个human类 
    def __init__(self,name,height,weight):#定义对象的属性
        self.name=name
        self.height=height
        self.weight=weight
    def shot(self):#定义对象的方法
        print(self.name,'slam dunk')
2.实例化一个对象 Jordan=human()
Jordan=human('Jordan', 188, 90)
3.访问对象的属性
height=Jordan.height
weight=Jordan.weight
4.访问对象的方法
shot=Jordan.shot()

'''
x=[1,2,3,4,5]
type(x)#查看数据类型
dir(x)#查看有哪些属性和方法

import numpy as np
x=np.random.randint(1,100,size=100)
type(x)
x.dtype
dir(x)

#方法
x.sum()
x.mean()
x.sort()
import pandas as pd
ps=pd.Series([1,2,3,4],index=list('abcd'))
df=pd.DataFrame(np.random.randn(12).reshape(4,3),index=['A','B','C','D'],columns=['one','two','three'])

'''
NumPy
'''
#向量化运算，不需要循环，增加运行效率
#两个字符串用加号是连接的作用
s1='Hello'
s2='World'
print(s1+s2)
#比较多维数组与python自带数组的运行效率
my_arr=np.arange(1000000)
my_list=list(range(1000000))
%time for _ in range(10): my_arr*2
%time for _ in range(10): [x*2 for x in my_list] 

import numpy as np
dir(np)

#如何使用NumPy
#直接将python数组或元组转换成ndarray
x=[1,2,3,4,5]
#type函数查看数据类型
type(x)
y=np.array(x)
type(y)
x=(1,2,3,4,5) #元组tuple,元组里的值无法更改
type(x)
#将python元组转化为ndarray
y=np.array(x)
type(y)
#比较传统列表数组与ndarray的区别
#向量化运算
a=[1,2,3,4,5]
b=np.array([1,2,3,4,5])
a+1
b+1
a*10
b*10

#NumPy有很多常用函数，其中使用比较多的功能是利用其生产数字
#比如随机数，正态分布，等差数列等
使用array创建数组
arr=np.array([1,2,3])
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
#使用arange创建数组，注意起始和终止位置，
arr=np.arange(0,10,1)
arr=np.arange(0,11,1)
arr=np.arange(1,11,2)
#创建1到12的3行4列的二维数组
arr=np.arange(12).reshape(3,4)
#random生成随机数
#生成随机数种子,可以使每次生成的随机数一样
np.random.seed(1234)
np.random.randint(0,10,size=10)
np.random.seed(1234)
np.random.randint(0,10,size=10)
np.random.seed(1234)
np.random.randint(0,10,size=9)
#生成正态分布样本
np.random.randn(1000)
#随机生成整数数据集
np.random.randint(size=1000,low=1,height=100)
np.random.randint(1,100,size=1000)


#数学计算函数
#使用array创建数组
#x是一个包含1000个随机正整数的集合，取值范围1~1000
x=np.random.randint(size=1000,low=1,height=100)
#输出x
x
#进行集合的求和、平均值、方差、标准差等的计算
np.sum(x)
np.mean(x)
np.var(x)
np.std(x)
np.min(x)
np.max(x)
np.argmin(x)
np.argmax(x)
np.cumsum(x)
np.prod(x)
#x的属性里有这些运算方法的也可以直接用x的方法
x.mean()
x.sum()
x.min()

#计算机性能测试分别生成100万、1000万、1亿个随机数进行求和
import numpy as np
x=np.random.randint(1,100,size=1000000)
np.sum(x)

'''
数组索引
'''
#生成1个3行2列的数组
x=np.arange(6).reshape(3,2)
x
#取第1列，注意python是从0开始的
x[:,0]
#取第2行
x[1,:]
#取出第1列第二行的值
x[0,1]
#选取多行，例取第1行和第3行
x[[0,2],:]
#改变维度
x.reshape(2,3)
#排序
x.sort()

'''
数组组合
'''
#创建1个3行2列的数组
a=np.arange(6).reshape(3,2)
#创建一个3行3列的数组
b=np.arange(9).reshape(3,3)
#创建1个2行3列的数组
c=np.arange(6).reshape(2,3)
#数组水平组合，水平组合需要行数一致
np.hstack((a,b))#别忘了中间的括号
np.concatenate((a,b),axis=1)#1是横轴 ，0是纵轴
np.append(a,b,axis=1)
#垂直组合与水平组合类似，只是要求列数一致
np.vstack((b,c))
np.concatenate((b,c),axis=0)
np.append(b,c,axis=0)

'''
生成扑克牌
'''
#生成A，2-10，J,Q,K
x=np.append('A',np.arange(2,11))
x=np.append(x,['J','Q','K'])
#扩大4倍
x=np.tile(x,4)
#生成4种52张花色
y=np.repeat(['spades','heart','diamond','cube'], 13)
#合并两个数组
poker=np.char.add(y,x)
#添加Joker
poker=np.append(poker,['black Joker','red Joker'])

'''
pandas提供3种数据类型，分别是Series,DataFrame和Panel。
分别对应一维数据，二维数据和多维数据。主要使用的还是Series和DataFrame
Series对应R种的向量，DataFrame对应R中的data.frame
'''
'''
pandas Series
'''
#加载pandas
import pandas as pd

#python普通列表
x=[1,2,3,4,5]
type(x)
#NumPy多维数组
y=np.array(x)
type(y)
#pandas Series类
z=pd.Series(x)#自带索引
type(z)
dir(z)
len(dir(z))
z.values#查看z的数值部分
z.index#查看z的索引部分

#生成Series,数据自带数值部分和索引部分
x=pd.Series([1,2,3,4,5,6],index=['a','b','c','d','e','f'])

#ndarray转换为Series
x=np.random,randn(5)
x=pd,Series(x)

#将python字典转换为Series
dict={'Beijing':2000,'Guangdong':12000,
      'Jiangsu':9000,'Shandong':8500}
x=pd.Series(dict)

'''
pandas DataFrame
'''
s=pd.Series([1,3,2,4],index=list('abcd'))
x=pd.Series(np.random.randn(12).reshape(4,3),index=['A','B','C','D'],columns=['one','two','three','four'])
a=x['one']#取出第1列
type(a)
A=x.iloc[0,]#取出第1行
A
type(A)

ID=[1,2,3,4]
name=['Tom','Katty','John','Brown']
sex=['man','woman','man','man']
df=pd.DataFrame({'ID':ID,'Name':name,'Sex':sex})#从字典转化为DataFrame

#随机生成DataFrame
df=pd.DataFrame(np.random.rand(10,4),columns=['a','b','c','d'])
#python字典可以直接转换为DataFrame
data={
'state':['Ohio','Ohio','Ohio','Nevada','Nevada','Nevada'],
'year':[2000,2001,2002,2001,2002,2003,],
'pop':[1.5,1.7,3.6,2.4,2.9,3.2]}
df=pd.DataFrame(data)
type(df)
dir(df)
df.head()
df.dtypes
df.info()
df.shape
df.index
df.columns
df.describe()
df.values

'''
设置工作目录
'''
#windows系统目录结构："C:/Users/xxx/Desktop"
#Linux系统目录结构："/home/xxx/"
#Mac系统目录结构"/Users/xxx/Desktop/"
import os
os.getcwd()
os.chdir('Desktop/python/datasets')#换成自己的工作目录
os.listdir()

'''
读写文件
'''

#读取文件
import pandas as pd 
mtcars=pd.read_csv('mtcars.csv',sep=',',header=0,index_col=0)
'''
常用选项参数：path：文件路径，注意一定要加引号
sep:分割符，csv文件为逗号，tsv文件为制表符\t
header:表格是否包含表头信息，默认为包含
names:哪一行作为列名，可以是行号，通常是第1行，也可以是赋值具体列名
index_col:哪一列作为行名，给定具体数字，也可以指定行名，在读取矩阵时比较重要，通常将第1列作为行名
na_values:缺失值用哪种符号表示
nrow:只取出n行数据
skiprows:跳过多少行，通常文件头部有注释行，可以配合nrow,读取文件中间部分
encoding:文件编码格式
'''
mtcars.head()
mtcars.shape
mtcars.index
mtcars.columns
mtcars.dtypes
mtcars.info()
dir(mtcars)
type(mtcars)
str(mtcars)
#写入文件
mtcars.to_csv('new_mtcars.csv')
mtcars.to_csv('new_mtcars.tsv',sep='\t')

'''
读写excel文件
'''
pd.read_excel('vlookup.xlsx',sheet_name=0)
df=pd.read_excel('vlookup.xlsx',sheet_name=0,index_col=0)
df.head()
#写入文件
df.to_csv('test.csv',header=T,index=T)
'''
选项参数：sheet_name  excel文件中的表名，sheet_name=0代表读取excel中的第1个表
index_col 使用哪一列进行行索引，默认从0开始
usecols  读取表格中的哪几列，必须是位置索引
header 哪一行设置为列索引，默认是第1行，即header=0
date_parser 解析日期的函数
parse_dates 尝试将数据解析为日期，默认为False,如果为True,则尝试解析所有列，
此外，还可以指定需要解析的一组列号或列名
names 列索引
engine 默认是C，如果文件路径中存在中文，engine='python'
encoding  默认是utf-8,还可以是gbk
skiprows:跳过前几行读取文件，默认从0开始
nrows 读取多少行数据
converters 列名跟函数之间的映射关系组成的字典
'''

'''
pandas索引
'''
#Series索引
x=pd.Series([1,2,3,4,5,6],index=['a','b','c','d','e','f'])
x.values[3]
x.values[[0,1]]
x.values[np.arange(4)]
x[['a','b']]
#pandas的DataFrame索引
#选取数据
mtcars=pd.read_csv('mtcars.csv',sep=',',header=0,index_col=0)
mtcars.head()
mtcars.shape
mtcars.index
mtcars.columns
#用点号.选取列
mtcars.cyl
mtcars.cyl.size

#中括号里可以直接写列名，写数字的话代表行
mtcars['mpg']
mtcars[['mpg']]
mtcars[['mpg','cyl']]
mtcars[0:5]

#标签索引 loc:location位置索引使用行名列名
mtcars.loc[:,'cyl']#全部选取用冒号：表示
mtcars.loc[['Fiat 128','Valiant']]
#数字索引 iloc:i=integer 数字索引，输入行号或列号
mtcars.iloc[0:5,:]
mtcars.iloc[1]
mtcars.loc[:,['disp','hp']]

#奇数行
mtcars.iloc[np.arange(0,32,2),:]
#偶数行
mtcars.iloc[np.arange(1,32,2),:]

#删除行列
mtcars.drop(index=["Valiant"])
mtcars.drop(columns=['mpg','cyl'])
mtcars[mtcars.index!=5]
mtcars[mtcars.index!='Volvo 142E']

df = pd.DataFrame(np.arange(12).reshape(3,4), columns=['A', 'B', 'C', 'D'])
x=[1,2]
df.drop(df.columns[x], axis=1, inplace=True)
#df.columns[x]取出行名

#负数索引,与R不同，R中负数索引是删除，python里是-1行是倒数第1行
mtcars.iloc[-1,:]
mtcars.iloc[:,-1]

'''
逻辑值索引
'''
#逻辑值索引,逻辑值的个数必须与行列数相匹配,
#既可以使用位置索引loc也可以使用数字所以iloc
x=mtcars.iloc[0:3,0:3]
x.loc[:,[True,False,False]]
x.loc[[True,False,True],:]
x.iloc[[True,False,False],:]
x.loc[[True,False,True],[False,True,False]]

#筛选奇数项
logic=np.repeat(['True','False'], repeats=16)
#repeat是分别重复16次
logic
mtcars[logic]
logic=np.tile(['True','False'],reps=16)
#tile是整体重复16次
logic
mtcars.loc[logic,:]

'''
筛选数据
'''
mtcars[mtcars.loc[:,'mpg']>=25]#或者mtcars.loc[mtcars.mpg>=25,:]
mtcars.loc[mtcars.cyl==4,:]
mtcars.query('cyl==4')
mtcars.loc[(mtcars.mpg>=25)&(mtcars.cyl==4),:]
#mtcars[(mtcars.mpg>=25)&(mtcars.cyl==4)]
mtcars.loc[(mtcars.mpg>=25)|(mtcars.cyl==4),:]
#mtcars[(mtcars.mpg>=25)|(mtcars.cyl==4)]
# &与 |或 ！非
#根据字符串匹配进行筛选
iris=pd.read_csv('C:/Users/bdgcx/seaborn-data/iris.csv')
#import seaborn as sns
#iris=sns.load_dataset('iris')
iris.head()
iris.query('species=="setosa"') 
#iris.loc[iris.species=='setosa',:]

np.repeat([1,2,3,4,5], repeats=[1,2,3,4,5])
np.tile(A=[1,2,3,4,5],reps=2)
#生成DataFrame

'''
利用python实现vlookup, vlookup即按列筛选数据
'''
gene121=pd.read_csv('121genes.csv',squeeze=True)
#squeeze参数是文件只有一列时，默认这一列读入为Series而不是DataFrame
gene121
#去除重复项
gene121.duplicated()
gene121[gene121.duplicated()]

gene121.unique()
gene121.nunique()
geneid=gene121.unique()
gene200=pd.read_csv('gene200.csv',index_col=0)
#gene200=pd.read_csv('gene200.csv',index_col=0)
#gene200.reset_index(drop='gene')
gene200.head()
gene200.index
#重新索引reindex, 实现vlookup功能
gene93=gene200.reindex(index=geneid)
#去掉缺失值
gene86=gene93.dropna()
#保存最后结果
gene86.to_csv('gene86.csv')

'''
修改数据
'''
mtcars.iloc[0,0]=12
mtcars.iloc[:,1]=10#相当于mtcars.cyl=10
mtcars.cyl.replace(4,'four')
mtcars.cyl.replace([4,6,8],['four','six','eight'])
#replace不是对原数据进行修改
#修改行名
mtcars.rename(index={'Fiat 128':'fiat128'})
mtcars.rename(index={'Fiat 128':'fiat128'},inplace=True)
#inplace=True可以在原数据集上进行改动
#修改列名
#mtcars.reset_index()
mtcars.rename(columns={'cyl':'cylinder','mpg':'meters per gallon'})
mtcars.rename(columns={'cyl':'cylinder','mpg':'meters per gallon'},inplace=True)
mtcars.rename({'cyl':'cylinder'},axis=1)
mtcars.rename({'Fiat 128':'fiat128'},axis=0)
#修改数据
np.where(mtcars.mpg>20,'T','F')
[np.log(x) for x in mtcars['cyl']]
mtcars.cyl[0]
mtcars['logic']=np.where(mtcars.mpg>25,'T','F')
[np.log(x) for x in mtcars['cyl']]

'''
排序
'''
#按行名排序
mtcars.sort_index()
#按列名排序 
mtcars.sort_index(axis=1)
mtcars.sort_index(ascending=False)
#值排序
mtcars.sort_values(by='cyl')
mtcars.sort_values(by='cyl',ascending=False)
mtcars.sort_values(by=['mpg','cyl'],ascending=False)
#by是多个值的时候有先后顺序
mtcars.sort_values(by=['mpg','cyl'],ascending=[False,True])
mtcars[mtcars.cyl.isin([4,6])]

'''
随机抽样
'''
np.random.seed(1234)
mtcars.sample(n=25) #按个数,默认为无放回的随机抽样
mtcars.sample(n=25,replace=True)#replace=True,有放回的随机抽样
mtcars.sample(frac=0.2) #数据比较大时，按百分比
#a按列抽样
mtcars.sample(frac=0.1,axis=1)#抽出10%的行
mtcars.sample(frac=0.2,axis=1)#抽出20%的行

'''
斗地主
'''
#生成扑克牌
#生成A，2-10，J,Q,K
x=np.append('A',np.arange(2,11))
x=np.append(x,['J','Q','K'])
#扩大4倍
x=np.tile(x,4)
#生成4种52张花色
y=np.repeat(['spades','heart','diamond','cube'], 13)
#合并两个数组
poker=np.char.add(y,x)
#添加Joker
poker=np.append(poker,['black Joker','red Joker'])
poker=pd.Series(poker)
#洗牌
shutter=poker.sample(54)
shutter.values
shutter.values[np.arange(0,51,3)]
first=shutter.values[np.arange(0,51,3)]
second=shutter.values[np.arange(1,51,3)]
third=shutter.values[np.arange(2,51,3)]
dipai=shutter.values[[51,52,53]]

'''
获取帮助
1.help函数   help(np.arange)  或    np.arange?
2.官方文档
3.搜索引擎
'''

'''
计算基因长度分布
'''
gff=pd.read_csv('H37Rv.gff',sep='\t',skiprows=9,header=None)
gff.size
gff.columns
gff.index
#筛选第3列为gene的行
gene=gff[gff[2]=='gene']
#gene=gff[gff.iloc[:,2]=='gene']
gene.size
#计算基因长度
gene_lengh=np.abs(gene.iloc[:,4]-gene.iloc[:,3])+1
gene_lengh.describe()
gene_lengh.describe().round(2)#round保留几位小数
#绘制基因长度分布图
gene_lengh.hist()
gene_lengh.hist(bins=80)

%who #查看环境里有哪些变量
del(gene) #删除环境中某个变量

'''
修改行列
'''
#删除行列
mtcars.drop(index="Volve 142E")
mtcars.drop(columns=['mpg'])
mtcars.drop(columns=['mpg','cyl'])
mtcars.drop(index='Volve 142E',columns='cyl')

#增加行列
logic=np.where(mtcars.mpg>20,'T','F')
mtcars['logic']=''#新增1列，但没有赋值
mtcars.logic=logic #赋值个数与原DataFrame要匹配
#mtcars['logic']=np.where(mtcars.mpg>25,'T','F')

#取log值然后赋值给原数据集
np.log(mtcars.cyl)
mtcars['cyl_log']=np.log(mtcars.cyl)
mtcars['cyl_log']=np.round(np.log(mtcars.cyl),2)
#[np.log(x) for x in mtcars['cyl']]
#log_cyl=[np.log(x) for x in mtcars['cyl']]
np.round(log_cyl,2)

#按行和列求和
gene=pd.read_csv('heatmap.csv',index_col=0)
gene.head()
gene.index
gene.columns
total1=gene.apply(func=sum, axis=0)
gene.loc['Total',:]=total1
total2=gene.apply(func=sum, axis=1)
gene.loc[:,'Total']=total2
gene

'''
处理缺失值
'''
#R内置数据集sleep
sleep=pd.read_csv('sleep.csv',index_col=0,na_values=['NA'])
sleep.head()
#判断缺失值
sleep.isna()
sleep.isnull()
#删除缺失值
sleep.dropna(axis=0)
sleep.dropna(axis=1)
sleep.dropna(axis=0,how='all')
#填充缺失值
sleep.fillna(axis=0,method='ffill')#ffill即向前填充forward?
sleep.fillna(axis=1,method='bfill')#bfill即向后填充backward?
sleep.fillna(value=sleep.mean())

'''
分组计算
'''
#R内置数据集ToothGrowth
x=pd.read_csv('ToothGrowth.csv',index_col=0)
x
x.columns
x.supp
#计算频数
x.supp.value_counts()
x.dose.value_counts()

#将dose列的类型转换为字符串类
x['dose']=x['dose'].astype('str')

#二维列联表
pd.crosstab(x.dose, x.supp)
pd.crosstab(x.supp, x.dose)

#分组统计
x.groupby(by=x.supp).sum()
x.groupby(by=x.supp).mean()
x.groupby(x='supp')['len'].mean()

x.groupby(by=['supp','dose']).min()
x.groupby(by=['supp','dose']).max()
x.groupby(by=['supp','dose']).mean()

'''
数据透视表
'''
x=pd.read_excel('2015年度中国城市GDP排名.xlsx',index_col=0)
x.head()
x.columns
#计算频数
x.Province.value_counts()
#添加平均收入项
x['Average']=x.Income/x.People
x.Average=round(x.Average,ndigits=2)

#探索数据
x.sort_index(ascending=False)
x.sort_index(ascending=False,axis=1)
x.sort_values('Income')
x.sort_values('Income',ascending=False)

#分组统计(数据透视pivot_table)
x.pivot_table(index='Province',aggfunc=sum)
#统计频数aggfun=size
x.pivot_table(values='Income',index='Province',aggfunc=size) 
#进行排序
x.pivot_table(values='Income',columns='Province',aggfunc=size).sort_values('Income')

x.pivot_table(index='Province',aggfunc=max)
x.pivot_table(index='Province',values='City',aggfunc=max)
x.pivot_table(index='Province',values=['City','Income'],aggfunc=max)
x.pivot_table(index=['Province','City'],values='Income',aggfun=max)

'''
计算相关性
'''
#使用R内置数据集state.x77.csv
x=pd.read_csv('state.x77.csv',sep=',',header=0,index_col=0)
x
x.shape
x.index
x.columns
x.corr() #计算pearson相关系数
x.corr('kendall') #计算Kendall Tau相关系数
x.corr('spearman') #计算spearman秩相关
x['Murder'].corr(x['Income'])
x.corrwith(x['Murder']) #将Murder和其它观测值的相关系数计算出来
x['Murder'].cov(x['Income'])


















