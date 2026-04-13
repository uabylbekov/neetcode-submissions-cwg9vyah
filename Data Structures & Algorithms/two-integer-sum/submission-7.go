func twoSum(nums []int, target int) []int {
    seen := make(map[int]int)
    for i, num := range nums {
        potential := target - num
            if j, ok := seen[potential]; ok {
            return []int{j, i}
        }
        seen[num] = i
    }

    return []int{-1, -1}
}
