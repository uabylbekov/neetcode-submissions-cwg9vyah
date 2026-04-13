func twoSum(nums []int, target int) []int {
    seen := make(map[int]int)

    for i, num := range nums {
        diff := target - num
        if _, ok := seen[diff]; ok {
            return []int {seen[diff], i}
        }
        seen[num] = i
    }
    return []int {-1, -1}
}
