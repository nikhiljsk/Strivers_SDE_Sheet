# Approach 1
# O(N2), O(N)
# Try to empty the stack and put element one by one in right position
def insert_at_pos(stack, x):
    if len(stack) == 0 or stack[-1] < x:
        stack.append(x)
    else:
        tmp = stack.pop()
        insert_at_pos(stack, x)
        stack.append(tmp)


def helper(stack):
    if len(stack) != 0:
        x = stack.pop()
        helper(stack)
        insert_at_pos(stack, x)


def sortStack(stack):
    helper(stack)
    return stack



# Similar to the above revesing a stack code
# O(N2), O(N)
def insert_at_bottom(stack, x):
    if len(stack) == 0:
        stack.append(x)
    else:
        tmp = stack.pop()
        insert_at_bottom(stack, x)
        stack.append(tmp)


def helper2(stack):
    if len(stack) != 0:
        x = stack.pop()
        helper2(stack)
        insert_at_bottom(stack, x)


def reverse(stack):
    helper2(stack)
    return stack


# Driver code
a = [3, 2, 1, 4]
# print("Reverse:", reverse(a))
print("Sorted:", sortStack(a))