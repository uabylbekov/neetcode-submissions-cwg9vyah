import "slices"

func isAnagram(s string, t string) bool {
    s_slice := make([]int, 26)
    t_slice := make([]int, 26)

    for _, char := range s {
        s_slice[char - 'a'] += 1
    }

    for _, char := range t {
        t_slice[char - 'a'] += 1
    }

    return slices.Equal(s_slice, t_slice)
}
