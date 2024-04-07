#Kth Largest Element 
import heapq

def findKthLargest(nums, k):
    for i in range(len(nums)):
        nums[i] = -nums[i]
    heapq.heapify(nums)
    
    for j in range(k):
        x = heapq.heappop(nums)
    return -x

#UNFINISHED, NEED TO DO QUICK SELECT SOLUTION

nums1 = [3,2,1,5,6,4]
nums2 = [3,2,3,1,2,4,5,5,6]
print(findKthLargest(nums1, 2))
print(findKthLargest(nums2, 4))