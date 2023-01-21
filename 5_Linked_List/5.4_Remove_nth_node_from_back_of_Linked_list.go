// Approach 1
// O(N), O(1)
func removeNthFromEnd(head *ListNode, n int) *ListNode {
	preHead := &ListNode{Next: head}
	t, h := preHead, head
	for i := 0; i < n && h != nil; i++ {
		h = h.Next
	}
	for h != nil {
		h = h.Next
		t = t.Next
	}
	t.Next = t.Next.Next
	return preHead.Next
}

// Approach 2
// Same as above, but slightly different in terms of starting/stopping condition of hare
// O(N), O(1)
func removeNthFromEnd(head *ListNode, n int) *ListNode {
	preHead := &ListNode{Next: head}
	t, h := preHead, preHead
	for i := 0; i < n; i++ {
		h = h.Next
	}
	for h.Next != nil {
		h = h.Next
		t = t.Next
	}
	t.Next = t.Next.Next
	return preHead.Next
}