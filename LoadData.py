from numpy import *
import pandas as pd
import random


def load_rating_data(file_path='ml-100k/u.data'):
    """
    load movie lens 100k ratings from original rating file.
    need to download and put rating data in /data folder first.
    Source: http://www.grouplens.org/
    """
    prefer = []
    for line in open(file_path, 'r'):  # 打开指定文件
        (userid, movieid, rating, ts) = line.split('\t')  # 数据集中每行有4项
        uid = int(userid)
        mid = int(movieid)
        rat = float(rating)
        prefer.append([uid, mid, rat])
    data = array(prefer)
    return data


def load_Douban_data(file_path='Data/Douban.csv'):
    header = ['user_id', 'item_id', 'rating', 'timestamp', 'tags']
    dataframe = pd.read_csv(file_path, header=None, delimiter='|', encoding='UTF-8', names=header)
    prefer = []
    z = 0
    for line in dataframe.itertuples():
        UserID = int(line[1])
        MovieID = int(line[2])
        Rating = int(line[3])
        prefer.append([UserID, MovieID, Rating])
        z+=1
        print(z)
    data = array(prefer)
    return data


def spilt_rating_dat(data, size=0.2):
    train_data = []
    test_data = []
    for line in data:
        rand = random.random()
        if rand < size:
            test_data.append(line)
        else:
            train_data.append(line)
    train_data = array(train_data)
    test_data = array(test_data)
    return train_data, test_data
