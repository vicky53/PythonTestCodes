def triangle(n):
    dots = 0
    for val in range(1, n+1):
        dots = dots + val
    return dots


print(triangle(1))
print(triangle(2))
print(triangle(3))
print(triangle(8))
print(triangle(2153))



