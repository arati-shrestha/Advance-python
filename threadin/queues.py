from threading import Thread, Lock, current_thread
from queue import Queue 
import time

def worker(q):
    while True:
        value = q.get()

        #processing
        with lock:
            print(f'in {current_thread().name} got {value} ')
        q.task_done()

if __name__ == "__main__":
    q = Queue()
    lock = Lock()
    num_threads = 10
    
    for i in range(num_threads):
        thread = Thread(target= worker, args = (q,))
        thread.daemon = True
        thread.start()
        
    for i in range(1,21):
        q.put(i)    
    q.join()

print('end main')
        
        
        
        
        
        
        
#     q.put(1)
#     q.put(2)
#     q.put(3)
#     q.put(4)
    
# #4,3,2,1 -->
#     first = q.get()
#     print(first)
#     print(q.empty()) #returns true if queue is empty
#     q.task_done() #returns true if all the task is complete
    
#     q.join() #blocks the main thread until the elements in the queue is processed

#     print('end main ')