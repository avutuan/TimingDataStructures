'''
Author: Tuan Vu
KUID: 3100366
Date: 3/17
Lab: lab06
Last modified: 3/17
Purpose: node class
'''
class Node:
    def __init__(self, entry): #initializing variables for node
        self.entry = entry
        self.next = None
