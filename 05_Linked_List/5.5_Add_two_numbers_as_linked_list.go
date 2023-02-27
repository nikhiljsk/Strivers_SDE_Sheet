// Approach 1
// Only optimal solution exists
// O(max(N, M)), O(1)
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	newHead := &ListNode{}
	newTail := newHead
	i, j := l1, l2
	carry := 0
	for i != nil || j != nil || carry != 0 {
		sum := 0
		if i != nil {
			sum += i.Val
			i = i.Next
		}
		if j != nil {
			sum += j.Val
			j = j.Next
		}

		sum += carry
		carry = sum / 10

		temp := &ListNode{Val: sum % 10}
		newTail.Next = temp
		newTail = temp
	}
	return newHead.Next
}