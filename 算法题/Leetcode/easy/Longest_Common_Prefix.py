'''
2017.9.14
14.
Write a function to find the longest common prefix string amongst an array of strings.
'''

class Solution(object):
    def longestCommonPrefix(self, strs):  # by me
        '''
        :type strs: List[str]
        :rtype: str
        '''
        if len(strs) == 0:
            return ''
        shortest_len = len(strs[0])
        shortest_str = strs[0]
        prefix = ''
        for s in strs:
            L = len(s)
            if L <= shortest_len:
                shortest_len = L
                shortest_str = s
        prefix_list = []
        for i in range(1, shortest_len + 1):
            tmp = shortest_str[0:i]
            prefix_list.append(tmp)
        flag = True
        for p in prefix_list:
            for s in strs:
                if s.find(p) != 0:
                    flag = False
                    break
            if flag:
                prefix = p
        return prefix

    def longestCommonPrefix2(self, strs):
        prefix = ''
        if not strs:
            return prefix
        len_min = min([len(s) for s in strs])
        for i in range(len_min):
            chars = [s[i] for s in strs]
            if max(chars) is min(chars):
                prefix = prefix + strs[0][i]
            else:
                return prefix
        return prefix


if __name__ == "__main__":
    strs = ["abc", "ab", "abcd", "abcde"]
    print(Solution().longestCommonPrefix(strs))
