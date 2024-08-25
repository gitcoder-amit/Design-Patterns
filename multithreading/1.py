import threading
from threading import Thread
import time


def thrdFunc():
    print('start')
    time.sleep(5)
    print('end')


thrd = Thread(target=thrdFunc)
thrd.start()
thrd.join()   # join will wait for this particular thread to complete if we will not write this line then active_count
# will be print first after then end

print(threading.active_count())