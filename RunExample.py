import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.neighbors import NearestNeighbors
from LoadData import *
from DataHelper import *
from sklearn.model_selection import train_test_split
from ProbabilisticMatrixFactorization import PMF

if __name__ == "__main__":
    file_path = "Data/TestDouban.csv"
    user_simility = LoadData4Matrix('Data/user_similarity.dat')
    item_simility = LoadData4Matrix('Data/item_similarity.dat')
    Userneighbor_indices = LoadData4Matrix('Data/UserneighborMatrix.dat')
    Itemneighbor_indices = LoadData4Matrix('Data/ItemneighborMatrix.dat')
    pmf = PMF()
    pmf.user_simility_matrix = user_simility
    pmf.user_neighbor_matrix = Userneighbor_indices
    pmf.item_simility_matrix = item_simility
    pmf.item_neighbor_matrix = Itemneighbor_indices
    pmf.set_params({"num_feat": 10, "epsilon": 1, "_lambda": 0.1, "momentum": 0.8, "maxepoch": 10, "num_batches": 100,
                    "batch_size": 1000})
    ratings = load_Douban_data(file_path)
    print(len(np.unique(ratings[:, 0])), len(np.unique(ratings[:, 1])), pmf.num_feat)
    train, test = train_test_split(ratings, test_size=0.1)  # spilt_rating_dat(ratings)
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
