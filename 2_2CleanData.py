# -*- coding: utf-8 -*-
# remove those tags which are annotated by less than five distinct users and five distinct items
import pandas as pd
import numpy as np
import csv

file_path = 'Data/TestDouban.csv'
UserSet = set()  # UserID采样集合
ItemSet = set()  # ItemID采样集合
UserTags = {}  # 用户标签
ItemTags = {}  # 电影标签


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

                if UserID not in UserSet:
                    UserSet.add(UserID)  # 将未记录的UserID添加进UserIDSet集合
                if MovieID not in ItemSet:
                    ItemSet.add(MovieID)  # 将未记录的MovieID添加进ItemSet集合

                if MovieID in ItemTags:
                    ItemTags[MovieID].add(tag)
                else:
                    ItemTags.setdefault(MovieID, set())
                    ItemTags[MovieID].add(tag)
                if UserID in UserTags:
                    UserTags[UserID].add(tag)
                else:
                    UserTags.setdefault(UserID, set())
                    UserTags[UserID].add(tag)

    for user, _tags in UserTags.items():
        if user == 1001901:
            print(user)
        if len(_tags) < 5:
            UserSet.remove(user)
    for item, _tags in ItemTags.items():
        if len(_tags) < 5:
            ItemSet.remove(item)

    with open('Data/TestDouban.csv', 'w', newline='', encoding='UTF-8') as csv_file:
        writer = csv.writer(csv_file, delimiter='|')
        num = 0
        for line in dataframe.itertuples():
            UserID = int(line[1])
            MovieID = int(line[2])
            Rating = int(line[3])
            TimeStamp = line[4]
            tags = line[5]

            if len(tags) == 0:
                continue
            if UserID in UserSet:
                if MovieID in ItemSet:
                    try:
                        writer.writerow([UserID, MovieID, Rating, TimeStamp, tags])
                        num += 1
                        print(num)
                    except Exception as e:
                        print(e)
                else:
                    print('MovieID' + str(MovieID))
            else:
                print('UserID' + str(MovieID))
