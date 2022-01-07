# Remove the duplicates from a list of integers,
# keeping the last ( rightmost ) occurrence of each element.
#
# Example:
# For input: [3, 4, 4, 3, 6, 3]
#
# remove the 3 at index 0
# remove the 4 at index 1
# remove the 3 at index 3
# Expected output: [4, 6, 3]

def solve(arr):
    newlist = []
    for i in arr[::-1]:
        if i not in newlist:
            newlist.append(i)
    print(newlist[::-1])




solve([3, 4, 4, 3, 6, 3])  #, [4, 6, 3])
solve([1, 2, 1, 2, 1, 2, 3])#, [1, 2, 3])
solve([1, 2, 3, 4])#, [1, 2, 3, 4])
solve([1, 1, 4, 5, 1, 2, 1])#, [4,5,2,1])