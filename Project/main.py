from DistanceCalculator import DistanceCalculator
from MSTMaker import MSTMaker

import numpy as np
import pandas as pd
# Get and prepare the data
# data = ...
# Generate proximity matrix from data
#p_maker = DistanceCalculator()
#pm = p_maker.get_prox_mat()
# Create MST from pm
#mst_maker = MSTMaker()
#mst = mst_maker.get_mst()
# repeat:
#   Create new cluster by breaking the link corresponding to the largest distance
# until: Only singleton clusters remain
def prepare_data(filename):
    '''
    Assumes data is in csv format
    '''
    df = pd.read_csv(filename).values
    classes = df[:,-1]
    names = df[:,0]
    data = df[:,1:len(df[0])-1]
    return data, classes, names

data, classes, names = prepare_data("zoo.csv")
dc = DistanceCalculator(data)
dl, nr_entries = dc.get_dist_list()

mst_maker = MSTMaker(dl, nr_entries)
mst = mst_maker.get_mst()
print(mst)
