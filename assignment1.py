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
#for example
n=5
inverted_upper_triangle(n)

#example output
# * * * * * 
# * * * * 
# * * *
# * *
# *



#PYRAMID
def pyramid_pattern(n):
    for i in range(n):
        print(' ' * (n-i-1), end='')
        print('* ' * (i+1))
# for example
if __name__ == "__main__":
    rows = 5
    pyramid_pattern(rows)

#example output
#     * 
#    * * 
#   * * *
#  * * * *
# * * * * *