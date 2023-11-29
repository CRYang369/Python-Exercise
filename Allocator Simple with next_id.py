# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 14:48:34 2023

@author: Yang Cairong
"""


class CannotAllocateException(Exception):
    pass

class InvalidIdException(Exception):
    pass

import collections
class Allocator:

    def __init__(self, max_capacity):
        # self.queue = []# FILO,the allocated order equal to the release order need to use deque() FIFO 
        self.queue=collections.deque()
        self.next_id = 0
        self.allocated = set()
        self.max_capacity = max_capacity
        
    def allocate(self):
        """Returns an unallocated id"""
        if self.queue:
            allocate_id = self.queue.pop()
        
        elif self.next_id < self.max_capacity:
            allocate_id = self.next_id
            self.next_id += 1
            # print(self.next_id)

        else:
            raise CannotAllocateException("No ids available")
        
        self.allocated.add(allocate_id)

        return f'{allocate_id} has been allocated.'

    def release(self, release_id):
        """Releases the id and allows it to be allocated"""       
    
        if release_id not in self.allocated:
            raise InvalidIdException(f"The id {release_id} cannot be released.")
        self.allocated.remove(release_id)
        self.queue.appendleft(release_id)
        return f'{release_id} has been released'

# Test the IDAllocator class
allocator = Allocator(7)

print(allocator.allocate())  # Output: 0
print(allocator.allocate())  # Output: 1
print(allocator.release(0))
print(allocator.allocate())  # Output: 0
print(allocator.allocate())  # Output: 2
print(allocator.release(2))
print(allocator.allocate())  # Output: 2
print(allocator.allocate())  # Output: 3
print(allocator.allocate())  # Output: 6
allocator.release(17)         #InvalidIdException: The id 7 cannot be released.
print(allocator.allocate())  # CannotAllocateException: No ids available
# allocator.release(7)
print(allocator.allocate())  # Output: 6
allocator.release(1)
allocator.release(3)
allocator.release(6)  #InvalidIdException: The id 6 cannot be released.

print(allocator.allocate())  # Output: 1 (The released ID is reused)
print(allocator.allocate())  # Output: 3 (Next available ID after 2)
# print(allocator.allocate())  # Output: 3 (Next available ID after 2)
print(allocator.allocate())  # Output: 3 (Next available ID after 2)
