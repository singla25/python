# Time function Execution

# Write a decorator that measures the time a function takes to execute

import time

def timer(func):
    def wrapper(*args, **kwargs):
        print(f"Executing {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} executed in {end-start} seconds")
        return result 
    return wrapper

@timer
def example_func(n):
    time.sleep(n)
    print(f"I sleep for {n} sec")

example_func(2)