# 이진 탐색 by recursion

def binary_search_by_recursion(array, target, start,end):
    if start > end:
        return None
    mid = (start + end) // 2

    if array[mid] == target:
        return mid

    elif array[mid] > target:
        return binary_search_by_recursion(array, target, start, mid-1)
    else:
        return binary_search_by_recursion(array, target, mid+1, end)


# 이진 탐색 by loop
def binary_search_by_loop(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
        return None

# 1 5 6 7 8 10 12 15
#