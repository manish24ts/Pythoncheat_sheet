from collections import deque

dq = deque([1, 2, 3])

dq.append(4)           # [1, 2, 3, 4]
dq.appendleft(0)       # [0, 1, 2, 3, 4]

dq.pop()               # removes 4
dq.popleft()           # removes 0

dq.extend([5, 6])      # [1, 2, 3, 5, 6]
dq.extendleft([-1, -2])# [-2, -1, 1, 2, 3, 5, 6]

dq.remove(2)           # removes first 2
dq.reverse()           # reverses deque
dq.rotate(2)           # rotates 2 steps right
dq.rotate(-1)          # rotates 1 step left

print(dq.count(3))     # number of times 3 appears
copy_dq = dq.copy()    # make a shallow copy
dq.clear()             # now dq is empty
