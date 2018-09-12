import multiprocessing as mp
import os

def washer(dishes, output):
    for dish in dishes:
        print('Washing', dish, 'dish:', os.getpid(), flush=True)
        output.put(dish)

def dryer(input):
    while True:
        dish = input.get()
        print('Drying', dish, 'dish', os.getpid(), flush=True)
        input.task_done()

if __name__ == "__main__":
    num_processes = 2
    num_guests = 10
    dish_queue = mp.JoinableQueue()
    for i in range(num_processes + 1):
        dryer_proc = mp.Process(target=dryer, args=(dish_queue,))
        dryer_proc.daemon = True
        dryer_proc.start()

    dishes = ['salad', 'bread', 'entree', 'dessert'] * num_guests
    washer(dishes, dish_queue)
    dish_queue.join()