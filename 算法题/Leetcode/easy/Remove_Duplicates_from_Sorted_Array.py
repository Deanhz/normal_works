"""
2017.9.16
26.
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this in place with constant memory.
For example,
Given input array A = [1,1,2],
Your function should return length = 2, and A is now [1,2].
"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length <= 1:
            return length
        n = 0
        lastchar = nums[0]
        for index in range(length):
            curChar = nums[index - n]
            if index == 0:
                continue
            # print("index:{},curChar:{},lastchar:{}".format(
            #     str(index), curChar, lastchar))
            if curChar == lastchar:
                n += 1
                lastchar = curChar
                del(nums[index - n])
                continue
            lastchar = curChar
        # print(nums)
        return length - n

    # def removeDuplicates2(self, nums): # this is wrong,because nums is not change
    #     if len(nums) == 0:
    #         return 0
    #     n = 1
    #     lastchar = nums[0]
    #     for index, char in enumerate(nums):
    #         if index == 0:
    #             continue
    #         if char != lastchar:
    #             n += 1
    #         lastchar = char
    #     nums = list(set(nums)) # this is wrong,because nums is not change
    #     return n


if __name__ == "__main__":
    t = [1, 1, 2]
    print(Solution().removeDuplicates(t))
    print(t)

#总结
#del()函数，会直接改变原来的数据。
#for index,char in enumerate(nums) 的index是一直都在递增的，如果在循环体中改变了nums，那么enumerate(nums)会变化。
#for i in range(len(nums))，内部改变了nums，头部没有影响，应为range(len(nums))在第一次生成一个固定的list。
