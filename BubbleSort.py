import numpy as np
import time

def BubbleSort(a):
    '''
    冒泡排序

    算法描述：
        1.比较相邻的元素。如果第一个比第二个大，就交换它们两个；
        2.对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对，这样在最后的元素应该会是最大的数；
        3.针对所有的元素重复以上的步骤，除了最后一个；
        4.重复步骤1~3，直到排序完成。        
    '''
    for i in range (len(a)-1):
        for j in range (len(a)-1):
            if a[j] > a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
    return a


# if __name__ == '__main__':
#     a = np.random.permutation(10)
#     print(a)
#     b = BubbleSort(a)
#     print(b)
if __name__ == '__main__':
    # a = np.random.permutation(10)
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(a)
    t1 = time.time()
    for i in range(1):
        b = BubbleSort(a)
    t2 = time.time()
    ti = t2-t1
    print('spend time :', ti)
    print(b)
