def merge(nums1, m, nums2, n):
    # Initialize pointers for nums1, nums2, and the merged array
    i = m - 1
    j = n - 1
    k = m + n - 1

    # Merge the arrays from right to left
    while i >= 0 and j >= 0:
        if nums1[i] <= nums2[j]:
            nums1[k] = nums2[j]
            j -= 1
        else:
            nums1[k] = nums1[i]
            i -= 1
        k -= 1

    # Copy the remaining elements from nums2 if any
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
merge(nums1, m, nums2, n)
print(nums1) 
