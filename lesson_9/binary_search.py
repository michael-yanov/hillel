def binary_search(lst, key_value, left=0, right=None):
    if right is None:
        right = len(lst)

    middle = (left + right) // 2
    while lst[middle] != key_value and left <= right:
        if lst[middle] < key_value:
            left = middle + 1
        else:
            right = middle - 1

    middle = (left + right) // 2

    return (True, middle) if not left > right else (False, middle + 1)


l = [6, 9, 25, 32, 41, 48, 58, 60, 65, 67, 70, 75, 75, 89, 90, 92, 95, 98, 100, 100]
print(binary_search(l, 54, 0))
