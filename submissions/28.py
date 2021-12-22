class Solution(object):

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """   

        len_haystack, len_needle = len(haystack), len(needle)
          
        if len_needle == 0:
            return 0
    
        for i in range(len_haystack-len_needle+1):
            if haystack[i:i+len_needle] == needle:
                return i     
        return -1     

# HAYSTACK = input('Please input haystack: ')
# NEEDLE = input('Please input needle: ')
HAYSTACK='sdafdsafsafunction'
NEEDLE='function'


print('haystack is "{}" and needle is "{}"'.format(HAYSTACK, NEEDLE))

s = Solution()
print(s.strStr(HAYSTACK, NEEDLE))