class Solution(object):
    def sumThree(self, nums, target):
        gap=abs(nums[0]+nums[1]+nums[2]-target)
        result=[]
        for index, a in enumerate(nums):
            left = index + 1
            right=len(nums)-1
            while left< right:
                b= nums[left]
                c= nums[right]
                total = a+b+c
                if total< target:
                    tmp = abs(total - target)
                    if gap >tmp:
                        gap = tmp
                        result=[a, b, c]
                    left+=1
                elif total > target:
                    tmp = abs(total - target)
                    if gap >tmp:
                        gap = tmp
                        result = [a, b, c]
                    right-=1;
                else:
                    return 0, [a,b,c]
        return gap, result

if __name__ == '__main__':
    sol = Solution()
    nums=[-1, 0, -3, 9, -2, 1, 2]
    target=4
    gap, result = sol.sumThree(nums, target)
    print("the minumun gap is {}, three numbers are: {} ".format(gap, result))



