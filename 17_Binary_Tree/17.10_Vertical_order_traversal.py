# Approach 1 - BFS
# O(N LogN), O(2N)
class Solution:
        def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
            ds = collections.defaultdict(list)
            # Root, Row (x), Column (y)
            q = collections.deque([(root, 0, 0)])

            while len(q) != 0:
                root, x, y = q.popleft()
                if root.left: q.extend([(root.left, x+1, y-1)])
                if root.right: q.extend([(root.right, x+1, y+1)])

                ds[(x, y)].append(root.val)

            res = collections.defaultdict(list)
            keys = sorted(ds.keys(), key = lambda x: (x[1], x[0]))
            for key in keys:
                x, y = key
                res[y] += sorted(ds[key])

            return res.values()

# Approach 2 - DFS
# O(N LogN), O(2N)
class Solution:
        def helper(self, root, x, y, ds):
            if not root: return
            ds[(x,y)] += [root.val]
            self.helper(root.left, x+1, y-1, ds)
            self.helper(root.right, x+1, y+1, ds)

        def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
            ds = collections.defaultdict(list)
            self.helper(root, 0, 0, ds)

            res = collections.defaultdict(list)
            keys = sorted(ds.keys(), key = lambda x: (x[1], x[0]))
            for key in keys:
                x, y = key
                res[y] += sorted(ds[key])

            return res.values()