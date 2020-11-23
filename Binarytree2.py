################# Removing Leaf Node
def removeleaf(root):
  if root == None:
    return None
    
  if root.left == None and root.right == None:
    return None
    
  root.left = removeleaf(root.left)
  root.right = removeleaf(root.right)
  
  return root
  
###########mirror binary tree

  def mirrorBinaryTree(root) :
    
    if root == None:
        return None
    
    mirrorBinaryTree(root.left)
    mirrorBinaryTree(root.right) 
    
    tmp = root.left
    root.left = root.right
    root.right = tmp
    

########## Binary Tree Is Balanced

Time complexity O(n^2) and O(nlogn)
For every node it is checkinh height

def height(root):
  if root==None:
    return 0
   return 1 + max(height(root.left),height(root.right))
   
   
def isbalanced(root):
  if root==None:
    return True
    
  lt = height(root.left)
  rt = height(root.right)
  
  if lt-rt>1 or rt-lt>1:
    return False
  
  leftbalanced = isbalanced(root.left)
  rightbalanced = isbalanced(root.right)
  
  if leftbalanced and rightbalanced:
    return True
  else:
    return False
    
    --2------
def getheightBalanced(root):
  if root==None:
    return 0,True
  
  lt,leftbalanced = getheightBalanced(root.left)
  rt,rightbalanced = getheightBalanced(root.right)
  
  h = 1 + max(lh,rh)
  if lt-rt>1 or rt-lt>1:
    return h,False
  
  if leftbalanced and rightbalanced:
    return h,True
  else:
    return h,False
    
################### Diameter of Binary Tree

-------1-------------------
def diameterOfBinaryTree(root) :
    if root==None:
        return 0
    
    lheight = height(root.left)
    rheight = height(root.right)
    
    ldia = diameterOfBinaryTree(root.left)
    rdia = diameterOfBinaryTree(root.right) 
    
    return max(lheight+rheight+1,max(ldia,rdia))
    
def height(root):
    if root == None:
        return 0
    return 1 + max(height(root.left),height(root.right))

-----------2----------

def diameter_height(node):
    if node is None:
        return 0, 0
    ld, lh = diameter_height(node.left)
    rd, rh = diameter_height(node.right)
    return max(lh + rh + 1, ld, rd), 1 + max(lh, rh)



###########LevelSize print of node in tree
Print Levelwise

def printLevelWise(root):
    if root is None:
        return
    q=queue.Queue()
    q.put(root)
    while q.qsize()!=0:
        p=q.get()
        print(p.data,end=":")
        if p.left:
            print("L:{}".format(p.left.data),end=",")
            q.put(p.left)
        elif p.left is None:
            print("L:"+""+"-1",end=",")
        if p.right:
            print("R:{}".format(p.right.data),end="")
            q.put(p.right)
        elif p.right is None:
            print("R:"+""+"-1",end="")        
        print()

########################Construct Tree Using Inorder and Preorder

def buildTreePreOrder(preorder, inorder):
    if len(preorder) == 0:
        return None
        
        ##gind root
    rootData = preorder[0]
    root = BinaryTreeNode(rootData)
    i=0
    ## inorder
    while i < len(inorder) :
        if inorder[i] == rootData:
            leftin=inorder[0:i]
            rightin=inorder[i+1:]
        i += 1
    l= len(leftin)
    ##preorder
    Lpre= preorder[1:l+1]
    Rpre= preorder[l+1:]
    leftSub= buildTreePreOrder(Lpre,leftin)
    rightSub= buildTreePreOrder(Rpre,rightin)
    
    # connect 
    root.left=leftSub
    root.right=rightSub
    return root
 

################################### Construct Tree Using Inorder and postorder

def buildTree(postOrder, inOrder, n) :
    if len(postOrder) == 0 :
        return None
        
        ##Find root data
    rootdata = postOrder[-1]
    root = BinaryTreeNode(rootdata)
        ###Find location in inorder
    rootdataindex = -1
    for i in range(len(inOrder)):
        if inOrder[i] == rootdata:
            rootdataindex = i
            break
                
    if rootdataindex == -1:
        return None
        
        #Find inorder
    leftinorder = inOrder[:rootdataindex]
    rightinorder = inOrder[rootdataindex+1:]
        
    lengthleftinorder = len(leftinorder)
        
        #find postorder
    leftpostorder = postOrder[:lengthleftinorder]
    rightpostorder = postOrder[lengthleftinorder:-1]
        
    leftchild = buildTree(leftpostorder, leftinorder, n)
    rightchild = buildTree(rightpostorder, rightinorder, n)
        
    root.left = leftchild
    root.right = rightchild
        
    return root
        
################Create & Insert Duplicate Node

def insertDuplicateNode(root):
    if root  == None:
        return None
    
    addrleft = root.left
    
    data = root.data
    newnode = BinaryTreeNode(data)
    root.left = newnode
    
    newnode.left = addrleft
    insertDuplicateNode(newnode.left)
    insertDuplicateNode(root.right)


###########Minimum and Maximum in the Binary Tree


MIN_VALUE = -9999999999
MAX_VALUE = 9999999999

def getMinAndMax(root) :
    minimum,maximum=INT_MAX,INT_MIN
    if root ==None:
        return minimum,maximum
    leftmin,leftmax=getMinAndMax(root.left)
    rightmin,rightmax=getMinAndMax(root.right)
    minimum=min(root.data,leftmin,rightmin)
    maximum=max(root.data,leftmax,rightmax)
    return minimum,maximum



################ Level order traversal
def printLevelATNewLine(root):
    q = queue.Queue()
    if root == None:
        return None
    
    q.put(root)
    q.put(None)
    while not q.empty():
        p = q.get()
        if p == None:
            print()
            if q.empty():
                break
            q.put(None)
        else:
            print(p.data , end = " ")
            if p.left != None:
                q.put(p.left)
            if p.right != None:
                q.put(p.right)


########### Path Sum Root to Leaf
def rootToLeafPathsSumToK(root, k, lst):
    if root is None:
        return None
    if root.left is None and root.right is None:
        if root.data==k:
            print(*lst,k)
    lst.append(root.data)
    rootToLeafPathsSumToK(root.left,k-root.data,lst)
    rootToLeafPathsSumToK(root.right,k-root.data,lst)
    lst.pop()
         
  
  ##########has sum or not
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root == None:
            return False
        
        if root.left is None and root.right is None:
            if root.val==sum:
                return True
        
        left = self.hasPathSum(root.left,sum-root.val)
        right = self.hasPathSum(root.right,sum-root.val)
        
        if left or right:
            return True
        else:
            return False
                
  
######### Print nodes at distance k from node  
  
def nodesAtDistanceKHelper(root, target, k) :
    if root is None :
        return -1
    if root.data == target :
        nodesAtDistanceKDown(root, k)
        return 0

    leftD = nodesAtDistanceKHelper(root.left, target, k)
    if leftD != -1 :
        if (leftD + 1) == k :
            print(root.data)
        else :
            nodesAtDistanceKDown(root.right, k - leftD - 2)
        return 1 + leftD

    rightD = nodesAtDistanceKHelper(root.right, target, k);
    if rightD != -1 :
        if (rightD + 1) == k :
            print(root.data)
        else :
            nodesAtDistanceKDown(root.left, k - rightD - 2)
        return 1 + rightD
    return -1

def nodesAtDistanceKDown(root, k) :
    if root is None : 
        return
    if k == 0 :
        print(root.data)
        return
    nodesAtDistanceKDown(root.left, k - 1)
    nodesAtDistanceKDown(root.right, k - 1)

def nodesAtDistanceK(root, node, k) :
    nodesAtDistanceKHelper(root, node, k)



################## Identical tree

def identicalTrees(a, b): 
      
    # 1. Both empty 
    if a is None and b is None: 
        return True 
  
    # 2. Both non-empty -> Compare them 
    if a is not None and b is not None: 
        return ((a.data == b.data) and 
                identicalTrees(a.left, b.left)and
                identicalTrees(a.right, b.right)) 
      
    # 3. one empty, one not -- false 
    return False
    
    
    
    
    
    
def printLevelWiseTree(tree):
    q1=queue.Queue()
    q2=queue.Queue()
    q1.put(tree)
    while not q1.empty():
        while not q1.empty():
            parent=q1.get()
            print(parent.data,end=':')
            for i in range(len(parent.children)):
                if i==len(parent.children)-1:
                    print(parent.children[i],end='')
                else:
                    print(parent.children[i],end=',')
                q2.put(parent.children[i])
            print()
        q1,q2=q2,q1