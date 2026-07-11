class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def count_letters(s: str) -> dict:
            counts = {}
            for c in s:
                counts[c] = counts.get(c, 0) + 1
            return counts
        return count_letters(s) == count_letters(t)
