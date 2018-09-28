class Solution(object):
    def reverse(self, x):

        flag=-1
        if x>0:
            flag=1
        else:
            flag = -1
        x=x*flag
        print(x)
        result = 0
        # while x>0:
        while x:
            # result = result * 10+ x%10
            # x=x/10
            result = result * 10 + x % 10
            x /= 10
        if result>2147483647:
            print(result)
            return 0
        else:
            print(result)
            return result*flag

    def atoi(self, str):
        str = str.lstrip()
        if not str: return 0
        for i in range(len(str)):
            if not ('0' <= str[i] <= '9' or str[i] in ('+', '-')):
                str = str[:i:]
                break
        try:
            f = 1
            intx = int(str)
            if intx >= 2147483647:
                intx = 2147483647
            elif intx <= -2147483648:
                intx = -2147483648
            return intx
        except:
            return 0


if __name__ == "__main__":
    # assert Solution().atoi(321000) == 123
    # assert Solution().atoi(-321) == -123
    # assert Solution().atoi(1534236469) == 0

    assert Solution().reverse(321000) == 123
    assert Solution().reverse(-321) == -123
    assert Solution().reverse(1534236469) == 0
