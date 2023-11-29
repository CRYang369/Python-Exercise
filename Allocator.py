# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 00:14:35 2023

@author: Yang Cairong
"""
import collections
class CannotAllocateException(Exception):
    pass

class InvalidIdException(Exception):
    pass
class Allocator:

    def __init__(self, max_val):
        self.queue = collections.deque()
        self.first_pass_idx = 0 #your interview might not require this optimization
        self.allocated = set()
        self.max_val = max_val
        
    def allocate(self): #get
        """Returns an unallocated id"""
        result = None
        if self.first_pass_idx < self.max_val:
            self.first_pass_idx += 1
            result = self.first_pass_idx - 1
        elif len(self.queue) > 0:
            result = self.queue.pop()
        if result is not None:
            self.allocated.add(result)            
            return result
        else:
            raise CannotAllocateException("No ids available")

    def release(self, id):
        """Releases the id and allows it to be allocated"""
        if (not 0 <= id < self.max_val) or (id not in self.allocated):
            #You should say that you'd like to throw an exception in case of an error
            raise InvalidIdException(f"The id {id} cannot be released.")
        self.allocated.remove(id)
        self.queue.appendleft(id)

# Test the IDAllocator class
allocator = Allocator(7)

print(allocator.allocate())  # Output: 0
print(allocator.allocate())  # Output: 1
print(allocator.allocate())  # Output: 2
print(allocator.allocate())  # Output: 3
print(allocator.allocate())  # Output: 4
print(allocator.allocate())  # Output: 5
print(allocator.allocate())  # Output: 6
# allocator.release(7)         #InvalidIdException: The id 7 cannot be released.
# print(allocator.allocate())  # CannotAllocateException: No ids available
# allocator.release(7)

allocator.release(1)
allocator.release(6)  #InvalidIdException: The id 6 cannot be released.

print(allocator.allocate())  # Output: 1 (The released ID is reused)
print(allocator.allocate())  # Output: 3 (Next available ID after 2)

