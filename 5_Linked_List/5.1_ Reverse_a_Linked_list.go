// O(N), O(1)
func reverseList(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}
	var l *ListNode
	m, r := head, head.Next
	for r != nil {
		m.Next = l
		l = m
		m = r
		r = r.Next
	}
	m.Next = l
	return m
}

// Python Code
"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        l = None
        m, r = head, head.next
        while r:
            m.next = l
            l = m
            m = r
            r = r.next
        m.next = l
        return m
"""