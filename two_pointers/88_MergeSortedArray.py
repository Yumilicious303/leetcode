#Merge Sorted Array
def merge(nums1, m, nums2, n):
    i1, i2, insert = m - 1, n - 1, len(nums1) - 1
    while i1 >= 0 and i2 >= 0:
        if nums1[i1] >= nums2[i2]:
            nums1[insert] = nums1[i1]
            i1 -= 1
        else:
            nums1[insert] = nums2[i2]
            i2 -= 1
        insert -= 1
    
    while i2 >= 0:
        nums1[insert] = nums2[i2]
        insert -= 1
        i2 -= 1
    
    return nums1








print(merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))
print(merge(nums1 = [1], m = 1, nums2 = [], n = 0))
print(merge(nums1 = [0], m = 0, nums2 = [1], n = 1))
print(merge(nums1 = [4, 0, 0, 0, 0, 0], m = 1, nums2 = [1, 2, 3, 5, 6], n = 5))
        

