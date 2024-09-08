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