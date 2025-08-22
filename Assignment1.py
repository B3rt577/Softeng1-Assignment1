'''
Title: EECS 348 Assignment 1
Description: CEO Email prioritization program
Input(s): Assignment1_Test_Files.txt
Output: Next email and number of unread emails
All collaborators: 
Author's name: Edbert Jensen
Creation Date: 8/22/2025
'''

class MaxHeap:
    def __init__(self):
        self.arr = []       # initialize an empty list when MaxHeap object is created
    
    # i should just be a variable that is the position or index the newly inserted node.
    def heapify(self, i):    
        # the definition of the parent property of Binary Heaps is (index - 1) floor division by 2
        parent = (i - 1) // 2   

        # A condition that checks if the parent is positie and whatever index i is bigger than the parent value
        if parent >= 0 and self.arr[i] > self.arr[parent]:       
            self.arr[i], self.arr[parent] = self.arr[parent], self.arr[i]
        
        # Recursively heapify the parent node
            self.heapify(parent)

    def insertNode(self,key):
        self.arr.append(key)
        
        #recursive
        self.heapify( len(self.arr) - 1 )   

    def peek(self):
        return self.arr[0] if self.arr else None
    
if __name__ == '__main__':
    arr = [ 3,10, 11, 40, 5, 8]
    heap = MaxHeap()
    for i in arr:
        heap.insertNode(i)
    print(heap.arr)