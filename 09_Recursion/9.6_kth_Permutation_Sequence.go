// Approach 1
// O(N! * N)
// Use recursion to generate all permutations, sort and return

// Approach 2
// O(N*N), O(N)
func delNum(slice []int, s int) []int {
	return append(slice[:s], slice[s+1:]...)
}

func IntToString(a []int) string {
	b := make([]string, len(a))
	for i, v := range a {
		b[i] = strconv.Itoa(v)
	}

	return strings.Join(b, "")
}

func getPermutation(n int, k int) string {
	fact := 1
	var numbers []int
	for i := 1; i < n; i++ {
		numbers = append(numbers, i)
		fact *= i
	}
	numbers = append(numbers, n)
	fmt.Println(numbers, fact)

	k -= 1
	var ans []int
	for true {
		ans = append(ans, numbers[k/fact])
		numbers = delNum(numbers, k/fact)
		if len(numbers) == 0 {
			break
		}
		k = k % fact
		fact = fact / len(numbers)
	}
	return IntToString(ans)
}

"""
// Python Code
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fact = 1
        nums = list()
        for i in range(1, n):
            nums.append(i)
            fact *= i
        nums.append(n)

        k-=1
        ans = list()
        while True:
            ind = k//fact
            ans.append(str(nums[ind]))
            nums.pop(ind)
            if len(nums) == 0:
                break
            k %= fact
            fact //=  len(nums)

        return ''.join(ans)
"""