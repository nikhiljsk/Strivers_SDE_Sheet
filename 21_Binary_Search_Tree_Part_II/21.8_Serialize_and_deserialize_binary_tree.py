# Approach 1
# O(N), O(1)
class Codec:

    def serialize(self, root):
        arr = list()
        q = collections.deque([root,])
        while q:
            node = q.popleft()
            if node:
                arr.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                arr.append("")
        return ','.join(arr)

    def deserialize(self, data):
        if not data:
            return
        
        arr = data.split(',')
        root = TreeNode(arr[0])
        queue = collections.deque([root])
        i = 1
        while queue:
            node = queue.popleft()
            if i < len(arr) and arr[i]:
                node.left = TreeNode(int(arr[i]))
                queue.append(node.left)
            i += 1
            if i < len(arr) and arr[i]:
                node.right = TreeNode(int(arr[i]))
                queue.append(node.right)
            i += 1
        return root