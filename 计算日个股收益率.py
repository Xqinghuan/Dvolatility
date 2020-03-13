# 练习
# 清欢

import os
import pandas as pd
import re
import numpy

'''
计算年收益率的思路
1.从多个表格当中读取数据
2.将多个表格的数据拼接在一起
3.计算每个公司每年的平均值
4.计算标准差
5.保留一年的数据，写入表格
'''

def ReadFile(data):
    '''读取表格中的数据'''
    excelFile = r'{}'.format(data)
    df = pd.DataFrame(pd.read_excel(excelFile))
    # print(df)
    # print(df.dtypes)
    df2 = df.drop(index=[0,1])

    '''这下面的是想将年月日切片为年的数据，但是会出现最后两个缺失值的问题
    ？？？？？？待解决
    '''
    # print(len(df2))
    # year = df2.iloc[:,[1]]
    # print(len(year))
    # peryear_list = (rows['Trddt'][0:4] for index,rows in year.iterrows())
    # df2['year'] = pd.DataFrame(peryear_list)
    # print(df2)
    # exit()
    # for index, rows in year.iterrows():
    #     # print(index, rows['Trddt'])
    #     peryear = rows['Trddt'][0:4]
    #     print(index, peryear)
    #     # peryear_list.append(peryear)
    # # print(len(peryear_list))
    # # dfyear = pd.DataFrame(peryear_list)
    # # df2['year'] = pd.DataFrame(dfyear)


    return df2

def AddForm(data):
    '''
    将多个表格拼接为一个表格
    '''
    # df = ReadFile(data[0])
    # df1 = ReadFile(data[1])
    # df2 = pd.concat([df, df1])
    # print(df2)
    df_all = pd.DataFrame()
    for i in data:
        df = ReadFile(i)
        df_all = pd.concat([df_all, df])
        per = (data.index(i))/len(data)
        print("当前进度为{}，数据总长度为{}".format(per, len(df_all)))

    return df_all

def FileName():
    '''获取要读取的每个文件的名字
    :return:返回要读取的所有文件的列表
    '''
    pathlist = []

    path = os.path.dirname(__file__)    # 当前运行文件所在的目录
    # filename_list = []
    for i in os.listdir():
        ptn = r'^日个股.*?'            # 匹配含有特定字符开头的文件夹
        if re.match(ptn, i):
            filepath = path + '/' + i + '/'
            filename_list = [filepath+j for j in os.listdir(filepath)]
            pathlist.append(filename_list)
    pathlist = [i for i in pathlist if len(i)>0]

    # 将pathlist三个列表改成一个列表
    PathList = []
    for i in pathlist:
        for j in i:
            PathList.append(j)

    # 挑选出文件后缀名字为.xls的数据
    ptn = r'.*?xls$'
    PathList = [i for i in PathList if re.match(ptn, i)]

    return PathList


def WriteFile(data):
    with open('日交易数据.txt','a+', encoding='utf-8') as f:
        for index, rows in data.iterrows():
            line = '{}'.format(data)
            f.writelines(line)


if __name__ == '__main__':
    # 获取表格名字
    PathList = FileName()
    # 获取总的数据
    data = AddForm(PathList)
    WriteFile(data)
    # df = ReadFile('demo.xls')
    # df1 = ReadFile('demo1.xls')




