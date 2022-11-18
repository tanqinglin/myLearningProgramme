# -*- coding: utf-8 -*-

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        l1 = len(nums1)
        l2 = len(nums2)
        if (l1 + l2) % 2 == 1:
            return self.deleteKNums(nums1, nums2, (l1 + l2) // 2)
        else:
            return float(self.deleteKNums(nums1, nums2, (l1 + l2) // 2 - 1) + self.deleteKNums(nums1, nums2, (l1 + l2) // 2)) / 2
            
    def deleteKNums(self, L1, L2, k):

        if L1 == []:
            return L2[k]
        if L2 == []:
            return L1[k]

        l1 = len(L1) // 2
        l2 = len(L2) // 2
        m1 = L1[l1]
        m2 = L2[l2]
        if l1 + l2 < k:
            if m1 < m2:
                return self.deleteKNums(L1[l1+1:], L2, k - l1 - 1)
            else:
                return self.deleteKNums(L1, L2[l2+1:], k - l2 - 1)
        else:
            if m1 > m2:
                return self.deleteKNums(L1[:l1], L2, k)
            else:
                return self.deleteKNums(L1, L2[:l2], k)

if __name__ == '__main__':
    nums1 = [1,2,2]
    nums2 = [1,2,3]
    Test = Solution()
    print(Test.findMedianSortedArrays(nums1, nums2))