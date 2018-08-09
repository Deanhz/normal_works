'''
2018.3.19
'''


def findLeft_rigt_firstBig(data):
    lbigMap = {}
    rbigMap = {}
    stack = []
    length = len(data)
    for i in range(length):
        while(stack and data[stack[-1]] < data[i]):
            stack.pop()
        if stack:
            lbigMap[i] = stack[-1]
        stack.append(i)

    while stack:
        stack.pop()

    for i in range(length)[::-1]:
        while(stack and data[stack[-1]] < data[i]):
            stack.pop()
        if stack:
            rbigMap[i] = stack[-1]
        stack.append(i)
    return lbigMap, rbigMap


if __name__ == "__main__":
    data = [3, 4, 5, 1, 2]
    l, r = findLeft_rigt_firstBig(data)
    print(l, r)
