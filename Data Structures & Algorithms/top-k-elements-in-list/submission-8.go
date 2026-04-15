func topKFrequent(nums []int, k int) []int {
	freq := make(map[int]int)
	for _, num := range nums {
		freq[num]++
	}

	bucket := make([][]int, len(nums)+1)
	for i, v := range freq {
		bucket[v] = append(bucket[v], i)
	}

	result := make([]int, 0, 0)
	for i := len(bucket)-1; i > -1; i-- {
		for _, v := range bucket[i] {
			result = append(result, v)
			k--
			if k == 0 {
				return result
			}
		}
	}

	return result
}
