import heapq
from collections import deque
from typing import List
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hm = {}
        for t in tasks:
            if t in hm:
                hm[t] = hm[t] + 1
            else:
                hm[t] = 1
        time = 0
        max_heap = [(-v,k) for v, k in zip(hm.values(), hm.keys()) ]
        heapq.heapify(max_heap)
        queue = []
        while max_heap or queue:
            time += 1
            if max_heap:
                #max heap exists
                front = heapq.heappop(max_heap)
                #Add one instead of subtract because negative 
                #for max heap
                front = (front[0] +1, front[1])
                if front[0] < 0:
                    queue.append((front[0], front[1], time + n))
            else:
                #Max heap empty
                time = queue[0][2]
                count, task, ready_time = queue.pop(0)
                heapq.heappush(max_heap, (count,task))
                
            if queue and queue[0][2] == time:
                front = queue.pop(0)
                heapq.heappush(max_heap, (front[0], front[1]))
        return time
