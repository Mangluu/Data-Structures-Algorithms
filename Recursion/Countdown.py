import time

def countdown(n):
    if n == 0:
        return n
    print(n)
    time.sleep(1)
    return countdown(n - 1)

print(countdown(5))
