class QuickFindUF:
    def __init__(self, N):
        self.id = []
        self.len = N
        for i in range(N):
            self.id.append(i)
        return 
    def connected(self, p, q):
        print(len(self.id), p, q)
        return self.id[p] == self.id[q]
    def union(self, p, q):
        pid = self.id[p]
        qid = self.id[q]
        for i in range(self.len):
            if self.id[i] == pid:
                self.id[i] = qid
        return

class QuickUnionUF:
    def __init__(self, N):
        self.id = []
        self.len = N
        for i in range(N):
            self.id.append(i)
        return
    def root(self, i):
        while(i != self.id[i]):
            i = self.id[i]
        return i
    def connected(self, p, q):
        return self.root(p) == self.root(q)
    def union(self, p, q):
        pid = self.root(p)
        qid = self.root(q)
        self.id[pid] = qid
        return 
    
class WeightedQuickUnionUF:
    def __init__(self, N):
        self.id = []
        self.size = [1]*N
        self.len = N
        
        for i in range(N):
            self.id.append(i)
    
    def root(self, i):
        while(i != self.id[i]):
            # compress path
            self.id[i] = self.id[self.id[i]]
            i = self.id[i]
        return i
    def connected(self, p, q):
        return self.root(p) == self.root(q)
    
    def union(self, p, q):
        root_p = self.root(p)
        root_q = self.root(q)
        if (root_p == root_q):
            return
        if (self.size[root_p] < self.size[root_q]):
            self.id[root_p] = root_q
            self.size[root_q] += root_p
        else:
            self.id[root_q] = root_p
            self.size[root_p] += root_q
        return 

if __name__ == "__main__":
    import timeit
    t = timeit.Timer()
    wqu = WeightedQuickUnionUF(5)
    print(wqu.connected(0,2))
    wqu.union(0,1)
    wqu.union(1,4)
    wqu.union(4,2)
    print(wqu.connected(0,2))
    print(t.timeit())

    t = timeit.Timer()
    wfu = QuickFindUF(5)
    print(wfu.connected(0,2))
    wfu.union(0,1)
    wfu.union(1,4)
    wfu.union(4,2)
    print(wfu.connected(0,2))
    print(t.timeit())
    