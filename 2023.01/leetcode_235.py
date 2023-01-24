# leetCode 235. Lowest Common Ancestor of a Binary Search Tree

# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def lowestCommonAncestor(root, p, q):
    parent_p = root.index(p)
    parent_q = root.index(q)
    # print(parent_p, parent_q)
    while parent_p >= 0 and parent_q >= 0:
        # print('p', parent_p, 'q', parent_q)
        if parent_p > parent_q:
            while parent_p > 0 and parent_p != parent_q:
                # print('p', parent_p)
                parent_p = (parent_p - 1) // 2
        elif parent_p < parent_q:
            while parent_q > 0 and parent_p != parent_q:
                # print('q', parent_q)
                parent_q = (parent_q - 1) // 2
        else:
            return root[parent_p]


print(lowestCommonAncestor([6,2,8,0,4,7,9,None,None,3,5], 2, 8))    # 6
print(lowestCommonAncestor([6,2,8,0,4,7,9,None,None,3,5], 2, 4))    # 2
print(lowestCommonAncestor([2, 1], 2, 1))    # 2
