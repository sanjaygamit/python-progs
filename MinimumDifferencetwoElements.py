# Find Minimum Difference Between Two Elements in an Array

# arr = [5,32,45,4,12,18,25]

# Algorithm 
# 1. Sort the elements of the arrayt. 
# 2. Initialise the first defference value to be largest. Start comparing the difference of first elements with it. 
# 3. Compare elements with its adjacent element & keep track of minimum difference. 


# def minimum_difference(arr):
#     arr=sorted(arr)
#     size = len(arr)
#     min_diff = 9999*999

#     for i in range(size-1):
#         if(arr[i+1]-arr[i] < min_diff):
#             min_diff = arr[i+1] - arr[i]
#     return min_diff


arr = [5,32,45,4,12,18,25]
# print("Minimum difference between elements of an arry is", minimum_difference(arr))

# x = 3
# while x:
#     print(x)
#     x -=1

# def maximum_dif(arr):
#     arr = sorted(arr)
#     size=len(arr)
#     max_diff = -9999*999
#     for i in range(size-1):
#         if(arr[i+1] - arr[i]> max_diff):
#             max_diff = arr[i+1] - arr[i]
#     return max_diff

# print("Maximum difference between elements of an arry is", maximum_dif(arr))


