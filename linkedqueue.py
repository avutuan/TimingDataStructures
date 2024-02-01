'''
Author: Tuan Vu
KUID: 3100366
Date: 3/17
Lab: lab06
Last modified: 3/17
Purpose: queue class
'''
from node import Node

class LinkedQueue:
    
    def __init__(self): #defining the front and back of the queue
        self._front=None
        self._back=None
        
    def enqueue(self,entry): #defining enqueue to add the entry to the back of the queue
        new_node=Node(entry)
        if self._front==None:
            self._front=new_node
        else:
            self._back.next=new_node
        self._back=new_node
            
    def dequeue(self): #defining dequeue to remove and return the value at the front of the queue
        if self._front==None:
            raise RuntimeError
        else:
            cur_front=self._front
            self._front=cur_front.next
            if self._front==None:
                self._back=None
            return cur_front.entry

    def is_empty(self): #defining is_empty to return whether or not the queue is empty
        return self._front==None

    def peek_front(self): #defining peek_front to return the value at the front of the queue
        if self.is_empty():
            raise RuntimeError
        else:
            return self._front.entry
