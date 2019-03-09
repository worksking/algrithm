import numpy as np
def InsertSort(a):
    '''
    插入排序

    算法描述：
        1.从第一个元素开始，该元素可以认为已经被排序；
        2.取出下一个元素，在已经排序的元素序列中从后向前扫描；
        3.如果该元素（已排序）大于新元素，将该元素移到下一位置；
        4.重复步骤3，直到找到已排序的元素小于或者等于新元素的位置；
        5.将新元素插入到该位置后；
        6.重复步骤2~5。
    '''
    for i in range(len(a)-1):
        next = a[i+1]
        for j in range(i+1):
            if a[i-j] > next:
                a[i-j+1] = a[i-j]
                a[i-j] = next
    return a

if __name__ == '__main__':
    a = np.random.permutation(10)
    print(a)
    b = InsertSort(a)
    print(b)

                

