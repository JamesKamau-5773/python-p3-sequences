#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print([])
        return
    fibonacci_sequence = []
    for i in range (length):
        if i == 0:
            fibonacci_sequence.append(0)
            
        elif i == 1:
            fibonacci_sequence.append(1)
        else:
            next_num =  fibonacci_sequence[-1] + fibonacci_sequence[-2]
            fibonacci_sequence.append(next_num)       
    print(fibonacci_sequence)        