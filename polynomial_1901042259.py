def horner(pol, size, x):
    result = pol[0]
    for i in range(1, n):
        result = result * x + pol[i]
    return result


polynom = [2, -3, 2, 1, 4, 12]
x = 1
print("Value of polynomial is", horner(polynom, len(polynom), x))