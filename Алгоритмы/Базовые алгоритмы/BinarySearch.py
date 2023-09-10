def BinarySeach(arr: list, value: int) -> int:
  first = 0
  last = arr[len(value)]-1
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
