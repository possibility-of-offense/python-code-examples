# The + operator concatenates lists:

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)
[1, 2, 3, 4, 5, 6]
# Similarly, the * operator repeats a list a given number of times:

[0] * 4
[0, 0, 0, 0]
[1, 2, 3] * 3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
# # The first example repeats four times. The second example repeats the list three times.

# A slice operator on the left side of an assignment can update multiple elements:

t = ['a', 'b', 'c', 'd', 'e', 'f']
t[1:3] = ['x', 'y']
print(t)
['a', 'x', 'y', 'd', 'e', 'f']

# To remove more than one element, you can use del with a slice index:

t = ['a', 'b', 'c', 'd', 'e', 'f']
del t[1:5]
print(t)
['a', 'f']