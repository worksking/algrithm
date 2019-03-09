import numpy as np 
import time

def jiwei_sort(a):
    length = len(a)
    for i in range (length-1):
        sort_num = 0
        if (i+1)%2 == 0:
            for j in range (length-1):
                if a[length-1-j]<a[length-2-j]:
                    temp = a[length-2-j]
                    a[length-2-j] = a[length-1-j]
                    a[length-1-j] = temp
                    sort_num += 1
            print('ou shu:',a)
            if sort_num == 0:
                return a
            
        else:
            for j in range(length-1):
                if a[j+1] < a[j]:
                    temp = a[j]
                    a[j] = a[j+1]
                    a[j+1] = temp
                    sort_num += 1
            print('ji shu :',a)
            if sort_num == 0:
                return a
    return a


if __name__ == '__main__':
    # a = np.random.permutation(10)
    a = [1,2,3,4,5,6,7,8,9]
    print(a)
    t1 = time.time()
    for i in range(1):
        b = jiwei_sort(a)
    t2 = time.time()
    ti = t2-t1
    print('spend time :' , ti)
    print(b)

