class SplayTree:
    def __init__(self, arr=None):
        self.root = None
        if arr:
            self.root = self.build(arr, 0, len(arr))
    def build(self, arr, l, r):
        if l >= r:
            return None
        m = (l + r) // 2
        node = Node(arr[m])
        node.left = self.build(arr, l, m)
        node.right = self.build(arr, m + 1, r)
        if node.left:
            node.left.parent = node
        if node.right:
            node.right.parent = node
        self.pull(node)
        return node
    def pull(self, x):
        x.size = 1
        if x.left:
            x.size += x.left.size
        if x.right:
            x.size += x.right.size
    def push(self, x):
        if x and x.rev:
            x.left, x.right = x.right, x.left
            if x.left:
                x.left.rev ^= True
            if x.right:
                x.right.rev ^= True
            x.rev = False
    def rotate(self, x):
        p = x.parent
        g = p.parent

        if p.left == x:
            b = x.right
            x.right = p
            p.left = b
        else:
            b = x.left
            x.left = p
            p.right = b
        if b:
            b.parent = p
        x.parent = g
        if g:
            if g.left == p:
                g.left = x
            else:
                g.right = x
        p.parent = x
        self.pull(p)
        self.pull(x)
    def splay(self, x):
        if not x:
            return None

        while x.parent:
            p = x.parent
            g = p.parent

            if g:
                self.push(g)
            self.push(p)
            self.push(x)

            if not g:
                self.rotate(x)
            elif (g.left == p) == (p.left == x):
                self.rotate(p)
                self.rotate(x)
            else:
                self.rotate(x)
                self.rotate(x)

        self.root = x
        return x

    def kth(self, k):
        x = self.root
        while x:
            self.push(x)
            lsize = x.left.size if x.left else 0

            if k < lsize:
                x = x.left
            elif k > lsize:
                k -= lsize + 1
                x = x.right
            else:
                return self.splay(x)
        return None

    def split(self, k):
        if k == 0:
            r = self.root
            self.root = None
            return None, r

        x = self.kth(k - 1)

        right = x.right
        if right:
            right.parent = None

        x.right = None
        self.pull(x)

        return x, right

    def merge(self, left, right):
        if not left:
            return right
        if not right:
            return left

        x = left
        while True:
            self.push(x)
            if not x.right:
                break
            x = x.right

        while x.parent:
            if x.parent.parent:
                if (x.parent.left == x) == (x.parent.parent.left == x.parent):
                    self.rotate(x.parent)
                else:
                    self.rotate(x)
            self.rotate(x)

        x.right = right
        right.parent = x
        self.pull(x)

        return x

    def insert(self, k, val):
        left, right = self.split(k)
        node = Node(val)
        merged = self.merge(left, node)
        self.root = self.merge(merged, right)

    def _split_root(self, root, k):
        if not root:
            return None, None
        self.root = root
        return self.split(k)

    def erase(self, k):
        left, temp = self.split(k)
        mid, right = self._split_root(temp, 1)
        self.root = self.merge(left, right)

    def reverse(self, l, r):
        left, temp = self.split(l)
        mid, right = self._split_root(temp, r - l + 1)

        if mid:
            mid.rev ^= True

        merged = self.merge(left, mid)
        self.root = self.merge(merged, right)

    def assign(self, k, val):
        node = self.kth(k)
        node.value = val
        self.pull(node)

    def inorder(self):
        res = []
        stack = []
        x = self.root

        while stack or x:
            while x:
                self.push(x)
                stack.append(x)
                x = x.left

            x = stack.pop()
            res.append(x.value)
            x = x.right

        return res

    def check_no_cycle(self):
        seen = set()

        def dfs(x):
            if not x:
                return
            if id(x) in seen:
                raise Exception("Cycle detected")
            seen.add(id(x))
            dfs(x.left)
            dfs(x.right)

        dfs(self.root)
