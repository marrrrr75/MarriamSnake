import random

def spawn(ms_size, snake_body):
    while True:
        pos = random.randint(0, ms_size[0]-1), random.randint(0, ms_size[1]-1)
        if pos not in snake_body:
            return pos
