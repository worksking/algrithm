import numpy as np 

def change(a):
    if a < 0:
        a=-a
        i = a / 10
        j = 0
        b = 0
        while (i > 0):
            j = j + 1
            i //= 10
        for k in range (j+1):
            temp = a - (a//10)*10
            b += temp*(10**(j-k))
            a = a // 10
        b = -b
    else:
        i = a / 10
        j = 0
        b = 0
        while (i > 0):
            j = j + 1
            i //= 10
        for k in range(j+1):
            temp = a - (a//10)*10
            b += temp*(10**(j-k))
            a = a // 10
    return b

if __name__ == '__main__':
    a = -275203472
    b = change(a)
    print(a, b)
