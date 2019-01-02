class MSTMaker:
    def __init__(self, dist_list, nr_entries):
        self.dist_list = dist_list
        print(self.dist_list)
        self.nr_entries = nr_entries
        self.mst = []
        self.sets = [[i] for i in range(self.nr_entries)]

    def find_set(self, i):
        for set in self.sets:
            if i in set:
                return set

    def union(self, i, j):
        for set in self.sets:
            if i in set:
                set_i = set
            if j in set:
                set_j = set

        self.sets.remove(set_i)
        self.sets.remove(set_j)
        
        # extending happens in situ
        set_i.extend(set_j)
        self.sets.append(set_i)

    def get_mst(self):
        self.dist_list.sort() # Sort the distances in ascending order
        for dist, i, j in self.dist_list:
            if self.find_set(i) is not self.find_set(j):
                self.mst.append((dist, i, j))
                self.union(i, j)
        return self.mst
