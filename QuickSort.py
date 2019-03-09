import numpy as np 
import time

# def QuickSort(ls, start, end):
#     '''
#     快速排序

#     算法描述：
#         1.从数列中挑出一个元素，称为 “基准”（pivot）；
#         2.重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。
#           在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作；
#         3.递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。
#     参考资料：
#         https://www.cnblogs.com/AlwinXu/p/5424905.html
#         https://www.cnblogs.com/kunpengv5/p/7833361.html
#         https://www.toutiao.com/a6622232676961108487/?app=news_article
#     '''
#     if start < end:
#         left = start
#         right = end
#         base = ls[left]
#         while left < right:
#             while left < right and ls[right] >= base:
#                 right -= 1
#             ls[left] = ls[right]

#             while left < right and ls[left] <= base:
#                 left += 1            
#             ls[right] = ls[left]
#         ls[left] = base
#         QuickSort(ls, start, left-1)
#         QuickSort(ls, left+1, end)
#     return ls

def Partition(ls, start, end):
    left = start
    right = end
    base = ls[left]
    while left < right:
        while left < right and ls[right] >= base:
            right -= 1
        while left < right and ls[left] <= base:
            left += 1
        if left < right:
            ls[left], ls[right] = ls[right], ls[left]
    ls[start]= ls[right]
    ls[right] = base 
    return right

def QuickSort(ls, start, end):
    if end > start:
        k = Partition(ls, start, end)
        QuickSort(ls, start, k-1)
        QuickSort(ls, k+1, end)
    return ls



if __name__ == '__main__':
    a = np.random.permutation(10)
    print(a,'\n')
    b = QuickSort(a, 0, len(a)-1)
    print(b)

