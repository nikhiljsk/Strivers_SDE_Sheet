// Approach 1
// O(N), O(1)
// For arrays, you do this sort of thing
func deleteNode(node *ListNode) {
	i := node
	for true {
		i.Val = i.Next.Val
		if i.Next.Next == nil {
			i.Next = nil
			break
		}
		i = i.Next
	}
}

// Approach 2
// O(1), O(1)
// Just assign the next val, and skip one node
func deleteNode(node *ListNode) {
	node.Val = node.Next.Val
	node.Next = node.Next.Next
}