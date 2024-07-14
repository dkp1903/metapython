## The Global Interpreter Lock in Python is often understood inaccurately. While GIL ensures that multiple threads do not run the same Python bytecode, 
## it does not guarantee thread safety for mutable objects, lists for example, which are ubiquitously used.



import threading

my_list = [] # a list is a non thread safe DS, and multiple threads can write to the same list.
# my_list = queue.Queue() # A queue is thread safe, and should instead be used here
# The GIL ensures that only one thread runs at a time, but it cannot ensure two different threads won't append to it one after the other, in which case, we'd get an
# incorrect output

def append_to_list(value):
    my_list.append(value)

threads = [threading.Thread(target=append_to_list, args=(i,)) for i in range(100)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

print(len(my_list))  # Expected: 100, Actual: <100 (due to data corruption)



