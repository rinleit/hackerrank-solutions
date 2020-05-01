def fibonacci(n):
    prev, next = 0, 1
    for _ in range(2, n + 1):
        next, prev = prev + next, next
    return next
n = int(input())
print(fibonacci(n))