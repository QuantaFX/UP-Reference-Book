BITS = 15
MAXV = 1 << BITS

class MisofTree:
    def __init__(self):
        self.cnt = [[0, 0] for _ in range(1 << (BITS + 1))]
        self.root = 1
        self.nodes = 2

    def _new_node(self):
        idx = self.nodes
        self.nodes += 1
        if idx >= len(self.cnt):
            self.cnt.append([0, 0])
        return idx

    def insert(self, x):
        node = self.root
        for i in reversed(range(BITS)):
            b = (x >> i) & 1
            self.cnt[node][b] += 1

            nxt = self.cnt[node].__len__()
            if not hasattr(self, "child"):
                self.child = {}

            if (node, b) not in self.child:
                self.child[(node, b)] = self._new_node()

            node = self.child[(node, b)]

    def erase(self, x):
        node = self.root
        path = []

        for i in reversed(range(BITS)):
            b = (x >> i) & 1
            path.append((node, b))
            node = self.child[(node, b)]

        for node, b in path:
            self.cnt[node][b] -= 1

    def kth(self, k):
        node = self.root
        res = 0

        for i in reversed(range(BITS)):
            left = self.cnt[node][0]

            if k < left:
                node = self.child.get((node, 0), node)
            else:
                k -= left
                res |= (1 << i)
                node = self.child.get((node, 1), node)

        return res
