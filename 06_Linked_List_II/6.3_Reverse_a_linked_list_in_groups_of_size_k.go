// Approach 1 - FAILED!
// The reason this fails is, the method reverses the LL k nodes at a time
// But the actual question is totally different
// This returns 4-3-2-1 instead of 2-1-4-3
func reverse(prev, start, end *ListNode) {
	if start == nil || start.Next == nil {
		return
	}
	l := prev
	m, r := start, start.Next
	for m != end {
		m.Next = l
		l = m
		m = r
		r = r.Next
	}
	m.Next = l
}

func reverseKGroup(head *ListNode, k int) *ListNode {
	var prev *ListNode
	sNode, kNode := head, head
	count := k - 1
	for kNode != nil && kNode.Next != nil && count != 0 {
		kNode = kNode.Next
		count--
		if count == 0 {
			fmt.Println("TEST", sNode.Val, kNode.Val)
			temp := kNode.Next
			reverse(prev, sNode, kNode)
			fmt.Println("Test Now", kNode.Val)
			prev = kNode
			sNode, kNode = temp, temp
			count = k - 1
		}
	}
	return prev
}

// Approach 2 - Python
// This approach is sort off the above approach but with the right intuition
// O(N), O(K)
class Solution(object):
    def reverseKGroup(self, head, k):
        count, node = 0, head
        while node and count < k:
            node = node.next
            count += 1
        if count < k: return head
        new_head, prev = self.reverse(head, count)
        head.next = self.reverseKGroup(new_head, k)
        return prev
    
    def reverse(self, head, count):
        prev, cur, nxt = None, head, head
        while count > 0:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            count -= 1
        return (cur, prev)

// Approach 3
// O(N), O(1)
// TODO: Check this again
func reverseKGroup(head *ListNode, k int) *ListNode {
    if head == nil || k == 1 {
        return head
    }
    dummy := &ListNode{}
    dummy.Next = head
    cur, nex, pre := dummy, dummy, dummy
    count := 0

    // Len of LL
    for cur.Next != nil {
        count++
        cur = cur.Next
    }

    for count >= k {
        cur = pre.Next
        nex = cur.Next
        for i:=0; i<k-1; i++{
            cur.Next = nex.Next
            nex.Next = pre.Next
            pre.Next = nex
            nex = cur.Next
        }
        pre = cur
        count -= k
    }
    return dummy.Next

}