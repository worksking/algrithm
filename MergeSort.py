import numpy as np 

def Merge(left, right):
    output = []
    while len(left) > 0 and len(right)>0:
        if left[0] <= right[0]:
            output.append(left.pop(0))
        else:
            output.append(right.pop(0))

    #while循环出来之后 说明其中一个数组没有数据了，我们把另一个数组添加到结果数组后面
    output += left
    output += right
    print('output is :', output, '\n')
    return output

def MergeSort(a):
    '''
    归并排序

    算法描述：
        1.把长度为n的输入序列分成两个长度为n/2的子序列；
        2.对这两个子序列分别采用归并排序；
        3.将两个排序好的子序列合并成一个最终的排序序列。
    参考：
    https://www.cnblogs.com/Lin-Yi/p/7309143.html
    '''
    # 不断递归调用自己一直到拆分成成单个元素的时候就返回这个元素，不再拆分了
    if len(a) == 1:
        return a
    length= len(a)

    # 取拆分的中间位置    
    middle = length // 2
    
    #拆分过后左右两侧子串
    left = a[:middle]
    right = a[middle:]
    print('left and right:',left, right)

    # 对拆分过后的左右再拆分 一直到只有一个元素为止
    # 最后一次递归时候lef和rig都会接到一个元素的列表
    # 最后一次递归之前的lef和rig会接收到排好序的子序列
    lef = MergeSort(left)
    rig = MergeSort(right)
    print('lef and rig:',lef, rig, '\n')
    # 我们对返回的两个拆分结果进行排序后合并再返回正确顺序的子列表
    # 这里我们调用拎一个函数帮助我们按顺序合并lef和rig
    return Merge(lef, rig)


if __name__ == '__main__':
    # a = np.random.permutation(10)
    a = [0, 1, 9, 3, 2, 4, 5, 8, 7, 6]
    print('original array is:', a, '\n')
    b = MergeSort(a)
    # print('output array is:', b)



