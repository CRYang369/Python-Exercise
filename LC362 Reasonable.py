# -*- coding: utf-8 -*-
"""
Spyder Editor

Use 2 levels of nested lists.
For the inner list the first item is the timestamp and the second one is the number of hits at the moment
At hit function we will update the hits count if it's already in the deque.
Append a new item at the deque if it's still not appear in the deque.
For both cases we need to increment the counter.
When we get hits at getHits function,we need to consider the time constraint with 300 second.
We can count the time difference between the current timestamp and the head of the deque. 
If it's greater than or equal to 300 seconds we set as the default time differece,the head of the deque will be popped out.
And then we need updated the counter, the counter should subtract the second item of the head ie the hits number at that timestamp.
At last we return the length of the deque as the total hits within 300 second.

"""

from collections import deque
class HitCounter:
    def __init__(self):
        self.time_diff=300
        self.q=deque()
        self.counter=0
    def hit(self,timestamp):
        # current=len(self.q)-1 # the tail of the queue
        if self.q and timestamp==self.q[len(self.q)-1][0]:
            self.q[len(self.q)-1][1]+=1
        else:
            self.q.append([timestamp,1])
        
        self.counter+=1
        
    def getHits(self,timestamp):
        if self.q and timestamp-self.q[0][0]>=self.time_diff:
            _,num =self.q.popleft()
            self.counter-=num
        return self.counter
        
if __name__=="__main__":
    counter = HitCounter()

    counter.hit(1)
    counter.hit(1)
    counter.hit(2)
    counter.hit(2)
    counter.hit(3)
    #// 在时刻 4 统计过去 5 分钟内的敲击次数, 函数返回 3 。
    counter.getHits(4)
    #// 在时刻 300 敲击一次。
    counter.hit(300)
    #// 在时刻 300 统计过去 5 分钟内的敲击次数，函数返回 4 。
    print(counter.getHits(300))
    #// 在时刻 301 统计过去 5 分钟内的敲击次数，函数返回 3 。
    print(counter.getHits(301))


