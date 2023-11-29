# -*- coding: utf-8 -*-
"""
Spyder Editor

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
        
#def main():
if __name__=="__main__":
    counter = HitCounter();

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

