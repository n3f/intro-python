import multiprocessing
import os

def do_this(what):
    whoami(what)
    
def whoami(what):
    print('process:%s says %s' % (os.getpid(), what))


if __name__ == "__main__":
    whoami("I'm the main program")
    for i in range(1,4):
        p = multiprocessing.Process(target=do_this, args=("I'm function %s" % i,))
        p.start()