import threading
import time


def timer(timer_runs):

    while timer_runs.is_set():
        ##Acá hará el proceso
        time.sleep(60)   # 60 segundos.

timer_runs = threading.Event()

timer_runs.set()

t = threading.Thread(target=timer, args=(timer_runs,))

