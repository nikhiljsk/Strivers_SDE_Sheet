# Approach 1
# O(N), O(W) - W is usually considered to be equal to N
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return root

        res, q = list(), collections.deque()
        q.append(root)

        while len(q) != 0:
            qLen = len(q)
            temp = list()
            for i in range(qLen):
                curr = q.popleft()
                temp.append(curr.val)

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            res.append(temp)

        return res


# Follow-up Question - Level order Traversal - Zig-zag or Spiral
# Approach 1
# O(N), O(W) - W is usually considered to be equal to N
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return root

        res, q, isReverse = list(), collections.deque(), False
        q.append(root)

        while len(q) != 0:
            qLen = len(q)
            temp = list()
            for i in range(qLen):
                curr = q.popleft()
                temp.append(curr.val)

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

            if isReverse:
                res.append(reversed(temp))
                isReverse = False
            else:
                res.append(temp)
                isReverse = True

        return res

# Approach 2 - Cleaner Code
# O(N), O(W)
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return root

        res, q, isReverse = list(), collections.deque(), False
        q.append(root)

        while len(q) != 0:
            qLen = len(q)
            temp = [0] * qLen
            for i in range(qLen):
                curr = q.popleft()
                if isReverse: temp[qLen-i-1] = curr.val
                else: temp[i] = curr.val

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

            res.append(temp)
            isReverse = not isReverse

        return res

# Approach 3 - Clever way of utilizing deque
# Trick is to flip the order of left and right when we are appending from left.
# O(N), O(W)
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        queue = collections.deque([root])
        res = []
        isReverse = False
        while queue:
            n = len(queue)
            level = []
            for i in range(n):
                if isReverse:
                    node = queue.pop()
                    if node.right: queue.appendleft(node.right)
                    if node.left: queue.appendleft(node.left)
                else:
                    node = queue.popleft()
                    if node.left: queue.append(node.left)
                    if node.right: queue.append(node.right)
                level.append(node.val)
            res.append(level)
            isReverse = not isReverse
        return res
