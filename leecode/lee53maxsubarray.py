# -*- coding: utf-8 -*-
# @Time    : 2018/9/2 19:14
# @Author  : Hzhang
# @Email   : zyh_njust@hotmail.com
# @File    : lee53maxsubarray.py
# @Software: PyCharm

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        这个有个动态规划的意思， 就是说不是说一个之第五个， 需要 b把前面从0 4 都加到5然后拿到结果。 而不是用current 来代表前面的这个值， 然后呢如果是负的干脆置为零。 就是说不加他， 这样就是总是最好的前面的值加上这个值。
        """
        if not nums:
            return 0

        current = nums[0]
        m = current
        length = len(nums)
        for i in range(1, length):
            if current < 0:
                current = 0
            current += nums[i]
            m = max(current, m)
        print(m)
        return m
    # def maxSubArray(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     if not nums:
    #         return 0
    #     length = len(nums)
    #     current = nums[0]
    #     m = current
    #     for i in range(1, length):
    #         if current < 0:
    #             current = 0
    #         current += nums[i]
    #         print(current)
    #         m = max(current, m)
    #         print("m: %d" % m)
    #     print(m)
    #     return m
if __name__ == "__main__":
    assert Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

