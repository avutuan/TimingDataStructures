'''
Author: Tuan Vu
KUID: 3100366
Date: 3/17
Lab: lab06
Last modified: 3/17
Purpose: stack class
'''
from node import Node

class Stack:
    
    def __init__(self): #initializing the top of the stack
        self.top=None
        
    def push(self, entry): #defining the push method for the stack to make the entry the top
       node=Node(entry)
       node.next=self.top
       self.top=node
       
    def is_empty(self): #defining the is_empty method for the stack to check if the stack is empty and return a boolean value
        return self.top==None
    
    def peek(self): #defining the peek method to tell whats the current top of the stack
        if self.is_empty():
            raise RuntimeError
        else:
            return self.top.entry
        
    def pop(self): #defining the pop method that 
        if self.is_empty():
            raise RuntimeError
        else:
            temp = self.top
            self.top=temp.next
            return temp.entry
