# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 16:44:08 2023

@author: Yang Cairong
"""

class CannotAllocateException(Exception):
    pass

class IncapacityidIdException(Exception):
    pass

class SpaceEfficientAllocator:

    def __init__(self, max_capacity):
        self.max_capacity = max_capacity
        self.bool_array = [False] * max_capacity
# we don't know how many ids have been allocated, in the worst situation
# we need to traverse the whole list till the last location to find the free space
    def allocate(self):
        """Returns an unallocated id"""
        for allocate_id, allocate_state in enumerate(self.bool_array):
            if not allocate_state: #find the first meet False(Free)
                self.bool_array[allocate_id] = True  #change it into True->Allocated
                return allocate_id
        raise CannotAllocateException("No ids available")

    def release(self, release_id):
        """Releases the id and allows it to be allocated"""
#since we don't maintain any data structure to record the allocated id
# we need  to firstly ensure the id is within the proper range and then check the state          
        if not 0 <= release_id < self.max_capacity or not self.bool_array[release_id] :
            raise Exception(f"The id {release_id} cannot be released.")
        self.bool_array[release_id] = False


# Test the IDAllocator class
allocator = SpaceEfficientAllocator(7)

print(allocator.allocate())  # Output: 0
print(allocator.allocate())  # Output: 1
allocator.release(0)
print(allocator.allocate())  # Output: 0
print(allocator.allocate())  # Output: 2
allocator.release(2)
print(allocator.allocate())  # Output: 2
print(allocator.allocate())  # Output: 3
print(allocator.allocate())  # Output: 6
allocator.release(17)         #IncapacityidIdException: The id 7 cannot be released.
print(allocator.allocate())  # CannotAllocateException: No ids available
# allocator.release(7)
print(allocator.allocate())  # Output: 6
allocator.release(1)
allocator.release(3)
allocator.release(6)  #IncapacityidIdException: The id 6 cannot be released.
# allocator.release(12)
print(allocator.allocate())  # Output: 1 (The released ID is reused)
print(allocator.allocate())  # Output: 3 (Next available ID after 2)
# print(allocator.allocate())  # Output: 3 (Next available ID after 2)
print(allocator.allocate())  # Output: 3 (Next available ID after 2)
print(allocator.allocate())  # Output: 3 (Next available ID after 2)
print(allocator.allocate())  # Output: 3 (Next available ID after 2)
print(allocator.allocate())  # Output: 3 (Next available ID after 2)

