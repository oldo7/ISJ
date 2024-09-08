#!/usr/bin/env python3

import collections

def log_and_count(counts, key=None):
    if(type(counts) is not collections.Counter):                        #kontrola ci counts je counter
        print("error: provided counts variable is not a couner")
        exit(1)
    def outer(func):
        def inner(*args, **kwargs):
            print(f"called {func.__name__} with {args} and {kwargs}")   #vypis spravy o zavolani funkcie
            newKey = key
            if newKey is None:
                newKey = func.__name__
            counts[newKey] += 1                                         #navysenie counteru
        return inner
    return outer

import collections

my_counter = collections.Counter()

@log_and_count(key = 'basic functions', counts = my_counter)
def f1(a, b=2):
    return a ** b

@log_and_count(key = 'basic functions', counts = my_counter)
def f2(a, b=3):
    return a ** 2 + b

@log_and_count(counts = my_counter)
def f3(a, b=5):
    return a ** 3 - b

f1(2)
f2(2, b=4)
f1(a=2, b=4)
f2(4)
f2(5)
f3(5)
f3(5,4)

print(my_counter)