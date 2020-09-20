import math

def prob(n, p):
    result = p * pow((1 - p), n - 1)
    return result

def infoMeasure(n, p):
    pr = prob(n, p)
    result = - math.log(pr, 2)
    return result

def sumProb(N, p):
    """ Khi thực hiện hàm sumProb(500, 0.2) kết quả thu đuọc là0.9999999999999998 ~ 1
        Khi thực hiện hàm sumProb(5000, 0.2) ta được kết quả là 0.999999999999998 ~ 1
        => hàm sumProb có thể sử dụng để kiểm chứng tổng xác suất của phân bố geometric bằng 1 """
    sum = 0
    for i in range(1, N):
        sum += prob(i, p)
    return sum

def approxEntropy(N, p):
    """ Entropy của nguồn geometric với N=100, p=1/2 là 1.9999999999999998 ~ 2
        Entropy của nguồn geometric với N=1000, p=1/2 là 1.9999999999999998 ~ 2
        => hàm approxEntropy tính xấp xỉ entropy của nguồn tin geometric với p=1/2 bằng 2"""
    entropy = 0
    for i in range(1, N):
        entropy += prob(i, p) * infoMeasure(i, p)
    return entropy
    
print(sumProb(500, 0.2))
print(sumProb(5000, 0.2))
print(approxEntropy(100, 0.5))
print(approxEntropy(1000, 0.5))

