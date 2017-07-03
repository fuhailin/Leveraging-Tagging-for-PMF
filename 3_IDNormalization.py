# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from DataHelper import *

file_path='Data/TestDouban.csv'

def Normalization(dataframe, i):
    test2 = dataframe.icol(i)
    print(test2[1])
    # test2.order()
    # test2.sort()
    myid = set()
    for j in range(0, len(test2)):
        myid.add(test2[j])
    test1 = list(myid)
    test1.sort()
    norid = np.zeros((1, len(test1) + 1))
    for k in range(0, len(test1)):
        norid[0][k + 1] = test1[k]
    return norid


def Extract(filename='test.txt', matrixdata=None):
    file_object = open(filename, 'a')
    for q in range(1, len(matrixdata[0])):
        file_object.write(str(q) + '|' + str(int(matrixdata[0][q])) + '\n')
        print(q)
    file_object.close()


if __name__ == '__main__':
    header = ['user_id', 'item_id', 'rating', 'timestamp', 'tags']
    dataframe = pd.read_csv(file_path, header=None, delimiter='|', encoding='UTF-8', names=header)
    print(dataframe.user_id)

    TagSet=set()
    for line in dataframe.itertuples():
        tags = line[5]
        tagList = str(tags).lower().split(',')
        for i in range(0, len(tagList)):
            tag = tagList[i]
            if tag not in TagSet:
                TagSet.add(tag)  # 将未记录的Tag添加进Tag集合
    _taglist=sorted(TagSet)
    TagDict = {}
    index = 1
    for singletag in _taglist:
        TagDict[singletag] = index
        print(TagDict[singletag])
        index += 1
    SaveData2pkl(TagDict,'Data/tags.pkl')

    file_object = open('Data/tags.txt', 'a', encoding='UTF-8')
    for q, w in TagDict.items():
        file_object.write(str(w) + '|' + str(q) + '\n')
    file_object.close()

    data0 = Normalization(dataframe, 0)
    print(len(data0[0]))
    Extract('Data/users.txt', data0)
    print('FINISH0')

    data1 = Normalization(dataframe, 1)
    print(len(data1[0]))
    Extract('Data/movies.txt', data1)
    print('FINISH1')




