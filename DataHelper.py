# -*- coding: utf-8 -*-
import pickle, numpy


def SaveData2pkl(DictData, FileFath='Datas/Mydata.pkl', mode='wb'):
    pkl_file = open(FileFath, mode)
    try:
        pickle.dump(DictData, pkl_file, protocol=2)
        return True
    except:
        return False
    finally:
        pkl_file.close()


def LoadData4pkl(FileFath='Datas/Mydata.pkl', mode='rb'):
    pkl_file = open(FileFath, mode)
    try:
        DataDict = dict(pickle.load(pkl_file))
        return DataDict
    except:
        return None
    finally:
        pkl_file.close()


def LoadData4Matrix(FileFath='Data/user_tag_matrix.dat', mode='rb'):
    pkl_file = open(FileFath, mode)
    try:
        DataDict = (pickle.load(pkl_file))
        return DataDict
    except:
        return None
    finally:
        pkl_file.close()


def Savetxt(FilePath, message='', mode='a'):
    file_object = open(FilePath, mode, encoding='UTF-8')
    file_object.write(message)
    file_object.close()