// O(N/2), O(1)
func middleNode(head *ListNode) *ListNode {
	t, h := head, head
	for h != nil && h.Next != nil {
		t = t.Next
		h = h.Next.Next
	}
	return t
}