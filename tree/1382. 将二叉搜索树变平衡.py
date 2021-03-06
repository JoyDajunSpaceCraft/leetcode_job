# 1382. 将二叉搜索树变平衡
# 给你一棵二叉搜索树，请你返回一棵 平衡后 的二叉搜索树，新生成的树应该与原来的树有着相同的节点值。

# 如果一棵二叉搜索树中，每个节点的两棵子树高度差不超过 1 ，我们就称这棵二叉搜索树是 平衡的 。

# 如果有多种构造方法，请你返回任意一种。
# 示例：
# 输入：root = [1,null,2,null,3,null,4,null,null]
# 输出：[2,1,3,null,null,null,4]
# 解释：这不是唯一的正确答案，[3,1,4,null,2,null,null] 也是一个可行的构造方案。
# 提示：
# 树节点的数目在 1 到 10^4 之间。
# 树节点的值互不相同，且在 1 到 10^5 之间。

# 将二叉树 读入列表 列表中元素 按照排列
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        l = inorder(root)

        def generator(l):
            if not l:
                return None
            mid = len(l) // 2 # 地板除获得整数
            root = TreeNode(l[mid])
            root.left = generator(l[:mid])
            root.right = generator(l[mid + 1:])
            
            return root
        return generator(l)
