import matplotlib.pyplot as plt
import numpy as np
from LoadData import *
from sklearn.model_selection import train_test_split
from ProbabilisticMatrixFactorization import PMF
from Tf_idf import TFIDF

if __name__ == "__main__":
    file_path = "Data/FinalTestDouban.csv"
    user_simility, Userneighbor_indices, item_simility, Itemneighbor_indices = TFIDF()
    pmf = PMF()
    pmf.user_simility_matrix = user_simility
    pmf.user_neighbor_matrix = Userneighbor_indices
    pmf.item_simility_matrix = item_simility
    pmf.item_neighbor_matrix = Itemneighbor_indices
    pmf.set_params({"num_feat": 10, "epsilon": 1, "_lambda": 0.01, "momentum": 0.8, "maxepoch": 100, "num_batches": 10, "batch_size": 1000})
    ratings = load_Douban_data(file_path)
    # ratings = load_rating_data()
    print(len(np.unique(ratings[:, 0])), len(np.unique(ratings[:, 1])), pmf.num_feat)
    train, test = train_test_split(ratings, test_size=0.2)  # spilt_rating_dat(ratings)
    pmf.fit(train, test)

    # Check performance by plotting train and test errors
    plt.plot(range(pmf.maxepoch), pmf.rmse_train, marker='o', label='Training Data')
    plt.plot(range(pmf.maxepoch), pmf.rmse_test, marker='v', label='Test Data')
    plt.title('The MovieLens Dataset Learning Curve')
    plt.xlabel('Number of Epochs')
    plt.ylabel('RMSE')
    plt.legend()
    plt.grid()
    plt.show()
    print("precision_acc,recall_acc:" + str(pmf.topK(test)))
