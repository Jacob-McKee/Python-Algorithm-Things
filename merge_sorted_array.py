class Solution(object):
    def merge(self, nums1, m, nums2, n):
        # The efficient way to do it
        i = m - 1
        j = n - 1
        k = m + n - 1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # The easier way I did it first, which, was still fairly efficient
        for i in range(n):
            nums1[m+i] = nums2[i]
        
        nums1.sort()
        