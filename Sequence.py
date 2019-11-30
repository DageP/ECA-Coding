def fib():
    a, b = 1, 1
    while 1: #While this is true
        yield a #only return a 
        a, b = b, a + b

import types
if type(fib()) == types.GeneratorType:
    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 30:
            break
