'''
    知识背景： if n==1, f(n) = 1,
              if n==2, f(n) = 1,
              if n >2, f(n) = f(n-1) + f(n-2).
    method 3 and method 4 are very important. 
'''
#############################################################
## method 1: recurse/递归解法
# 每次都要计算之前的所有值，这样造成了极大的资源浪费
# T(n) = T(n-1) + T(n-2) + θ(1) >= 2*T(n-2) = θ(2^(n/2))
def fibonacci_tool_1(n):
    if n <= 2:
        return 1
    else:
        return fibonacci_tool_1(n-1) + fibonacci_tool_1(n-2)

def fibonacci_1(n):
    for i in range(1,n+1):
        print(fibonacci_tool_1(i))
##############################################################



#############################################################
## method 2: 循环
#‘循环’相对于‘递归’而言，不会出现递归带来的大量资源浪费现象。
def fibonacci_tool_2(n):
    if n <= 2:
        return 1
    else:
        a = 1
        b = 1
        for i in range(3, n+1):
            c = a + b
            a = b
            b = c
        return c

def fibonacci_2(n):
    for i in range(1, n+1):
        print(fibonacci_tool_2(i))
#############################################################


#############################################################
'''
method 3: memorized dynamic program algorithm/迭代
    -this method fib(k) only recurses the first time it's called
    -memorized caslls cost θ(1)
    -nonmemorized calls is n :fib(1), fib(2), ...., fib(n)
    the nonrecursive work per call is θ(1),is consatant.
    time = θ(n)
'''
def fibonacci_3(n):
    memo = [0, 1]
    for i in range(2, n+1):
        memo.append(memo[i-1] +memo[i-2])
    return memo[n]
#############################################################



#############################################################
'''
## method 4:  matrix manipulation/矩阵运算
# 参考网址： http://www.spytensor.com/index.php/archives/24/
'''


def fibonacci_4(n):
    import numpy as np
    matrix = np.matrix('1 1; 1 0')
    # print(matrix)
    memo = []
    for i in range(0,n):
        fib_i = np.array((matrix**i))[0][0]
        memo.append(fib_i)
        print(fib_i)
    return memo
##############################################################




if __name__ == '__main__':

    # fibonacci_1(5)

    # fibonacci_2(5)

    # print(fibonacci_3(10))

    fibonacci_4(10)
