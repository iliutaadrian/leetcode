class Solution(object):

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        start, end = 0, len(x) - 1
        while start < end:
            while x[start].isalnum() == False and start < end:
                start += 1
            while x[end].isalnum() == False and start < end:
                end -= 1

            if x[start].lower() != x[end].lower():
                return False
            start += 1
            end -= 1

        return True


if __name__ == "__main__":
    print(Solution().isPalindrome("race a car"))

