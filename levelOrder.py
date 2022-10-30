from collections import deque
 
class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None
 
# /* Function to print level order of
#    given binary tree. Direction of printing
#    level order traversal of binary tree changes
#    after every two levels */
def modifiedLevelOrder(node):
   
    # For null root
    if (node == None):
        return
 
    if (node.left == None and node.right == None):
        print(node.data, end = " ")
        return
 
    # Maintain a queue for normal
    # level order traversal
    myQueue = deque()
 
    # /* Maintain a stack for printing nodes in reverse
    #    order after they are popped out from queue.*/
    myStack = []
 
    temp = None
 
    # sz is used for storing the count
    # of nodes in a level
    sz = 0
 
    # Used for changing the direction
    # of level order traversal
    ct = 0
 
    # Used for changing the direction
    # of level order traversal
    rightToLeft = False
 
    # Push root node to the queue
    myQueue.append(node)
  
    # Run this while loop till queue got empty
    while (len(myQueue) > 0):
        ct += 1
 
        sz = len(myQueue)
 
        # Do a normal level order traversal
        for i in range(sz):
            temp = myQueue.popleft()
 
            # /*For printing nodes from left to right,
            # simply print nodes in the order in which
            # they are being popped out from the queue.*/
            if (rightToLeft == False):
                print(temp.data,end=" ")
 
            # /* For printing nodes
            # from right to left,
            # push the nodes to stack
            # instead of printing them.*/
            else:
                myStack.append(temp)
 
            if (temp.left):
                myQueue.append(temp.left)
 
            if (temp.right):
                myQueue.append(temp.right)
 
        if (rightToLeft == True):
 
            # for printing the nodes in order
            # from right to left
            while (len(myStack) > 0):
                temp = myStack[-1]
                del myStack[-1]
 
                print(temp.data, end = " ")
 
        # /*Change the direction of printing
        # nodes after every two levels.*/
        if (ct == 2):
            rightToLeft = not rightToLeft
            ct = 0
 
        print()
 
# Driver program to test above functions
if __name__ == '__main__':
   
    # Let us create binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.left.left = Node(8)
    root.left.left.right = Node(9)
    root.left.right.left = Node(3)
    root.left.right.right = Node(1)
    root.right.left.left = Node(4)
    root.right.left.right = Node(2)
    root.right.right.left = Node(7)
    root.right.right.right = Node(2)
    root.left.right.left.left = Node(16)
    root.left.right.left.right = Node(17)
    root.right.left.right.left = Node(18)
    root.right.right.left.right = Node(19)
 
    modifiedLevelOrder(root)
