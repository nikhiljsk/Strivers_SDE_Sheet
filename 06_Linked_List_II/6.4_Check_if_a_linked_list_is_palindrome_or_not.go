package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func reverseLL(head *ListNode) *ListNode {
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

func isPalindrome(head *ListNode) bool {
	if head == nil || head.Next == nil {
		return head != nil
	}
	middle, end := head, head
	// This is the tricky part, this is different from the middle node problem. This is the actual logic to find the floor of middle.
	for end.Next != nil && end.Next.Next != nil {
		end = end.Next.Next
		middle = middle.Next
	}

	middle.Next = reverseLL(middle.Next)
	middle = middle.Next

	for head != nil && middle != nil {
		if head.Val != middle.Val {
			return false
		}
		head = head.Next
		middle = middle.Next
	}
	return true
}
