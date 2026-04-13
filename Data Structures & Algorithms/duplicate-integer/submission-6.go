func hasDuplicate(nums []int) bool {
    seen := make(map[int]int)
    for _, num := range nums {
        if _, ok := seen[num]; ok {
            return true
        }
        seen[num] = num
    }
    return false
}
