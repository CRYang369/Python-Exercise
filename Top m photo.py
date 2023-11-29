# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 17:54:56 2023

@author: Yang Cairong
"""

import heapq

class LogIterator:
    def __init__(self, logs):
        self.logs = logs
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.logs):
            log = self.logs[self.index]
            self.index += 1
            return log
        else:
            raise StopIteration()

def top_m_visited_photos(logs, m):
    photo_count = {}
    for log in logs:
        photo_id = log['photoId']
        if photo_id not in photo_count:
            photo_count[photo_id] = 1
        else:
            photo_count[photo_id] += 1

    priority_queue = []
    for photo_id, count in photo_count.items():
        heapq.heappush(priority_queue, (-count, photo_id))
        if len(priority_queue) > m:
            heapq.heappop(priority_queue)

    top_m_photos = [photo_id for _, photo_id in priority_queue]
    return top_m_photos

# Example usage:
logs = [
    {'photoId': 1, 'timestamp': '2023-08-01'},
    {'photoId': 1, 'timestamp': '2023-08-02'},
    {'photoId': 1, 'timestamp': '2023-08-02'},
    {'photoId': 1, 'timestamp': '2023-08-03'},
    {'photoId': 1, 'timestamp': '2023-08-04'},
    {'photoId': 2, 'timestamp': '2023-08-02'},
    {'photoId': 2, 'timestamp': '2023-08-10'},
    {'photoId': 2, 'timestamp': '2023-08-02'},
    {'photoId': 2, 'timestamp': '2023-08-09'},
    {'photoId': 3, 'timestamp': '2023-08-02'},
    {'photoId': 3, 'timestamp': '2023-08-04'},
    {'photoId': 3, 'timestamp': '2023-08-02'},
    {'photoId': 4, 'timestamp': '2023-08-05'},
    {'photoId': 4, 'timestamp': '2023-08-02'},
    {'photoId': 5, 'timestamp': '2023-08-06'},
    {'photoId': 6, 'timestamp': '2023-08-06'},
    {'photoId': 7, 'timestamp': '2023-08-06'},
    # ... other log entries ...
]
m = 5
top_m = top_m_visited_photos(logs, m)
print(top_m)
