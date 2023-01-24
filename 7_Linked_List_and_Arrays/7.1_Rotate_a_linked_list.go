// Approach 1
// For each k, find the last element from the list. Move it to the first.
// O(k*n), O(1)

// Approach 2
// O(N), O(1)
func rotateRight(head *ListNode, k int) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}
	iter, count := head, 1
	for iter.Next != nil {
		count++
		iter = iter.Next
	}
	// Connect the last node and first
	iter.Next = head

	// Find the node to disconnect
	dis := count - (k % count)
	iter = head
	for i := 0; i < dis-1; i++ {
		iter = iter.Next
	}
	// Set the head to right of iter
	head = iter.Next
	// Disconnect
	iter.Next = nil

	return head
}