import signal
import time

def handler(signum, frame):
    print("Forever is over!")
    raise Exception("end of time")

def loop_forever():
    while 1:
        print("sec")
        time.sleep(1)

signal.signal(signal.SIGALRM, handler)
signal.alarm(10)
try:
    loop_forever()
except Exception, exc:
    print(exc)