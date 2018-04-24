'''
BinarySearch
search a given key's index from a sorted list
'''
def bs(key, l):
    left, right = 0, len(l)
    while left <= right:
        mid = (left + right) // 2
        if key == l[mid]:
            return mid
        elif key > l[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1

l1 = [1,2,3,7,8,9,10,5]
l1.sort()
print("sorted list is", l1)
try:
    key = int(input("enter an integer you want to find:\n"))
except:
    key = int(input("please enter a nonnegative integer:\n"))


result1 = bs(key, l1)
if result1 != -1:
    print("the index of", key, "is", result1)
else:
    print("cannot find the integer you want")