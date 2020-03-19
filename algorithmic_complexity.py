import time

def factorial(n):
    response = 1

    while n > 1:
        response *= n
        n -= 1

    return response

def recursive_factorial(n):
    if n == 1:
        return1
    return n * factorial(n - 1)

if __name__ == '__main__':
    n = 1000

    start = time.time()
    factorial(n)
    end = time.time()
    print(end - start)

    start = time.time()
    recursive_factorial(n)
    end = time.time()
    print(end -start)
