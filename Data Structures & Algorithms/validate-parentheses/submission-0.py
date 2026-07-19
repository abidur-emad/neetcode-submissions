class Solution:
    def isValid(self, s: str) -> bool:
        opened = []
        pairs = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for c in s:
            if c in pairs.values():
                opened.append(c)
            elif not opened or opened.pop() != pairs.get(c):
                return False
                
        return not opened