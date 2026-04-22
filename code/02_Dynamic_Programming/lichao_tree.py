class Line:
    __slots__ = ['m', 'c']
    def __init__(self, m=0, c=float('-inf')):
        self.m = m
        self.c = c
        
    def eval(self, x):
        return self.m * x + self.c

class Node:
    __slots__ = ['line', 'left', 'right']
    def __init__(self):
        self.line = Line()
        self.left = None
        self.right = None

class LiChaoTree:
    def __init__(self, min_x=-10**12, max_x=10**12):
        self.root = Node()
        self.min_x = min_x
        self.max_x = max_x

    def add_line(self, m, c):
        self._insert(self.root, self.min_x, self.max_x, Line(m, c))

    def _insert(self, node, l, r, new_line):
        mid = (l + r) // 2
        
        left_better = new_line.eval(l) > node.line.eval(l)
        mid_better = new_line.eval(mid) > node.line.eval(mid)
        
        if mid_better:
            node.line, new_line = new_line, node.line
        if r - l <= 1:
            return
            
        if left_better != mid_better:
            if not node.left:
                node.left = Node()
            self._insert(node.left, l, mid, new_line)
        else:
            if not node.right:
                node.right = Node()
            self._insert(node.right, mid, r, new_line)

    def query(self, x):
        return self._query(self.root, self.min_x, self.max_x, x)

    def _query(self, node, l, r, x):
        if not node:
            return float('-inf')
        if r - l <= 1:
            return node.line.eval(x)
            
        mid = (l + r) // 2
        res = node.line.eval(x)
        
        if x < mid:
            res = max(res, self._query(node.left, l, mid, x))
        else:
            res = max(res, self._query(node.right, mid, r, x))
            
        return res