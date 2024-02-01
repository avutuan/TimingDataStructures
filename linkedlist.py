'''
Author: Tuan Vu
KUID: 3100366
Date: 3/17
Lab: lab06
Last modified: 3/17
Purpose: LinkedList class
'''
from node import Node

class LinkedList:
    def __init__(self): #Initialize variables of linked list
        self.front = None
        self.length=0

    def get_length(self): #Define function to return the length of the list
        return self.length

    def insert(self, index, entry): #Define function of insert to insert an entry at a particular index in the list which would increase the length by 1
        new_node=Node(entry)
        if 0>index or index>self.length:
            raise RuntimeError #Raise error if the index is less than 0 or greater than the length of the list
        elif index==0:
            new_node.next=self.front
            self.front=new_node
        else:
            curr_node=self.front
            for i in range(index-1):
                curr_node=curr_node.next
            new_node.next=curr_node.next
            curr_node.next=new_node
        self.length+=1

    def get_entry(self, index): #Return the entry at index, raises a RuntimeError otherwise.
        if index<0 and index>=self.length:
            raise RuntimeError
        curr = self.front
        for i in range(index):
            curr = curr.next
        return curr.entry

    def set_entry(self, index, entry): #Sets the entry at index, raises a RuntimeError otherwise. Even if successful, the length remains the same.
        if 0>index or index>self.length:
            raise RuntimeError
        else:
            curr_node=self.front
            for i in range(index):
                curr_node=curr_node.next
            curr_node.entry=entry

    def remove(self, index): #Removes the entry at the index. Valid indices range from 0 to length-1 inclusively. Each remove decreases the length by 1.
        if 0>index or index>self.length:
            raise RuntimeError
        if index == 0:
            self.front=self.front.next
        else:
            curr_node=self.front
            for i in range(index-1):
                curr_node=curr_node.next
            curr_node.next=curr_node.next.next
        self.length-=1

    def clear(self): #Empties the list
        self.front=None
        self.length=0

    def reverse(self):
        for _ in range(self.length):
            self.insert(_,self.get_entry(self.length-1))
            self.remove(self.length-1)

    def count(self, target):
        counter=0
        for i in range(self.length):
            if self.get_entry(i)==target:
                counter+=1
        return counter

dog=LinkedList()
dog.count(1)
