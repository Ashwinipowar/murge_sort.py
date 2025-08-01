# nums=[3,1,2,4,6,7,3,5,8]
# def merge_sort(arr):
#     if len(arr)<=1:
#         return arr    
#     mid=len(arr)//2
#     left_half=arr[ :mid]
#     right_half=arr[mid: ]
#     left_half = merge_sort(left_half)
#     right_half = merge_sort(right_half)
#     return merge_array(left_half, right_half)
    
# def merge_array(left,right):
#     result=[]
#     i,j=0, 0
#     n, m =len(left), len(right)


#     while i < n and j < m:
#         if left[i]<=right[j]:
#             result.append(left[i])
#             i+=1
#         else:
#             result.append(right[j])
#             j+=1

#     if i < n:
#         while i < n:
#             result.append(left[i])
#             i+=1
#     if j < m:
#         while j < m:
#             result.append(right[j])
#             j+= 1

#             return result
        
# sorted_nums = merge_sort(nums)
# print(sorted_nums)
# this is my code but having some erroe in it( from youtube)



nums = [3, 1, 2, 4, 6, 7, 3, 5, 8]

def merge_sort(arr):
    if len(arr) <= 1:
        return arr    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    return merge_array(left_half, right_half)

def merge_array(left, right):
    result = []
    i, j = 0, 0
    n, m = len(left), len(right)  # ✅ FIXED

    while i < n and j < m:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < n:
        result.append(left[i])
        i += 1

    while j < m:
        result.append(right[j])
        j += 1

    return result   # ✅ Make sure it's at the correct indentation

sorted_nums = merge_sort(nums)
print(sorted_nums)

