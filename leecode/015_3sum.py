class Solution(object):
    def threeSum(self, nums):
        result=[] #learn
        nums.sort();
        for index, a in enumerate(nums):
            if index >=1 and nums[index-1] ==a:
                continue  # 就是说如果重复值， 直接拿下
            left = index+1
            right = len(nums) - 1
            while left < right:
                b = nums[left]
                c=nums[right]
                total = a + b + c
                # if(total <= 0):  # this will fail
                if(total < 0):
                    left+=1 #learn
                elif(total > 0):
                    right-=1
                else:
                    result.append([a, b, c])
                    while(left<right and nums[left]== nums[left+1]):
                        left +=1
                    # while(left< right and nums[right] == nums[right-1]):
                    while left < right and nums[right] == nums[right - 1]:
                        right-=1
                    left+=1
                    right-=1
        return result

if __name__ == '__main__':
    sol = Solution()
    print(sol.threeSum([-1,0,-2,1,2,-1,-4]))

