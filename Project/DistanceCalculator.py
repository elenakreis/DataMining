import numpy as np

class DistanceCalculator:
    def __init__(self, data, dist_meas = 'euclidean'):
        # data should be a numpy array
        self.data = data
        self.nr_entries = data.shape[0]
        self.dist_meas = dist_meas

    def get_dist(self, i, j):
        entry_i = self.data[i]
        entry_j = self.data[j]

        if self.dist_meas == 'euclidean':
            dist = np.linalg.norm(entry_i - entry_j)
        # add more distance measures here; catch error
        return dist

    def get_dist_list(self):
        dl = []
        for i in range(self.nr_entries):
            for j in range(i+1, self.nr_entries):
                dist = self.get_dist(i, j)
                dl.append((dist, i, j))
        return (dl, self.nr_entries)
