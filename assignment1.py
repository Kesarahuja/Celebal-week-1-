#UPPER TRIANGULAR
def lower_triangle(n):
    for i in range(1, n + 1):
        print('*' * i)
#for example
lower_triangle(5)

#example output
# *
# **
# ***
# ****
# *****

#LOWER TRIANGULAR 
def inverted_upper_triangle(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print('*', end=' ')
        print() 
n=5
inverted_upper_triangle(n)