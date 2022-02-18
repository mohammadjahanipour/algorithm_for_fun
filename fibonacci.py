def Fib(l):
    y = [0, 1]
    for i in range(1, 1000):
        if i == 1:
            y[i] = 1
            b = [1]
            y.extend(b)
        elif i > 1:
            y[i] = y[i-1]+y[i-2]
            b = [y[i]]
            y.extend(b)

    n = y[l]
    return print(n)


l = int(input("type"))
Fib(l)
