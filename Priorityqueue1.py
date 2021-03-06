Complete binary tree -- 
1 All level should be completely filled except the last level
2 First left child then right child be inserted  ie left tp right insertion

Removal = 
Removal from right to left child and last level to top

Height = log(n)

Heap is Complete binary tree (2 child) and heap order property
min heap - parent value must be less than child value  ie minimum valaue at top
(no concept of bst less than greater thanP)
max head - parent priority value higher than child value  ie maximum value at top


Insert at last and then make changes

Deletion min
1 delete 1 node and replace with last element and then adjust the tree

      10
   20    30
  40 50 60  70
80

next insert beside 80 as chikd oof 40
next insert beside 40 as chikd oof 50

array for heap 10 20 30 40 50 60 70 80
                0 1   2  3  4  5  6  7
                
                anyones child of parent  -  2*i+1,2*i+2  --i--> index of parent 
                


Code : Remove Min
Send Feedback
Implement the function RemoveMin for the min priority queue class.
For a minimum priority queue, write the function for removing the minimum element present. Remove and return the minimum element.
Note : main function is given for your reference which we are using internally to test the code.


class PriorityQueueNode:
    def __init__(self,ele,priority):
        self.ele = ele
        self.priority = priority
        
class PriorityQueue:
    def __init__(self):
        self.pq = []
    
    def isEmpty(self):
        return self.getSize() == 0
    
    def getSize(self):
        return len(self.pq)

    def getMin(self):
        if self.isEmpty():
            return None
        return self.pq[0].ele
    
    def __percolateUp(self):
        childIndex = self.getSize() - 1
        while childIndex > 0:
            parentIndex = (childIndex-1)//2
            
            if self.pq[parentIndex].priority > self.pq[childIndex].priority:
                self.pq[parentIndex],self.pq[childIndex] = self.pq[childIndex],self.pq[parentIndex]
                childIndex = parentIndex
            else:
                break
            
    def insert(self,ele,priority):
        pqNode = PriorityQueueNode(ele,priority)
        self.pq.append(pqNode)
        self.__percolateUp()
        
    def __percolateDown(self):
        
        parentIndex = 0
        childIndexleft = 2*parentIndex+1
        childIndexright = 2*parentIndex+2
            
        while childIndexleft < self.getSize() :
            minIndex = parentIndex
            if self.pq[minIndex].priority > self.pq[childIndexleft].priority:
                minIndex = childIndexleft
            if childIndexright< self.getSize() and self.pq[minIndex].priority > self.pq[childIndexright].priority:
                minIndex = childIndexright
                
            if  minIndex == parentIndex:
                break
            self.pq[parentIndex],self.pq[minIndex] = self.pq[minIndex],self.pq[parentIndex]
            parentIndex = minIndex
            childIndexleft = 2*parentIndex+1
            childIndexright = 2*parentIndex+2
        
        
    def removeMin(self):
        #Implment This Function Here
        if self.isEmpty():
            return None
        ele = self.pq[0].ele
        lastIndex = self.getSize() - 1
        self.pq[0] = self.pq[lastIndex]
        self.pq.pop()         
        self.__percolateDown()
        return ele
myPq = PriorityQueue()
curr_input = [int(ele) for ele in input().split()]
choice = curr_input[0]
i=1
while choice != -1:
    if choice == 1:
        element = curr_input[i]
        i+=1
        myPq.insert(element,element)
    elif choice == 2:
        print(myPq.getMin())
    elif choice == 3:
        print(myPq.removeMin())
    elif choice == 4:
        print(myPq.getSize())
    elif choice == 5:
        if myPq.isEmpty():
            print('true')
        else:
            print('false')
        break
    else:
        pass
    choice = curr_input[i]
    i+=1
        
    
    
Code : Max Priority Queue
Send Feedback
Implement the class for Max Priority Queue which includes following functions -
1. getSize -
Return the size of priority queue i.e. number of elements present in the priority queue.
2. isEmpty -
Check if priority queue is empty or not. Return true or false accordingly.
3. insert -
Given an element, insert that element in the priority queue at the correct position.
4. getMax -
Return the maximum element present in the priority queue without deleting. Return -Infinity if priority queue is empty.
5. removeMax -
Delete and return the maximum element present in the priority queue. Return -Infinity if priority queue is empty.
Note : main function is given for your reference which we are using internally to test the class.

class PriorityNode:
    def __init__(self,element,pri):
        self.element = element
        self.pri = pri

class PriorityQueue:    
    def __init__(self):
        self.pq = []
    
    def isEmpty(self):
        return self.getSize() == 0
        
    def getSize(self):
        return len(self.pq)

    def getMax(self):
        if self.isEmpty():
            return None
        return self.pq[0].element
        
    def __percolateUp(self):
        childIndex = self.getSize() - 1
        while childIndex > 0:
            parentIndex = (childIndex-1) // 2
            if self.pq[parentIndex].pri < self.pq[childIndex].pri:
                self.pq[parentIndex],self.pq[childIndex] = self.pq[childIndex],self.pq[parentIndex]
                childIndex = parentIndex
            else:
                break
                
    def __percolateDown(self):
        parentIndex=0
        leftChildIndex = 2*parentIndex + 1
        rightChildIndex = 2*parentIndex +2
        
        while leftChildIndex < self.getSize()-1:
            minIndex = parentIndex
            if self.pq[minIndex].pri < self.pq[leftChildIndex].pri:
                minIndex = leftChildIndex
            if self.pq[minIndex].pri < self.pq[rightChildIndex].pri:
                minIndex = rightChildIndex
            if minIndex == parentIndex:
                break
            self.pq[parentIndex],self.pq[minIndex] = self.pq[minIndex],self.pq[parentIndex]
            
            parentIndex = minIndex
            leftChildIndex = 2*parentIndex + 1
            rightChildIndex = 2*parentIndex +2
    def insert(self,element,pri):
        pqNode = PriorityNode(element,pri)
        self.pq.append(pqNode)
        self.__percolateUp()
        

    def removeMax(self):
        
        if self.isEmpty():
            return None
        element = self.pq[0].element
        self.pq[0] = self.pq[self.getSize()-1]
        self.pq.pop()
        self.__percolateDown()
        return element
    
            
    
        
myPq = PriorityQueue()
curr_input = [int(element) for element in input().split()]
choice = curr_input[0]
i=1
while choice != -1:
    if choice == 1:
        element = curr_input[i]
        i+=1
        myPq.insert(element,element)
    elif choice == 2:
        print(myPq.getMax())
    elif choice == 3:
        print(myPq.removeMax())
    elif choice == 4:
        print(myPq.getSize())
    elif choice == 5:
        if myPq.isEmpty():
            print('true')
        else:
            print('false')
        break
    else:
        pass
    choice = curr_input[i]
    i+=1    

    
