# -*- coding: utf-8 -*-
# Napisz generator kodów pocztowych, który przyjmuje 2 stringi: 
# "79-900" i "80-155" i zwraca listę kodów pomiędzy nimi.
import re
def fillList(a, b, s1, s2):
    codes = []
    j = s1
    for i in range(a, b):
            while j <= 999:
                j += 1
                codes.append(str(i)+"-"+str(j).zfill(3))
            j=0
    i = b
    for j in range(0, int(s2)):
        codes.append(str(i)+"-"+str(j).zfill(3))
    return codes

def generateCodesBetween(a, b):
    codesList = []
    begin = int(a[:2])
    end = int(b[:2])
    suf1 = int(a[3:6])
    suf2 = int(b[3:6])
    if begin <= end:
        codesList = fillList(begin, end, suf1, suf2)
    #Jeśli pierwszy kod będzie większy od drugiego dalej 
    #moze zwrócić kody między nimi
    else:   
        codesList = fillList(end, begin, suf2, suf1)

    return codesList

print(generateCodesBetween("79-900", "78-155"))