# -*- coding: utf-8 -*-
# Napisz generator kodów pocztowych, który przyjmuje 2 stringi: 
# "79-900" i "80-155" i zwraca listę kodów pomiędzy nimi.
import re
def getBetween(a, b):
    codesList = []
    begin = int(a[:2])
    end = int(b[:2])
    j=int(a[3:6])
    for i in range(begin, end):
        while j <= 999:

            codesList.append(str(i)+"-"+str(j).zfill(3))
            j += 1
        j=0
    i=end
    for j in range(0, int(b[3:6])):
        codesList.append(str(i)+"-"+str(j).zfill(3))
    return codesList

print('wynik: ')
print(getBetween("79-900", "80-155"))
