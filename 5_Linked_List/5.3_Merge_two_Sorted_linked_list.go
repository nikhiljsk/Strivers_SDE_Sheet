// Approach 1
// O(N), O(1)
func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
	if list1 == nil {
		return list2
	}
	if list2 == nil {
		return list1
	}
	// Init the NewHead
	i, j := list1, list2
	var newHead, newTail *ListNode
	if i.Val <= j.Val {
		newHead = i
		i = i.Next
	} else {
		newHead = j
		j = j.Next
	}
	newTail = newHead

	// Start Merge
	for i != nil && j != nil {
		if i.Val <= j.Val {
			newTail.Next = i
			newTail = i
			i = i.Next
		} else {
			newTail.Next = j
			newTail = j
			j = j.Next
		}
	}

	// Handle trailing nodes
	if i != nil {
		newTail.Next = i
	}
	if j != nil {
		newTail.Next = j
	}

	return newHead
}

// Approach 2
// A cleaner approach
// O(N), O(1)
func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
	if list1 == nil {
		return list2
	}
	if list2 == nil {
		return list1
	}
	// Init the NewHead
	i, j := list1, list2
	var newHead, newTail *ListNode
	if i.Val <= j.Val {
		newHead = i
		i = i.Next
	} else {
		newHead = j
		j = j.Next
	}
	newTail = newHead

	// Start Merge
	for i != nil || j != nil {
		if i == nil {
			newTail.Next = j
			break
		} else if j == nil {
			newTail.Next = i
			break
		} else if i.Val <= j.Val {
			newTail.Next = i
			newTail = i
			i = i.Next
		} else {
			newTail.Next = j
			newTail = j
			j = j.Next
		}
	}
	return newHead
}