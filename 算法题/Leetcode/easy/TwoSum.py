class Solution(object):
    def twoSum(self, nums, target):
        '''
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        '''
        for index, i in enumerate(nums):
            for indexj, j in enumerate(nums[index + 1:]):
                if i + j == target:
                    return [index, index + indexj + 1]

    def twoSum2(self, nums, target):
        for ind1, val in enumerate(nums):
            if target - val in nums:
                ind2 = nums.index(target - val)
                if ind1 != ind2:
                    return [ind1, nums.index(target - val)]

    def twoSum3(self, nums, target):
        for ind1, val in enumerate(nums):
            try:
                ind2 = nums.index(target - val)
                if ind1 != ind2:
                    return [ind1, ind2]
            except Exception:
                continue

    def twoSum4(self, nums, target):
        hash_map = {}
        for ind, val in enumerate(nums):
            hash_map[val] = ind
        for ind1, val in enumerate(nums):
            if target - val in hash_map:
                ind2 = hash_map[target - val]
                if ind1 != ind2:
                    return [ind1, ind2]


if __name__ == "__main__":
    nums = [3, 2, 4]
    target = 6
    s = Solution()
    print(s.twoSum3(nums, target))
