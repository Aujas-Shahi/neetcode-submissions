class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        strs = ""
        if len(s) != len(t):
            return False
        s = sorted(s)
        t = sorted(t)

        return s==t


        