# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import csv
from DataHelper import *




if __name__ == '__main__':
    header = ['after_id', 'before_id']
    userdataframe = pd.read_csv('Data/users.txt', header=None, delimiter='|', encoding='UTF-8', names=header)
    userdata = (userdataframe.as_matrix())[:, 1]
    # userdata=np.zeros((1,len(userdataframe)))
    moviedataframe = pd.read_csv('Data/movies.txt', header=None, delimiter='|', encoding='UTF-8', names=header)
    moviedata = (moviedataframe.as_matrix())[:, 1]
    tagdata=LoadData4pkl('Data/tags.pkl')
    with open('Data/FinalTestDouban.csv', 'w', newline='', encoding='UTF-8') as csv_file:
        writer = csv.writer(csv_file, delimiter='|')
        z = 1
        _header = ['user_id', 'item_id', 'rating', 'timestamp', 'tags']
        dataframe = pd.read_csv('Data/TestDouban.csv', header=None, delimiter='|', encoding='UTF-8', names=_header)
        for line in dataframe.itertuples():
            userindex = (np.where(userdata == int(line[1])))[0][0] + 1
            movieindex = np.where(moviedata == int(line[2]))[0][0] + 1
            tags = line[5]
            tagList = tags.split(',')
            _tags = str()
            for e in tagList:
                if e in tagdata:
                    _tags = _tags + str(tagdata[e]) + ','
                else:
                    print(e)
            _tags = _tags.rstrip(',')
            after_line = str(userindex) + '|' + str(movieindex) + '|' + str(line[3]) + '|' + line[4] + '|' + _tags
            try:
                writer.writerow([userindex, movieindex, line[3], line[4], _tags])
            except Exception as e:
                print(e)
            z += 1
            print(z)
