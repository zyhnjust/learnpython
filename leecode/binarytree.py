# -*- coding: utf-8 -*-
# @Time    : 2018/8/26 21:37
# @Author  : Hzhang
# @Email   : zyh_njust@hotmail.com
# @File    : binarytree.py
# @Software: PyCharm

class node(object):
    def __init__(self, data=None, left=None, right=None):
        self.data=data
        self.left= left
        self.right= right

def pre_order(tree):
    if tree == None:
        return
    print(tree.data)
    pre_order(tree.left)
    pre_order(tree.right)

def in_order(tree):
    if tree == None:
        return
    in_order(tree.left)
    print(tree.data)
    in_order(tree.right)

def post_order(tree):
    if tree == None:
        return
    post_order(tree.left)
    post_order(tree.right)
    print(tree.data)

def pre_order_norecur(tree):
    if tree==None:
        return
    stack=[tree]
    while stack:
        node=stack.pop()
        print(node.data)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

# 中序
def in_order_nonrecur(tree):
    if tree == None:
        return
    stack=[]
    node = tree
    while stack or node:
        while node:
            stack.append(node)
            node=node.left
        node=stack.pop()
        print(node.data)
        node=node.right

#后序
def post_order_nonrecur(tree):
    stack1 = [tree]
    stack2 = []
    while len(stack1) >0:
        node = stack1.pop()
        stack2.append(node)
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
    while len(stack2) > 0:
        node = stack2.pop()
        print(node.data)

if __name__ == '__main__':
    tree=node('D', node('B', node('A'), node('C')), node('E', right=node('G', node('F'))))
    print("pre oder")
    #DBACEGF
    pre_order(tree)
    print("pre oder")
    pre_order_norecur(tree)

    print("inorder")
    in_order(tree)
    print("inorder not recur")
    in_order_nonrecur(tree)

    print("postorder")
    post_order(tree)
    print("postorder not recur")
    post_order_nonrecur(tree)
