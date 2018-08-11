'''
2017.9.23
53.
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
'''


class Solution(object):
    def maxSubArray(self, nums):
        '''
        :type nums: List[int]
        :rtype: int
        '''
        max_num = max(nums)
        if max_num <= 0:
            return max_num
        current_max = 0
        max_result = -2 ** 31
        for i in nums:
            if i + current_max <= 0:
                current_max = 0
            else:
                current_max += i
            max_result = max(max_result, current_max)
        return max_result


if __name__ == '__main__':
    test = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(Solution().maxSubArray(test))
