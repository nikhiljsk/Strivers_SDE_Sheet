# Approach 1
# O(3N), O(3N)
def getTreeTraversal(root):
    if not root: return []
    pre_res, in_res, post_res = list(), list(), list()
    stack = [[root, 1]]
    while len(stack) != 0:
        curr = stack.pop()
        # For Pre-order
        if curr[1] == 1:
            curr[1] += 1
            stack.append(curr)
            pre_res.append(curr[0].data)
            if curr[0].left:
                stack.append([curr[0].left, 1])

        # For In-order
        elif curr[1] == 2:
            curr[1] += 1
            stack.append(curr)
            in_res.append(curr[0].data)
            if curr[0].right:
                stack.append([curr[0].right, 1])

        # For post-order
        elif curr[1] == 3:
            post_res.append(curr[0].data)

    return [in_res, pre_res, post_res]