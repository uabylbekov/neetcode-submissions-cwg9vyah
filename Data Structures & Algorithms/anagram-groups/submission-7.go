import (
	"slices"
	"maps"
)
func groupAnagrams(strs []string) [][]string {
	anagrams := make(map[[26]int][]string)
	for _, str := range strs {
		var key [26]int

		for _, s := range str {
			key[s - 'a']++
		}

		anagrams[key] = append(anagrams[key], str)
	}

	return slices.Collect(maps.Values(anagrams))
}
