def func(list1):
    list1[:] = [1, 2]  # correct
    # list1 = [1, 2]   # wrong


if __name__ == "__main__":
    test = [1, 2, 3]
    func(test)
    print(test)
