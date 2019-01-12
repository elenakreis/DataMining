from DistanceCalculator import DistanceCalculator
from MSTMaker import MSTMaker
from DHClustering import DHClustering

import numpy as np
import pandas as pd

def prepare_data(filename):
    '''
    Assumes data is in csv format
    '''
    df = pd.read_csv(filename).values
    classes = df[:,-1]
    names = df[:,0]
    data = df[:,1:len(df[0])-1]
    return data, classes, names

#data, classes, names = prepare_data("zoo.csv")
#data = np.array([[3,4],[2,5],[6,7],[0,3],[-1,7],[2,6]])
data = np.array([[0,0],[1,1],[9,9],[10,11]])
dc = DistanceCalculator(data)
dl, nr_entries = dc.get_dist_list()

mst_maker = MSTMaker(dl, nr_entries)
mst = mst_maker.get_mst()
print(mst)
dh_clusterer = DHClustering(mst)
clusters = dh_clusterer.make_clusters()
print(clusters, nr_entries)
