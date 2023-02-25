# Approach 1 - Recursive
# O(N), O(N)
def changeTree(root): 
    if not root: return

    child_sum = 0
    if root.left: child_sum += root.left.data
    if root.right: child_sum += root.right.data

    if child_sum > root.data:
        root.data = child_sum
    else:
        if root.left: root.left.data = root.data
        if root.right: root.right.data = root.data
    
    changeTree(root.left)
    changeTree(root.right)

    total = 0
    if root.left: total += root.left.data
    if root.right: total += root.right.data
    if root.data < total: root.data = total