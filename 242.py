class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        hashS = {}
        hashT = {}
        for i in range(len(s)):
            hashS[s[i]] = hashS.get(s[i], 0) + 1
            hashT[t[i]] = hashT.get(t[i], 0) + 1

        return hashS == hashT


if __name__ == "__main__":
    s = "aacc"
    t = "ccac"
    print(Solution().isAnagram(s, t))

