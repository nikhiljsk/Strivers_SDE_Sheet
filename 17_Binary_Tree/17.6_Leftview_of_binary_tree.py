# Appraoch 1 - Recursive
# O(N), O(H) - H is height of BT
def helper(root, level, res):
    if not root:
        return
    if level == len(res):
        res.append(root.data)
    helper(root.left, level+1, res)
    helper(root.right, level+1, res)

def LeftView(root):
    res = list()
    helper(root, 0, res)
    return res


# Approach 2 - Iterative - Level order Traversal or BFS
# O(N), O(B) - B is Breadth of BT
from collections import deque
def LeftView(root):
    if not root: return []

    q, res = deque([root]), list()
    while len(q) != 0:
        leftNode = None
        qLen = len(q)
        for i in range(len(q)):
            leftNode = q.popleft()
            if leftNode.right:
                q.append(leftNode.right)
            if leftNode.left:
                q.append(leftNode.left)
        res.append(leftNode.data)
    return res



# Follow-up question - Right View of BT
# Approach 1 - Recursive
# O(N), O(H) - H is height of BT
def helper(root, level, res):
    if not root:
        return
    if level == len(res):
        res.append(root.data)
    helper(root.right, level+1, res)
    helper(root.left, level+1, res)

def RightView(root):
    res = list()
    helper(root, 0, res)
    return res

# Approach 2 - Iterative - Level Order Traversal or BFS
# O(N), O(B) - B is Breadth of BT
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return root

        q, res = deque([root]), list()
        while len(q) != 0:
            rightNode = None
            qLen = len(q)
            for i in range(len(q)):
                rightNode = q.popleft()
                if rightNode.left:
                    q.append(rightNode.left)
                if rightNode.right:
                    q.append(rightNode.right)
            res.append(rightNode.val)
        return res