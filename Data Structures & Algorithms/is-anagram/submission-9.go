func isAnagram(s string, t string) bool {

    if len(s) != len(t) {
        return false
    }

    sCount := [26]int{}
    tCount := [26]int{}

    for _, v := range s {
        sCount[v - 'a'] += 1
    }

     for _, v := range t {
        tCount[v - 'a'] += 1
    }

    return sCount == tCount
}
