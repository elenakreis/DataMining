from DistanceCalculator import DistanceCalculator
from MSTMaker import MSTMaker
from DHClustering import DHClustering
from Printer import Printer
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

data, classes, names = prepare_data("zoo.csv")
dc = DistanceCalculator(data)
dl, nr_entries = dc.get_dist_list()
mst_maker = MSTMaker(dl, nr_entries)
mst = mst_maker.get_mst()
dh_clusterer = DHClustering(mst)
clusters = dh_clusterer.make_clusters()
p = Printer()
print(p.fill_in_names(clusters, names))


