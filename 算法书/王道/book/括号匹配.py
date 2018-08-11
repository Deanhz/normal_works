'''
2018.3.10
wangdao P84

包括圆括号、方括号、花括号，判断表达式中的括号是否匹配。
'''


class Stack(object):
    data = []


class Solution(object):
    def bracketMatch(buf):
        S = Stack()
        left_brackets = ["[", "(", "{"]
        right_brackets = ["]", ")", "}"]
        dic = {"]": "[", ")": "(", "}": "{"}

        if len(buf) == 0:
            return True
        for c in buf:
            if c in left_brackets:
                S.data.append(c)
            elif c in right_brackets:
                if len(S.data) == 0:
                    return False
                top_bracket = S.data.pop()
                if top_bracket != dic[c]:
                    print(1)
                    return False
            else:
                return False

        if len(S.data) == 0:
            return True
        else:
            return False


if __name__ == "__main__":
    test1 = ["(", "[", "{", "}", "]", ")"]
    test2 = ["(", "[", "{", "}", "]", ")", "}"]
    test_data = [test1, test2]
    for test in test_data:
        print(Solution.bracketMatch(test))
