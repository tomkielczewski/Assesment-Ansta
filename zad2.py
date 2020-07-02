# -*- coding: utf-8 -*-
# Podana jest lista zawierająca elementy o wartościach 1-n. Napisz funkcję, która sprawdzi, jakich elementów brakuje:

# 1-n = [1,2,3,4,5,...,10]
# np. n=10
# wejście: [2,3,7,4,9], 10
# wyjście: [1,5,6,8,10]

def missingValues(values, n):
    missingValues = []
    values.sort()
    id = 0
    for i in range(1,n+1):
        if not i in values:
            missingValues.append(i)
    return missingValues
                

l = [2,3,7,4,9]
print(missingValues(l, 10))