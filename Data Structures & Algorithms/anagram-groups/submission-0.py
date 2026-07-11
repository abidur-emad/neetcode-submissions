class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for word in strs:
            counts = [0] * 26
            for c in word:
                index = ord(c) - ord('a')
                counts[index] += 1
            hashmap.setdefault(tuple(counts), []).append(word)
        return list(hashmap.values())