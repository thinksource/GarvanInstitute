    def getHeight(self,root):
        #Write your code here
        right_height=0
        left_height=0
        if root.left!=None:
            left_height=self.getHeight(root.left)+1
        if root.right!=None:
            right_height=self.getHeight(root.right)+1
        return max(right_height, left_height)
