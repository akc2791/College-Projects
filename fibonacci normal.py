#Define a faster fibonacci procedure that will enable us to computer
#fibonacci(36).

def fibonacci(n):
    current = 0
    after = 1

    i = 0
    while i < n:
        current,after = after,current + after
        i += 1
    return current







print fibonacci(36)
#>>> 14930352