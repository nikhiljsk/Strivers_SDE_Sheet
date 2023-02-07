# Approach 1 - Brute Force
# For every index (candidate), go through each row and each column to evaluate
# O(N2), O(1) - Where N is number of elements in matrix

# Approach 2
# O(M*N), O(M)
class Solution:

    def celebrity(self, M, n):
        stack = list()
        # Step 1 - Insert candidates
        for i in range(n):
            stack.append(i)

        # Step 2 - Pop 2 at a time
        while len(stack) > 1:
            a = stack.pop()
            b = stack.pop()
            if M[a][b] == 1:
                stack.append(b)
            else:
                stack.append(a)

        # Step 3 - Verify it is true celebrity
        res = stack.pop()
        for i in range(n): # Check for row and col
            if((i != res) and (M[res][i]==1 or M[i][res] == 0)):
                return -1
        return res

# Approach 3
# O(2M), O(1)
class Solution:

    def celebrity(self, M, n):
        #initializing two pointers for two corners.
        a = 0
        b = n-1
        
        while(a<b):
            if(M[a][b] == 1):
                a += 1
            else:
                b -= 1

        # Verify it is true celebrity
        res = b # or a
        for i in range(n): # Check for row and col
            if((i != res) and (M[res][i]==1 or M[i][res] == 0)):
                return -1
        return res