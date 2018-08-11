'''
2017.9.18
35.easy
Given a sorted array and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
'''


class Solution(object):
    '''
    search the first number bigger than target to insert
    if not find, insert target in tail
    '''

    def searchInsert(self, nums, target):  # by me (linear search)
        '''
        :type nums: List[int]
        :type target: int
        :rtype: int
        '''
        length = len(nums)
        for i in range(length):
            if nums[i] < target:
                continue
            elif nums[i] == target:
                return i
            else:
                nums.insert(i, target)
                return i
        nums.append(target)
        return length

    def searchInsert2(self, nums, target):  # by me (binary search)
        length = len(nums)
        low = 0
        high = length - 1
        mid = 0
        index = length
        while low <= high:
            mid = int((low + high) / 2) #或者 (low + high) // 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
                index = mid
            else:
                return mid
        nums.insert(index, target)
        return index


if __name__ == '__main__':
    nums = [1, 3, 5, 6]
    target = 0
    print(Solution().searchInsert(nums, target))
    print(nums)
