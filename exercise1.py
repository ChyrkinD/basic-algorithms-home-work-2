import uuid
from queue import Queue
from random import randint

queue = Queue()

def generate_request():
    for _ in range(randint(0,2)):
        val  = str(uuid.uuid4())
        print(f'{val} - add to queue'.upper())
        queue.put(val)

def process_request():
    if not queue.empty():
        val = queue.get()
        print(f'{val} - get from queue'.upper())
    else:
        print('Queue is empty')

def main():
    print('Input "q" to stop loop')
    while True:
        generate_request()
        process_request()
        user_input = input()
        if user_input == 'q':
            break

if __name__ == '__main__':
    main()