# Approach 1
# O(All nodes), O(N) - If solution space is considered
# Recursive approach
def mergeTwoLL(a, b):
    res = Node(0)
    temp = res
    while a!=None or b!=None:
        if a == None:
            temp.bottom = b
            break
        elif b == None:
            temp.bottom = a
            break
        elif a.data < b.data:
            temp.bottom = a
            temp = a
            a = a.bottom
        else:
            temp.bottom = b
            temp = b
            b = b.bottom
    
    return res.bottom
            
            
def flatten(root):
    # Base Condition
    if root == None or root.next == None:
        return root
    
    # Start recursion to the last set
    root.next = flatten(root.next)
    
    # Once it reaches here, start merging
    root = mergeTwoLL(root, root.next)
    
    return root


# Approach 1
# O(All nodes), O(N) - If solution space is considered
# Iterative approach - Start from the beginning
def mergeTwoLL(a, b):
    res = Node(0)
    temp = res
    while a!=None or b!=None:
        if a == None:
            temp.bottom = b
            break
        elif b == None:
            temp.bottom = a
            break
        elif a.data < b.data:
            temp.bottom = a
            temp = a
            a = a.bottom
        else:
            temp.bottom = b
            temp = b
            b = b.bottom
    
    return res.bottom


def flatten(root):
    while root and root.next:
        temp = root.next.next
        root = mergeTwoLL(root, root.next)
        root.next = temp
    return root
