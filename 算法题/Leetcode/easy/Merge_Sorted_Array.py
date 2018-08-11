'''
2017.10.30
88. easy
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
The number of elements initialized in nums1 and nums2 are m and n respectively.
'''


class Solution(object):
    def merge(self, nums1, m, nums2, n):  # by me
        '''
        :type nums1: List[n]
        :type m: int
        :type nums2: List[n]
        :type n: int
        :rtype: void, Do not return anything,modify nums1 in-place instead
        '''
        if m == 0:
            nums1[:] = nums2[:n]
        buf = []
        i = j = 0
        while(i < m and j < n):
            if(nums1[i] <= nums2[j]):
                buf.append(nums1[i])
                i += 1
            else:
                buf.append(nums2[j])
                j += 1
        if(i < m):
            buf.extend(nums1[i:m])
        elif(j < n):
            buf.extend(nums2[j:n])
        nums1[:] = buf

    def merge2(self, nums1, m, nums2, n):  # by me
        if m == 0:
            nums1[:] = nums2[:n]
        i = j = 0
        while(i < m and j < n):
            if(nums2[j] < nums1[i]):
                nums1.insert(i, nums2[j])
                m = m + 1
                j = j + 1
            i = i + 1
        if (i < m):
            nums1[:] = nums1[:m]
        elif(j < n):
            nums1[:] = nums1[:m] + nums2[j:n]


if __name__ == '__main__':
    nums1 = [1, ]
    nums2 = []
    m = len(nums1)
    n = len(nums2)
    Solution().merge2(nums1, 1, nums2, 0)
    print(nums1)
