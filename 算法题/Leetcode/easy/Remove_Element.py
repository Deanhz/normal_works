'''
2017.9.18
27.
Given an array and a value, remove all instances of that value in place and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:
Given input array nums = [3,2,2,3], val = 3

Your function should return length = 2
'''


class Solution(object):
    def removeElement(self, nums, val):  # by me
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = len(nums)
        n = 0
        for i in range(length):
            if nums[i - n] == val:
                del(nums[i - n])
                n += 1
        return length - n

    def removeElement2(self, nums, val):  # use while
        length = len(nums)
        a = length
        i = 0
        while i < a:
            if nums[i] == val:
                del(nums[i])
                a = a - 1
                continue
            i += 1
        return a


if __name__ == "__main__":
    test = [3, 2, 2, 3, 1, 2, 3, 4]
    print(Solution().removeElement2(test, 2))
    print(test)

#总结
#for和while是不同的，第一种方法，使用for循环，for i in range(length)，此时就已经固定了循环的index,
#因为range(length)生成一个固定的list，length变化不会影响for头部。
#而第二种方法while语句，是判断条件是否成立。
