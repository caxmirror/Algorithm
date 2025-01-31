# time: n
# space: 1
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pointer1 = m - 1
        pointer2 = n - 1
        while pointer2 >= 0:
            if pointer1 < 0 or nums2[pointer2] >= nums1[pointer1]:
                nums1[pointer1 + pointer2 + 1] = nums2[pointer2]
                pointer2 -= 1
            else:
                nums1[pointer1 + pointer2 + 1] = nums1[pointer1]
                pointer1 -= 1
            