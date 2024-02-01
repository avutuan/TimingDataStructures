'''
Author: Tuan Vu
KUID: 3100366
Date: 3/17
Lab: lab06
Last modified: 3/17
Purpose: implementing time
'''
import time
from stack import Stack
from linkedqueue import LinkedQueue
from linkedlist import LinkedList

def nanosec_to_sec(ns):
    BILLION = 1000000000
    return ns/BILLION

def singlepoptimer():
    filler=1000
    while filler<=100000:
        counter=0
        counter_stack=Stack()
        while counter<=filler:
            counter_stack.push(counter)
            counter+=1
        
        print("Beginning the timing code...")
        start_time = time.perf_counter_ns() #start timer
        
        '''code we're timing'''
        counter_stack.pop()

        end_time = time.perf_counter_ns() #end timer
        print(f'Stack with {filler} elements')
        print("Total time in ns: ", end_time-start_time)
        print("Total time in sec: ", nanosec_to_sec(end_time-start_time), '\n')
        filler+=1000

def allpoptimer():
    filler=1000
    while filler!=100000:
        counter=0
        counter_stack=Stack()
        while counter<=filler:
            counter_stack.push(counter)
            counter+=1
        
        print("Beginning the timing code...")
        start_time = time.perf_counter_ns() #start timer
        
        '''code we're timing'''
        while not counter_stack.is_empty():
            counter_stack.pop()
            
        end_time = time.perf_counter_ns() #end timer
        print(f'Stack with {filler} elements')
        print("Total time in ns: ", end_time-start_time)
        print("Total time in sec: ", nanosec_to_sec(end_time-start_time), '\n')
        filler+=1000

def enqueuetimer():
    filler=1000
    while filler<=100000:
        counter=0
        counter_queue=LinkedQueue()
        while counter<=filler:
            counter_queue.enqueue(counter)
            counter+=1
        print("Beginning the timing code...")
        start_time = time.perf_counter_ns() #start timer
        
        '''code we're timing'''
        counter_queue.enqueue('corn')
        
        end_time = time.perf_counter_ns() #end timer
        print(f'Stack with {filler} elements')
        print("Total time in ns: ", end_time-start_time)
        print("Total time in sec: ", nanosec_to_sec(end_time-start_time), '\n')
        filler+=1000

def entryzerotimer():
    filler=1000
    while filler<=100000:
        counter=0
        counter_list=LinkedList()
        while counter<=filler:
            counter_list.insert(0, counter)
            counter+=1
        
        print("Beginning the timing code...")
        start_time = time.perf_counter_ns() #start timer
        
        '''code we're timing'''
        counter_list.get_entry(0)
        
        end_time = time.perf_counter_ns() #end timer
        print(f'Stack with {filler} elements')
        print("Total time in ns: ", end_time-start_time)
        print("Total time in sec: ", nanosec_to_sec(end_time-start_time), '\n')
        filler+=1000
        
def entryzerotimer():
    filler=1000
    while filler<=100000:
        counter=0
        counter_list=LinkedList()
        while counter<=filler:
            counter_list.insert(0, counter)
            counter+=1
            
        print("Beginning the timing code...")
        start_time = time.perf_counter_ns() #start timer

        '''code we're timing'''
        counter_list.get_entry(0)
        
        end_time = time.perf_counter_ns() #end timer
        print(f'Stack with {filler} elements')
        print("Total time in ns: ", end_time-start_time)
        print("Total time in sec: ", nanosec_to_sec(end_time-start_time), '\n')
        filler+=1000

def lastentrytimer():
    filler=1000
    while filler<=100000:
        counter=0
        counter_list=LinkedList()
        while counter<=filler:
            counter_list.insert(0, counter)
            counter+=1
            
        print("Beginning the timing code...")
        start_time = time.perf_counter_ns() #start timer

        '''code we're timing'''
        counter_list.get_entry(counter_list.length-1)
        
        end_time = time.perf_counter_ns() #end timer
        print(f'Stack with {filler} elements')
        print("Total time in ns: ", end_time-start_time)
        print("Total time in sec: ", nanosec_to_sec(end_time-start_time), '\n')
        filler+=1000

def printtimer():
    filler=1000
    while filler<=100000:
        counter=0
        counter_list=LinkedList()
        while counter<=filler:
            counter_list.insert(0, counter)
            counter+=1
            
        print("Beginning the timing code...")
        start_time = time.perf_counter_ns() #start timer

        '''code we're timing'''
        print_list=[]
        while counter_list.length!=0:
            print_list.append(counter_list.get_entry(counter_list.length-1))
            counter_list.remove(counter_list.length-1)
        print(print_list)
        
        end_time = time.perf_counter_ns() #end timer
        print(f'Stack with {filler} elements')
        print("Total time in ns: ", end_time-start_time)
        print("Total time in sec: ", nanosec_to_sec(end_time-start_time), '\n')
        filler+=1000
        
printtimer()
