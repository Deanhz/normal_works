'''
2017.9.18
28.
实现strstr(). 返回needle(关键字)在haystack(字符串)中第一次出现的位置，如果needle不在haystack中，则返回-1。 
'''


class Solution(object):
    def strStr(self, haystack, needle):  # by me
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        length = len(needle)
        length2 = len(haystack)
        if length == 0:
            return 0
        if length2 < length:
            return -1
        if haystack == needle:
            return 0
        for index in range(length2 - length + 1):
            s = haystack[index:index + length]
            if s == needle:
                return index
        return -1


if __name__ == '__main__':
    haystack = 'mississippi'
    needle = 'pi'
    print(Solution().strStr(haystack, needle))
