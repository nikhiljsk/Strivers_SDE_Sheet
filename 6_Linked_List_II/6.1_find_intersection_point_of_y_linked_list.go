// Approach 1
// O(2N), O(N)
func getIntersectionNode(headA, headB *ListNode) *ListNode {
	found := make(map[*ListNode]bool)
	i, j := headA, headB
	for i != nil {
		found[i] = true
		i = i.Next
	}
	for j != nil {
		if _, ok := found[j]; ok {
			return j
		}
		j = j.Next
	}
	return nil
}

// Approach 2
// O(2N), O(1)
func getIntersectionNode(headA, headB *ListNode) *ListNode {
	i, j := headA, headB
	for i != j {
		if i == nil {
			i = headB
		} else {
			i = i.Next
		}
		if j == nil {
			j = headA
		} else {
			j = j.Next
		}
	}
	return i
}