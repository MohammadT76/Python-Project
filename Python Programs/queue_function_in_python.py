
# about queue in python 
# https://www.guru99.com/python-queue-example.html

import queue

q1 = queue.Queue(5) #The max size is 5.

q1.put(1)
q1.put(2)
q1.put(3)
q1.put(4)
q1.put(5)

print(q1.full()) # will return true.
print(q1)
print(q1.get())
print(q1.get())
print(q1.full()) # will return true.


# %%

import queue
q1 = queue.Queue(22)

for i in range(20):
    q1.put(i) # this will additem from 0 to 20 to the queue
    
print(q1.full())

# %%
