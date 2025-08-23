'''
Title: EECS 348 Assignment 1
Description: CEO Email prioritization program
Input(s): Assignment1_Test_Files.txt
Output(s): Next email and number of unread emails
All collaborators: Geeks for geeks, ChatGPT
Author's name: Edbert Jensen
Creation Date: 8/22/2025
'''

'''
Sources for the MaxHeap: https://www.geeksforgeeks.org/dsa/introduction-to-max-heap-data-structure/

'''
class MaxHeap:
    def __init__(self):
        self.arr = []       # initialize an empty list when MaxHeap object is created
    
    # i should just be a variable that is the position or index the newly inserted node.
    # this fix was with the help of chatGPT. I initially had i initialize with creation and realized that i was just suppose to be a temp variable.
    def heapify_up(self, i):    
        # the definition of the parent property of Binary Heaps is (index - 1) floor division by 2
        parent = (i - 1) // 2   

        # A condition that checks if the parent is positie and whatever index i is bigger than the parent value
        if parent >= 0 and self.arr[i] > self.arr[parent]:       
            self.arr[i], self.arr[parent] = self.arr[parent], self.arr[i]
        
        # Recursively heapify the parent node
            self.heapify_up(parent)
    
    # i should be the current index 
    def heapify_down(self, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        # left 
        if ( left < len(self.arr) ) and ( self.arr[left] > self.arr[largest] ):
            largest = left
        
        #
        if ( right < len(self.arr) ) and ( self.arr[left] > self.arr[largest] ):
            largest = right
        
        if (largest != i):
            self.arr[i],self.arr[largest]=self.arr[largest],self.arr[i]

            #Recursively heapify the affected sub-tree
            self.heapify_down( largest )

    def insertNode(self,key):
        # Insert element to the list
        self.arr.append(key)
        
        # Heapify the new node following a Bottom-up approach
        self.heapify_up( len(self.arr) - 1 )   

    def deleteRoot(self):
        arr_len = len(self.arr)

        lastElement = self.arr[arr_len-1]

        self.arr[0] = lastElement

        arr_len = arr_len - 1   

        self.heapify_down(0)

    def peek(self):
        return self.arr[0] if self.arr else None
    

class PriorityQueue:
    def __init__(self):
        self.heap = MaxHeap()

    def enqueue(self, key):
        # insert a new element to the Queue
        self.heap.insertNode(key)
    
    def dequeue(self):
        # return the highest priority element which is the root of a Binary Max Heap and heapify down the Binary Max Heap
        self.heap.peek()
        self.heap.heapify_down(0)
    
# if __name__ == '__main__':
#     arr = [ 3,10, 11, 40, 5, 8]
#     heap = MaxHeap()
#     for i in arr:
#         heap.insertNode(i)
#     print(heap.arr)