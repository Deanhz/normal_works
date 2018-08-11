'''
2017.9.23
66.
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.
'''


class Solution(object):
    def plusOne(self, digits):  # by me
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = list(map(str, digits))
        number = int(''.join(digits))
        number = number + 1
        result = []
        for char in str(number):
            result.append(int(char))
        return result

    def plusOne2(self, digits):  # by me
        digits = digits[::-1]
        n = 0
        length = len(digits)
        for ind in range(length):
            if ind == 0:
                digits[ind] = digits[ind] + 1
            else:
                digits[ind] = digits[ind] + n
            n = digits[ind] // 10
            if n == 0:
                continue
            else:
                digits[ind] = digits[ind] % 10
                if ind == length - 1:
                    digits.append(1)
        digits = digits[::-1]
        return digits

    def plusOne3(self, digits):  # by me, this is efficient
        length = len(digits)
        n = 0
        for ind in range(length)[::-1]:
            if ind == length - 1:
                digits[ind] = digits[ind] + 1
            else:
                digits[ind] = digits[ind] + n
            n = digits[ind] // 10
            if n == 0:
                continue
            else:
                digits[ind] = digits[ind] % 10
                if ind == 0:
                    digits.insert(0, 1)
        return digits


if __name__ == "__main__":
    test = [1, 2, 3]
    print(Solution().plusOne3(test))
