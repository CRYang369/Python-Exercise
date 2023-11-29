# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 15:43:59 2023

@author: Yang Cairong
"""
class CannotAllocateException(Exception):
    pass
class IncapacityidIdException(Exception):
    pass

import collections
class Allocator:

    def __init__(self, max_capacity):

        self.max_capacity= max_capacity
        self.queue = collections.deque()
        self.allocated = set()
        
    def allocate(self):
        """Returns an unallocated id"""
      
        if len(self.queue) > 0:
            allocate_id = self.queue.pop()
        elif len(self.allocated) < self.max_capacity:
            allocate_id = len(self.allocated)
            # print(allocate_id)
        else:
            raise CannotAllocateException("No ids available")  

        self.allocated.add(allocate_id)
        # print(f'{id} has been allocated')
        return allocate_id

    def release(self, release_id):
        """Releases the id and allows it to be allocated"""
        if release_id not in self.allocated or  not 0 <= release_id < self.max_capacity :
            raise IncapacityidIdException(f"The id {release_id} cannot be released.")
        self.allocated.remove(release_id)
        self.queue.appendleft(release_id)
        # print( f'{release_id} has been released')
        
        
# Test the IDAllocator class
allocator = Allocator(7)
print(allocator.max_capacity)
print(allocator.allocate())  # Output: 0
print(allocator.allocate())  # Output: 1
allocator.release(0)
print(allocator.queue)
print(allocator.allocate())  # Output: 0
print(allocator.queue)
print(allocator.allocate())  # Output: 2
allocator.release(2)
print(allocator.allocate())  # Output: 2
print(allocator.allocate())  # Output: 3
print(allocator.allocate())  # Output: 6
# allocator.release(17)         #IncapacityidIdException: The id 7 cannot be released.
print(allocator.allocate())  # CannotAllocateException: No ids available
# allocator.release(7)
print(allocator.allocate())  # Output: 6
allocator.release(1)
allocator.release(3)
allocator.release(6)  #IncapacityidIdException: The id 6 cannot be released.
# allocator.release(17)  
print(allocator.allocate())  # Output: 1 (The released ID is reused)
print(allocator.allocate())  # Output: 3 (Next available ID after 2)
# print(allocator.allocate())  # Output: 3 (Next available ID after 2)
print(allocator.allocate())  # Output: 3 (Next available ID after 2)
print(allocator.allocated)
print(allocator.queue)








