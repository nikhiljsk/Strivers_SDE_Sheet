// Approach 1
// Use a hashmap to store the node and check
// O(N), O(N)

// Approach 2
// O(N), O(1)
func hasCycle(head *ListNode) bool {
	if head == nil || head.Next == nil {
		return false
	}
	t, h := head, head
	for h != nil && h.Next != nil {
		h = h.Next.Next
		t = t.Next
		if t == h {
			return true
		}
	}
	return false
}