'''
2018.3.19
'''


def getMaxWindow(arr, w):
    if not arr or w < 1 or len(arr) < w:
        return
    N = len(arr)
    result = []
    for i in range(N - w + 1):
        tmp = arr[i:i + w]
        _max = max(tmp)
        result.append(_max)
    return result


if __name__ == "__main__":
    test = [4, 3, 5, 4, 3, 3, 6, 7]
    print(getMaxWindow(test, w=3))
