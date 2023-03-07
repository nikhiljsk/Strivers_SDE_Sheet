// Approach 1
// O(N), O(N)
// Use a hashmap to store the node address, if found while iterating return else nil

// Approach 2
// O(N), O(1)
// Refer Notion for intuition or
// https://www.youtube.com/watch?v=QfbOhn0WZ88&list=PLgUwDviBIf0p4ozDR_kJJkONnb1wdx2Ma&index=38&ab_channel=takeUforward
// L1 = nC - L2
func detectCycle(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return nil
	}
	t, h := head, head
	var found bool
	for h != nil && h.Next != nil {
		h = h.Next.Next
		t = t.Next
		if t == h {
			found = true // Collided, so cycle exists
			break
		}
	}
	if !found {
		return nil
	}

	// Find the start point
	t = head
	for t != h {
		t = t.Next
		h = h.Next\
	}
	return t

}