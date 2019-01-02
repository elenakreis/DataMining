from DistanceCalculator import DistanceCalculator
from MSTMaker import MSTMaker

import numpy as np
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
def prepare_data(data):
    '''
    Assumes data is in csv format
    '''


array = np.array([[3,4],[0,0],[1,2]])
#list = [(3,5),(0,6),(2,4)]

dc = DistanceCalculator(array)
dl, nr_entries = dc.get_dist_list()

mst_maker = MSTMaker(dl, nr_entries)
mst = mst_maker.get_mst()
print(mst)
