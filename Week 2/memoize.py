
def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper


#@memoize
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

fib = memoize(fib)

#print(fib(40))

import time

for i in range(1, 39):
    t1 = time.time()
    fib(i)
    print "Tiempo: ", i, " -- ", time.time()-t1