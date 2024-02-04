class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        reverse = ""
        numtostr = str(x)
        for i in range(len(numtostr)-1, -1, -1):
            reverse = reverse + numtostr[i]
        # Se puede borrar el bucle si se pone return = numtostr == reverse[::-1]
        return numtostr == reverse

# Llamar al método isPalindrome con x = 121
result = Solution().isPalindrome(121)
print(result)
