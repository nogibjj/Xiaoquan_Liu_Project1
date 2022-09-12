import random
# write a hello function that prints hello world
def hello():
    print("Hello World")

#invoke the function
hello()

#write a decorator function logs input and output and times it to a function
def logs(func):
    def wrapper(*args, **kwargs):
        print("Calling {} with  arguments {}" .format(func.__name__, args))
        result = func(*args, **kwargs)
        print("{} returned {}" .format(func.__name__, result))
        return result
    return wrapper

# invoke the decorator function using hello function
@logs
def hello(x):
    print("Hello World! {}".format(x))

#invoke the function
hello(3)

# write a function that yields a generator that randomly picks between three types of fruits
def fruits_generator():
    fruits = ["apple", "banana", "orange"]
    while True:
        yield fruits[random.randint(0,2)]

#invoke fruit_generator function and print the result of the generator of five runs
for i in range(5):
    print(next(fruits_generator()))


