import numpy as np

class Printer:
    """
    Make a maxtrix of (n-1) by 4, where n is the number of attributes (dimentions).
    
    """        
    def print_clusters(self, clusters, nr_entries):
        ### Does not work yet
        Z = np.zeros((nr_entries, 4))
        dist, e1, e2  = clusters
        print(Z.shape)
        
    def fill_in_names(self, cluster, name_list):
        dist, e1, e2 = cluster
        if isinstance(e1, tuple):
            e1 = self.fill_in_names(e1, name_list)
        else:
            e1 = name_list[e1] ## Replace index by string
        if isinstance(e2, tuple):
            e2 = self.fill_in_names(e2, name_list)
        else:
            e2 = name_list[e2] ## Replace index by string        
        return (dist, e1, e2)

