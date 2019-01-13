import numpy as np

class DistanceCalculator:
    def __init__(self, data, dist_meas = 'euclidean'):
        """
        data : a numpy array with the entries as rows and attributes as columns.
        """
        self.data = data
        self.nr_entries = data.shape[0] # nr vertices
        self.dist_meas = dist_meas

    def get_dist(self, i, j):
        entry_i = self.data[i]
        entry_j = self.data[j]

        if self.dist_meas == 'euclidean':
            dist = np.linalg.norm(entry_i - entry_j)
        # possible to add more distance measures here
        return dist

    def get_dist_list(self):
        dl = []
        for i in range(self.nr_entries):
            for j in range(i+1, self.nr_entries):
                dist = self.get_dist(i, j)
                dl.append((dist, i, j))
        return dl, self.nr_entries
