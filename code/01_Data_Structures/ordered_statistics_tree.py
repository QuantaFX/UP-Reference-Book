class OrderedSet:
    def __init__(self):
        self.root = None

    def insert(self, x):
        if self.contains(x):
            return
        l, r = split(self.root, x)
        self.root = merge(merge(l, Node(x)), r)

    def erase(self, x):
        self.root = self._erase(self.root, x)

    def _erase(self, t, x):
        if not t:
            return None
        if t.key == x:
            return merge(t.left, t.right)
        elif x < t.key:
            t.left = self._erase(t.left, x)
        else:
            t.right = self._erase(t.right, x)
        pull(t)
        return t

    def contains(self, x):
        t = self.root
        while t:
            if t.key == x:
                return True
            t = t.left if x < t.key else t.right
        return False

    def order_of_key(self, x):
        t = self.root
        res = 0
        while t:
            if x <= t.key:
                t = t.left
            else:
                res += 1 + size(t.left)
                t = t.right
        return res

    def find_by_order(self, k):
        t = self.root
        while t:
            left_sz = size(t.left)
            if k < left_sz:
                t = t.left
            elif k == left_sz:
                return t.key
            else:
                k -= left_sz + 1
                t = t.right
        return None
