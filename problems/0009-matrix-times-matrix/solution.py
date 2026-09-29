def matrixmul(
    a: list[list[int | float]], b: list[list[int | float]]
) -> list[list[int | float]]:
    c = []
    rows = len(a)
    cols = len(b[0])

    for i in range(rows):
        inner = []
        for j in range(cols):
            sum = 0
            for multI in range(len(a[i])):
                if(len(a[i]) != len(b)):
                    return -1
                sum += a[i][multI] * b[multI][j]
            inner.append(sum)
        c.append(inner)
    return c
