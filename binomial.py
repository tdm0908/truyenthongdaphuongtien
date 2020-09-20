def prob(n, p, N):
    fact = lambda f: 1 if f == 0 else f * fact(f - 1)
    nCk = fact(N) / (fact(n) * fact(N - n))
    result = nCk * pow(p, n) * pow(1 - p, N - n)
    return result

def infoMeasure(n, p, N):
    pr = prob(n, p, N)
    result = - math.log(pr, 2)
    return result

def sumProb(N, p):
    """ Khi gọi hàm sumProb(100, 0.2) ta được kết quả là 0.9999999997963016 ~ 1
        Khi gọi hàm sumProb(500, 0.3) ta được kết quả là 0.9999999999999714 ~ 1
        => hàm sumProb có thể sử dụng để kiểm chứng tổng xác suất của phân bố binamial bằng 1 """
    sum = 0
    for i in range(1, N):
        sum += prob(i, p, N)
    return sum

def approxEntropy(N, p):
    """ Entropy của nguồn binomial với N=100, p=1/2 là 4.369011409223017
        Entropy của nguồn binomial với N=500, p=1/2 là 5.529987244677518 """
    entropy = 0
    for i in range(1, N):
        entropy += prob(i, p, N) * infoMeasure(i, p, N)
    return entropy

print(sumProb(500, 0.3))

print(approxEntropy(100, 0.5))
print(approxEntropy(500, 0.5))