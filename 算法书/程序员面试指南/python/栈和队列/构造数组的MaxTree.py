'''
2048.3.19
'''

'''
warning:
0 == False
'''


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


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


def getMaxTree(arr):
    lbigMap, rbigMap = findLeft_rigt_firstBig(arr)
    nArr = [Node(value) for value in arr]
    parents = []
    head = None
    for i in range(len(arr)):
        curNode = nArr[i]
        left = lbigMap.get(i)
        right = rbigMap.get(i)
        if left is not None:
            lNode = nArr[left]
        if right is not None:
            rNode = nArr[right]

        if left is None and right is None:
            head = curNode
            parents.append(-1)
        elif left is None:
            parents.append(right)
            if not rNode.left:
                rNode.left = curNode
            else:
                rNode.right = curNode
        elif right is None:
            parents.append(left)
            if not lNode.left:
                lNode.left = curNode
            else:
                lNode.right = curNode
        else:
            if lNode.value < rNode.value:
                parentId = left
                parentNode = lNode
            else:
                parentId = right
                parentNode = rNode
            parents.append(parentId)
            if not parentNode.left:
                parentNode.left = curNode
            else:
                parentNode.right = curNode
    return head, parents


if __name__ == "__main__":
    data = [3, 1, 4, 2]
    tree, parents = getMaxTree(data)
    print(parents)
