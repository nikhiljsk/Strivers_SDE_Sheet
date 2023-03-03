# Approach 1 - Recursive
# O(N), O(H)
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return None
        l, r, nex = root.left, root.right, root.next
        if l:
            l.next = r
            if nex:
                r.next = nex.left
            self.connect(l)
            self.connect(r)

        return root


# Approach 2 - Iterative
# O(N), O(1)
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root

        curr = root
        while curr.left:
            temp = curr
            while curr:
                curr.left.next = curr.right
                if curr.next:
                    curr.right.next = curr.next.left
                else:
                    curr.right.next = None
                curr = curr.next
            curr = temp.left

        return root
