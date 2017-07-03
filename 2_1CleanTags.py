# -*- coding: utf-8 -*-
# remove those tags which are annotated by less than five distinct users and five distinct items
import pandas as pd
import numpy as np
import csv

file_path = 'Data/Douban.csv'
TagSet = set()  # 集合set()不可添加重复数据,Tag采样集合

TagUsers = {}  # 标签下标索引
TagItems = {}

if __name__ == '__main__':
    header = ['user_id', 'item_id', 'rating', 'timestamp', 'tags']
    dataframe = pd.read_csv(file_path, header=None, delimiter='|', encoding='UTF-8', names=header)
    for line in dataframe.itertuples():
        UserID = int(line[1])
        MovieID = int(line[2])
        Rating = float(line[3])
        tags = line[5]
        if tags is not np.nan:
            tagList = str(tags).lower().split(',')
            for i in range(0, len(tagList)):
                tag = tagList[i]  # .replace(' ', '')  #Tag为空格
                if len(tag) == 0:
                    print(0)
                if tag not in TagSet:
                    TagSet.add(tag)  # 将未记录的Tag添加进Tag集合
                if tag in TagUsers:
                    TagUsers[tag].add(UserID)
                else:
                    TagUsers.setdefault(tag, set())
                    TagUsers[tag].add(UserID)
                if tag in TagItems:
                    TagItems[tag].add(MovieID)
                else:
                    TagItems.setdefault(tag, set())
                    TagItems[tag].add(MovieID)


    for _tag, users in TagUsers.items():
        if len(users) < 5:
            TagSet.remove(_tag)
    for _tag, items in TagItems.items():
        if len(items) < 5:
            if _tag in TagSet:
                TagSet.remove(_tag)

    with open('Data/TestDouban.csv', 'w', newline='', encoding='UTF-8') as csv_file:
        writer = csv.writer(csv_file, delimiter='|')
        num = 0
        for line in dataframe.itertuples():
            UserID = int(line[1])
            MovieID = int(line[2])
            Rating = int(line[3])
            TimeStamp = line[4]
            tags = line[5]
            # if tags is not np.nan:
            tagList = str(tags).lower().split(',')
            _tags = str()
            for e in tagList:
                if e in TagSet:
                    _tags = _tags + e + ','
                else:
                    print(e)
            _tags = _tags.rstrip(',')
            if len(_tags) == 0:
                continue
            try:
                writer.writerow([UserID, MovieID, Rating, TimeStamp, _tags])
                num += 1
                print(num)
            except Exception as e:
                print(e)

