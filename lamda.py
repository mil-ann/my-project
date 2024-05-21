def square(x):
    return x**2
# lambda x: x ** 2
numbers = [1,2,3,4,5]

squares = map(lambda x: x ** 2, numbers)
print(list(squares))