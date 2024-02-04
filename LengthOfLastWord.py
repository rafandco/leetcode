class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split()[len(s.split())-1])


# Llamar al método isPalindrome con x = 121
result = Solution().lengthOfLastWord("Hello World")
print(result)