# Approach 1 - Recursive
# O(N), O(H)
class Solution:
    def helper(self, root, target, res):
        if not root: return False
        res.append(root.val)
        if root.val == target: return True

        if self.helper(root.left, target, res) or self.helper(root.right, target, res):
            return True

        res.pop()
        return False

    def solve(self, A, B):
        res = list()
        self.helper(A, B, res)
        return res


# Golang Solution
"""
func helper(root *treeNode, target int, res []int) (bool, []int) {
    if root == nil {
        return false, res
    }
    res = append(res, root.value)

    if root.value == target {
        return true, res
    }

    b1, res := helper(root.left, target, res)
    b2, res := helper(root.right, target, res)
    if b1 || b2 {
        return true, res
    }

    res = res[:len(res)-1]
    return false, res

}


func solve(A *treeNode , B int )  ([]int) {
    res := make([]int, 0)
    _, res = helper(A, B, res)
    return res
}
"""