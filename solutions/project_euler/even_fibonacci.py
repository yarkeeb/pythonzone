"""
Project Euler 2:
Each new term in the Fibonacci sequence is generated by adding the
previous two terms. By starting with 1 and 2, the first 10 imtes will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values
do not exceed 4 million, find the sum of the even-valued terms.
"""

x = 1
y = 2
z = 0
sum = 0

while z <= 4000000:
    z = y
    if z % 2 == 0:
        sum += y
    z = x + y
    x = y
    y = z

print sum
