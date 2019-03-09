import numpy as np

def SelectSort(a):
    '''
    选择排序
    
    算法描述：
        1.初始状态：无序区为a[1..n]，有序区为空；
        2.第i趟排序(i=1,2,3…n-1)开始时，当前有序区和无序区分别为a[1..i-1]和a(i..n）。该趟排序从当前无序区中-选出关键字最小的记录 a[k]，
        将它与无序区的第1个记录R交换，使R[1..i]和R[i+1..n)分别变为记录个数增加1个的新有序区和记录个数减少1个的新无序区；
        3.n-1趟结束，数组有序化了。 
    '''
    # ways 1
    for i in range(len(a)-1):
        for j in range (i+1, len(a)):
            if a[i] > a[j]:
                min = a[j]
                a[j] = a[i]
                a[i] = min
    #ways 2
    # for i in range(len(a)-1):
    #     min_Index = i
    #     for j in range (i+1, len(a)):
    #         if a[min_Index] > a[j]:
    #             min_Index = j
    #     temp = a[i]
    #     a[i] = a[min_Index]
    #     a[min_Index] = temp

    return a


if __name__ == '__main__':
    a = np.random.permutation(10)
    print(a)
    b = SelectSort(a)
    print(b)
