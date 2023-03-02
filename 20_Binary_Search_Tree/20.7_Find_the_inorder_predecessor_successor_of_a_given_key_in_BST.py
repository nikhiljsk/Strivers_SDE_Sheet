# Approach 1 - Naive
# O(N)+O(LogN), O(N)
# Using inorder traversal to create an array and then do BS to return the answer


# Approach 2 - Better
# O(N), O(1)
# Just use a inorder traversal with while loop, return when found the answer


# Approach 3 - Optimized
# O(H), O(1)
def findPre(root, target):
    curr = root
    res = None
    while curr:
        if curr.key < target:
            res = curr
            curr = curr.right
        elif curr.key >= target:
            curr = curr.left
    return res


def findSuc(root, target):
    curr = root
    res = None
    while curr:
        if curr.key <= target:
            curr = curr.right
        elif curr.key > target:
            res = curr
            curr = curr.left
    return res


def findPreSuc(root, pre, suc, key):
    pre[0] = findPre(root, key)
    suc[0] = findSuc(root, key)