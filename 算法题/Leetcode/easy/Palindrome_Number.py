class Solution(object):
    def isPalindrome(self, x):  # by me
        '''
        :type x: int
        :rtype: bool
        '''
        for index, val in enumerate(str(x)):
            length = len(str(x))
            if index >= length - index - 1:
                return True
            if str(x)[index] != str(x)[length - index - 1]:
                return False

    def isPalindrome2(self, x):
        str1 = str(x)
        str2 = str(x)
        str1 = str1[::-1]
        if str1 == str2:
            return True
        else:
            return False


if __name__ == '__main__':
    print(Solution().isPalindrome2(1221))
