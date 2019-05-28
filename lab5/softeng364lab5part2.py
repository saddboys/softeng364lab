
# This program is adapted from the GEvent tutorial:
# http://sdiehl.github.io/gevent-tutorial/
import gevent
import time
num_tasks = 10

def now():
    return time.perf_counter()

def one_task(pid):
    # "pid" is "process identifier", a number
    expected = 1.0 # seconds
    print('{}: "Working" for {:f} sec... '.format(pid, expected))
    start_time = now()
    gevent.sleep(seconds=expected) # "hard work" :)
    actual = now() - start_time
    print('{}: Finished after {:f} sec'.format(pid, actual))

def run_timed(fun, *args, title="Running..."):
    print(title)
    start_time = now()
    fun(*args)
    print('Required: {:f} sec'.format(now() - start_time))
    
def run_tasks_synchronously():
    for pid in range(num_tasks):
        one_task(pid)
        
def run_tasks_asynchronously():
    threads = [gevent.spawn(one_task, pid) for pid in range(num_tasks)]
    gevent.joinall(threads)
    
run_timed(run_tasks_synchronously, title="Synchronous...")
run_timed(run_tasks_asynchronously, title="Asynchronous...")