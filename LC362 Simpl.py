# -*- coding: utf-8 -*-
"""
Spyder Editor
Design a hit counter which counts the number of hits received in the past 5 minutes.
Each function accepts a timestamp parameter (in seconds granularity)
and you may assume that calls are being made to the system in chronoogical order
(ie.the timestamp is monotonically increasing).The earlist timestamp starts at 1.
It is possible that several hits arrive roughtly at the same time

Store each hit in a deque.For getHits() remove all hits longer than or equal to
300 seconds ago.
Alternatively, to reduce memory use and increase performance
of getHits() store the count along with timestamp so multiple hits at same timestamp are
grouped.
Time -O(1) for init and hit(),O(n) for getHits().
number of hits since previous getHits().
Space O(n)
                                                                                 

This is a temporary script file.
"""

from collections import deque
class HitCounter:
    def __init__(self):
        self.time_diff=300
        self.q=deque()
    def hit(self,timestamp):
        self.q.append(timestamp)
    def getHits(self,timestamp):
        while self.q and timestamp-self.q[0]>=self.time_diff:
            self.q.popleft()
        return len(self.q)
        
if __name__=="__main__":
    counter = HitCounter();

    counter.hit(1);

    counter.hit(2);
 
    counter.hit(3)
    #// 在时刻 4 统计过去 5 分钟内的敲击次数, 函数返回 3 。
    counter.getHits(4)
    #// 在时刻 300 敲击一次。
    counter.hit(300)
    #// 在时刻 300 统计过去 5 分钟内的敲击次数，函数返回 4 。
    print(counter.getHits(300))
    #// 在时刻 301 统计过去 5 分钟内的敲击次数，函数返回 3 。
    print(counter.getHits(301))


