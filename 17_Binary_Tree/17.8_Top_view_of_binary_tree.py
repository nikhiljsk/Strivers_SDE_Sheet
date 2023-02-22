# Approach 1 - BFS - Own Solution
# O(N*LogN), O(W)
class Solution:
    def topView(self,root):
        ds = dict()
        # Root, Column (y)
        q = collections.deque([(root, 0)])

        while len(q) != 0:
            root, y = q.popleft()
            if root.left: q.extend([(root.left, y-1)])
            if root.right: q.extend([(root.right, y+1)])

            if y not in ds:
                ds[y] = root.data

        res = list()
        for key in sorted(ds.keys()):
            res.append(ds[key])

        return res


# Approach 2 - DFS
# O(N*LogN), O(H)
class Solution:
    def helper(self, root, x, y, ds):
        if not root: return

        if y in ds:
            if x < ds[y][0]:
                ds[y] = [x, root.data]
        else:
            ds[y] = [x, root.data]

        self.helper(root.left, x+1, y-1, ds)
        self.helper(root.right,x+1, y+1, ds)


    def topView(self, root):
        ds = dict()

        self.helper(root, 0, 0, ds)
        res = list()
        for key in sorted(ds.keys()):
            res.append(ds[key][1])
        return res