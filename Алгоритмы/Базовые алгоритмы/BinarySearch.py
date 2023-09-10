any_array = [6,8,9,2,5,1,4,7,3]
def BinarySeach(arr: list, value: int) -> int:
    arr = sorted(arr)
    first = 0
    last = arr[len(arr) - 1]
    index = -1
    
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if arr[mid] == value:
          index = mid
          return index
        if arr[mid] < value:
          first = mid + 1
        else:
          last = mid - 1

x = BinarySeach(any_array, 4)
print(sorted(any_array)[x])
