# -*- coding: utf-8 -*-
# @Time    : 2018/8/26 20:20
# @Author  : Hzhang
# @Email   : zyh_njust@hotmail.com
# @File    : treepre.py
# @Software: PyCharm
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # stack=[]
        # result=[]
        # while root or stack:
        #     if not root:
        #         root=stack.pop()
        #     result.append(root.val)
        #     if root.right:
        #         stack.append(root.right)
        #     root = root.left

        if not root:
            return []

        ret = []
        stack = [root]

        while stack:
            node = stack.pop()
            ret.append( node.val )

            if node.right:
                stack.append( node.right )
            if node.left:
                stack.append( node.left )

        return ret


if __name__ == '__main__':



