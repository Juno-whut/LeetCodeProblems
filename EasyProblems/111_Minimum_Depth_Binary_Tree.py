from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: TreeNode):
        if not root:
            return 0
        
        tree_queue = deque([root])
        currDepth = 0
        num_popped = 0
        num_in_layer = 1
        num_in_next_layer = 0
        while tree_queue:
            currNode = tree_queue.popleft()
            num_popped += 1
            if not currNode.left and not currNode.right:
                return currDepth+1
            
            if currNode.left:
                num_in_next_layer += 1
                tree_queue.append(currNode.left)   

            if currNode.right:
                num_in_next_layer += 1
                tree_queue.append(currNode.right)

            if nums_popped == num_in_layer:
                nums_popped = 0
                num_in_layer = num_in_next_layer
                num_in_next_layer = 0
                currDepth += 1
                

def main():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(Solution().minDepth(root))
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.left.right.right = TreeNode(4)
    root.left.right.right.right = TreeNode(5)
    root.right = TreeNode(3)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(5)
    root.right.right.right.right = TreeNode(6)
    print(Solution().minDepth(root))


if __name__ == "__main__":
    main()

