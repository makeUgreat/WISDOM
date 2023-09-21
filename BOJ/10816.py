def BS(target,arr):
    start = 0
    end = len(arr)-1

    while start <= end:
        mid = (start+end) // 2
        mid_v = arr[mid]

        if target == mid_v:
            return 1

        if target < mid_v:
            end = mid-1

        if target > mid_v:
            start = mid+1


    return 0
