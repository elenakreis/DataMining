class DHClustering:
    def __init__(self, mst):
        self.mst = mst

    def get_sets_helper(self, lst):
        for element in lst:
            for _, a, b in self.mst:
                if a is element and b not in lst:
                    lst.append(b)
                if b is element and a not in lst:
                    lst.append(a)
        return set(lst)

    def get_sets(self, edge):
        dist, i, j = edge

        set_i = self.get_sets_helper([i])
        set_j = self.get_sets_helper([j])

        return set_i, set_j

    def make_clusters_helper(self, elements):
        if(len(elements) == 1): 
            return elements.pop()
        edge = self.mst.pop()
        dist, _, _ = edge
        set1, set2 = self.get_sets(edge) 
        return (dist, self.make_clusters_helper(set1), self.make_clusters_helper(set2))

    def make_clusters(self):
        all_elements = set([])
        for _, i, j in self.mst:
            all_elements.add(i)
            all_elements.add(j)
        return self.make_clusters_helper(all_elements)
