# -*- coding: utf-8 -*-
# @Time    : 2018/9/10 22:17
# @Author  : Hzhang
# @Email   : zyh_njust@hotmail.com
# @File    : lee006zig.py
# @Software: PyCharm
# 首先知道两个规律。
# 巧妙的地方就是每次去做减法， 这样就获得了interval–2*i,  2*i,  interval–2*i, 2*i, interval–2*i,

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <=1: return s
        ans =""
        interval = 2 * (numRows - 1)  #if num is 4, interval is 6
        for i in range(0, len(s), interval):
            ans +=s[i]
        for row in range(1, numRows-1):
            inter = 2 * row
            i = row
            while i < len(s):
                ans += s[i]
                # 每次都用interval 减去inter， 也就是说第一次是8-2*， 第二次就是2*， 第三次又是i-2*
                inter = interval - inter
                i += inter
        for i in range(numRows -1, len(s), interval):
            ans += s[i]
        print(ans)
        return ans

if __name__ == "__main__":
    Solution().convert("PAYPALISHIRING", 2) == "PYAIHRNAPLSIIG"
    Solution().convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
    Solution().convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"

