from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_count = Counter(s1)
        s2_count = Counter()

        left, right = 0, 0
        
        while right < len(s1):
            s2_count[s2[right]] += 1
            right += 1
        
        if s1_count == s2_count:
            return True
        
        while right < len(s2):
            s2_count[s2[right]] += 1

            s2_count[s2[left]] -= 1
            if s2_count[s2[left]] == 0:
                del s2_count[s2[left]]
                
            left += 1
            right += 1

            if s1_count == s2_count:
                return True
        
        return False