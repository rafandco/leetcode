class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        index = -1
        letter = ""
        for i in s:
            if s.count(i) == 1:
                letter += i
                break
            else:
                index += 1
        if index == len(s)-1:
            return -1
        else:
            return s.index(letter)

        

result = Solution().firstUniqChar("leetcode")
print(result)