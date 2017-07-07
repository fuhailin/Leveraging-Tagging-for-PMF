# -*- coding: utf-8 -*-
# Remove those tags which are annotated by less than five distinct users and five distinct items
# @author: Kris
import math

import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.neighbors import NearestNeighbors


def TF(dataDict):
    tagTF = {}
    for each, taglist in dataDict.items():
        # user = line[1]
        # taglist = list(map(int, line[2].split(',')))
        if each not in tagTF:
            tagTF.setdefault(each, {})
            for tag in taglist:
                if tag in tagTF[each]:
                    tagTF[each][tag] += 1
                else:
                    tagTF[each][tag] = 1
    return tagTF


def IDF(dataDict):
    tagIDF = {}
    for each, taglist in dataDict.items():
        # testtags = list(map(int, line[2].split(',')))
        tagset = set(taglist)
        for e in tagset:
            if e in tagIDF:
                tagIDF[e] += 1
            else:
                tagIDF[e] = 1
    return tagIDF


def TFIDF():
    header = ['after_id', 'before_id']
    tagdataframe = pd.read_csv('Data/tags.txt', header=None, delimiter='|', encoding='UTF-8', names=header)
    num_tag = tagdataframe.shape[0]

    User_Tags = {}
    Item_Tags = {}
    _header = ['user_id', 'item_id', 'rating', 'timestamp', 'tags']
    dataframe = pd.read_csv('Data/FinalTestDouban.csv', header=None, delimiter='|', encoding='UTF-8', names=_header)
    for line in dataframe.itertuples():
        UserID = int(line[1])
        MovieID = int(line[2])
        tags = line[5]
        tagList = tags.split(',')
        _tags = str()
        for tag in tagList:
            if UserID in User_Tags:
                User_Tags[UserID].append(int(tag))
            else:
                User_Tags.setdefault(UserID, list())
                User_Tags[UserID].append(int(tag))
            if MovieID in Item_Tags:
                Item_Tags[MovieID].append(int(tag))
            else:
                Item_Tags.setdefault(MovieID, list())
                Item_Tags[MovieID].append(int(tag))

    num_user = len(User_Tags)
    num_item = len(Item_Tags)

    user_tag_tfidf = np.zeros((num_user, num_tag))
    item_tag_tfidf = np.zeros((num_item, num_tag))

    b = IDF(User_Tags)
    a = TF(User_Tags)
    for e, _tags in a.items():
        for _tag in _tags:
            tf = a[e][_tag] / (len(User_Tags[e]))
            idf = math.log((num_user / (b[_tag] + 1)), math.e)
            user_tag_tfidf[e - 1][_tag - 1] = tf * idf

    d = IDF(Item_Tags)
    c = TF(Item_Tags)
    for e, _tags in c.items():
        for _tag in _tags:
            tf = c[e][_tag] / (len(Item_Tags[e]))
            idf = math.log((num_user / (d[_tag] + 1)), math.e)
            item_tag_tfidf[e - 1][_tag - 1] = tf * idf

    # user_tag_tfidf.dump('Data/user_tag_tfidf.dat')
    # item_tag_tfidf.dump('Data/item_tag_tfidf.dat')
    knn = NearestNeighbors(metric="cosine", algorithm="brute")
    knn.fit(user_tag_tfidf)
    Userneighbor_indices = knn.kneighbors(n_neighbors=10, return_distance=False)
    # Userneighbor_indices.dump('Data/UserneighborMatrix.dat')
    user_similarity = cosine_similarity(user_tag_tfidf)
    # user_similarity.dump('Data/user_similarity.dat')
    print(Userneighbor_indices[1])

    knn = NearestNeighbors(metric="cosine", algorithm="brute")
    knn.fit(item_tag_tfidf)
    Itemneighbor_indices = knn.kneighbors(n_neighbors=10, return_distance=False)
    # Itemneighbor_indices.dump('Data/ItemneighborMatrix.dat')
    item_similarity = cosine_similarity(item_tag_tfidf)
    # item_similarity.dump('Data/item_similarity.dat'
    return user_similarity, Userneighbor_indices, item_similarity, Itemneighbor_indices
