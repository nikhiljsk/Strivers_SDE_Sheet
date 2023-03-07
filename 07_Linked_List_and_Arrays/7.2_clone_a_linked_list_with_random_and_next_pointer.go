// Approach 1 - FAILED!
// The below approach points to the random address of original LL
func copyRandomList(head *Node) *Node {
	if head == nil {
		return nil
	}
	// Store Random address in array
	var storeRandom []*Node
	iter := head
	for iter != nil {
		storeRandom = append(storeRandom, iter.Random)
		iter = iter.Next
	}

	// Start creating base LL with Next
	iter = head
	preHead := &Node{}
	tail := preHead
	var storeNewRandom []*Node
	for iter != nil {
		temp := &Node{}
		temp.Val = iter.Val
		tail.Next = temp
		tail = temp
		storeNewRandom = append(storeNewRandom, temp)
		iter = iter.Next
	}

	// Start populating random
	iter = preHead.Next
	for i := 0; i < len(storeRandom); i++ {
		iter.Random = storeRandom[i].Val
		iter = iter.Next
	}

	return preHead.Next
}

// Approach 2 - Brute Force
// O(N), O(N)
func copyRandomList(head *Node) *Node {
	// Store Random address
	store := make(map[*Node]*Node)
	iter := head
	for iter != nil {
		// Create new node
		temp := &Node{}
		temp.Val = iter.Val
		// Store in Map
		store[iter] = temp
		iter = iter.Next
	}

	// Populate Random and Next
	iter = head
	for iter != nil {
		store[iter].Next = store[iter.Next]
		store[iter].Random = store[iter.Random]
		iter = iter.Next
	}

	return store[head]
}

// Python Code
// It is important to check if iter.next and iter.random are not None,
// Cause in GO, dict will return None wihtout causing issues.
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return head

        iter, newNodes = head, dict()

        while iter:
            temp = Node(iter.val)
            newNodes[iter] = temp
            iter = iter.next


        iter = head
        while iter:
            if iter.next:
                newNodes[iter].next = newNodes[iter.next]
            if iter.random:
                newNodes[iter].random = newNodes[iter.random]
            iter = iter.next

        return newNodes[head]
"""

// Approach 3
// 1. Make a copy of each node and insert it right next to the node,
// 2. Then populate Next and random values.
// 3. Then seperate those and return.
// O(N), O(1)
func copyRandomList(head *Node) *Node {
	// Step 1
	iter := head
	for iter != nil {
		// Create new node
		temp := &Node{}
		temp.Val = iter.Val
		// Insert next to it
		temp.Next = iter.Next
		iter.Next = temp
		iter = iter.Next.Next
	}

	// Step 2
	iter = head
	for iter != nil {
		// Populate random
		if iter.Random != nil {
			iter.Next.Random = iter.Random.Next
		}
		iter = iter.Next.Next
	}

	// Step 3
	iter = head
	newHead := &Node{}
	newTail := newHead
	for iter != nil {
		// Original Node
		temp := iter.Next.Next
		// Dummy Node
		newTail.Next = iter.Next
		// Restore Connection
		iter.Next = temp
		// Move Forward
		newTail = newTail.Next
		iter = iter.Next
	}

	return newHead.Next
}