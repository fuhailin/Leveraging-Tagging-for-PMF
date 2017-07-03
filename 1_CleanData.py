# -*- coding: utf-8 -*-
# 将原始文件中的空白行去除，所有有Tag的数据行放进Douban.CSV文件中

import csv
import pandas as pd
import numpy as np


def CleanData(file_path):
    with open('Data/M1.csv', 'w', newline='', encoding='UTF-8') as csv_file:
        writer = csv.writer(csv_file, delimiter='|')
        num = 0
        for line in open(file_path, 'r', encoding='UTF-8'):  # 打开指定文件
            line = line.rstrip('\n')
            if len(line) == 0:
                continue
            linelist = line.split(',')  # 数据集中每行有4项
            UserID = int(linelist[0])
            MovieID = int(linelist[1])
            Rating = int(linelist[2])
            TimeStamp = linelist[3]
            Tag = linelist[4:]
            _tags = str()
            for e in Tag:
                if len(e.rstrip(' ')) == 0:
                    continue
                _tags = _tags + e + ','
            _tags = _tags.rstrip(',')
            # if len(_tags) == 0:
            #     continue
            try:
                writer.writerow([UserID, MovieID, Rating, TimeStamp, _tags])
                num += 1
                print(num)
            except Exception as e:
                print(e)


if __name__ == '__main__':
    CleanData('Data/M1.txt')
    print('Finish')
