# Approach - 1 - Iterative - BFS
# O(N), O(W)
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        q, res = deque(), 0
        q.append([root, 0])

        while len(q) != 0:
            qLen = len(q)
            res = max(res, q[-1][1] - q[0][1] + 1)
            for i in range(qLen):
                curr = q.popleft()
                node, dist = curr[0], curr[1]

                if node.left:
                    q.append([node.left, 2*dist])
                if node.right:
                    q.append([node.right, 2*dist+1])

        return res


# Approach 2 - Recursive - DFS
# To build a dictionary of levels, and the indices in each of them
# O(N), O(H)
from collections import defaultdict
class Solution:
    def helper(self, node, level, ind, di):
        if node:
            di[level].append(ind)
            self.helper(node.left, level+1, ind*2, di)
            self.helper(node.right, level+1, ind*2+1, di)

    def widthOfBinaryTree(self, root: TreeNode) -> int:
        di = defaultdict(list)
        self.helper(root, 0 , 0, di)

        res = 0
        for level in di:
            curr = max(di[level]) - min(di[level]) + 1
            res = max(res, curr)

        return res