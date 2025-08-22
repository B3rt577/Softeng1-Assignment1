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
    def __init__(self,i):
        self.arr = []       # initialize an empty list when MaxHeap object is created
        self.i = i          # index i variable is tracked to act as pointer

    def heapify(self):
        parent = (self.i - 1) // 2

        if parent >= 0 and self.arr[i] > self.arr[parent]:
            self.arr[self.i], self.arr[parent] = self.arr[parent], self.arr[self.i]
        
        # Recursively heapify the parent node
            MaxHeap.heapify(self.arr, parent)

    def insertNode(self,key):
        self.arr.append(key)

        MaxHeap.heapify(self.arr, len(self.arr)- 1 )

    def peek(self):
        return self.arr[0]
    
    def 
