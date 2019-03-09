import numpy as np 

def ShellSort(a):
    '''
    希尔排序

    算法描述：
        1.选择一个增量序列t1，t2，…，tk，其中ti>tj，tk=1；
        2.按增量序列个数k，对序列进行k 趟排序；
        3.每趟排序，根据对应的增量ti，将待排序列分割成若干长度为m 的子序列，分别对各子表进行直接插入排序。仅增量因子为1 时，整个序列作为一个表来处理，表长度即为整个序列的长度。
    参考：
    https://www.cnblogs.com/0zcl/p/6680652.html
    https://www.toutiao.com/a6622232676961108487/?app=news_article
    '''
    length = len(a)
    gap = int(length/2)
    while (gap>0):
        for i in range(length - gap):
            index = i + gap
            position = i
            next = a[index]
            while (position >= 0 ) and (a[position] > next):
                a[position+gap] = a[position]
                a[position] = next
                position = position - gap
        print('gap is %d' % (gap))
        print('array is:', a, '\n')
        gap //= 2        
    return a


if __name__ == '__main__':
    a = np.random.permutation(10)
    # a = [9, 8, 1, 4, 6, 7, 3, 2, 0, 5]
    print('original array is:', a, '\n')
    b = ShellSort(a)
    print('output array is:', b)
