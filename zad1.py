# -*- coding: utf-8 -*-
# Napisz generator kodów pocztowych, który przyjmuje 2 stringi: 
# "79-900" i "80-155" i zwraca listę kodów pomiędzy nimi.
import re

def generateCodesBetween(a, b):
    codesList = []
    begin = int(a[:2])
    end = int(b[:2])
    if begin <= end:
        j=int(a[3:6])
        for i in range(begin, end):
            while j <= 999:
                j += 1
                codesList.append(str(i)+"-"+str(j).zfill(3))
            j=0
        i=end
        for j in range(0, int(b[3:6])):
            codesList.append(str(i)+"-"+str(j).zfill(3))

    #Jeśli pierwszy kod będzie większy od drugiego dalej 
    #moze zwrócić kody między nimi
    else:   
        j=int(b[3:6])
        for i in range(end, begin):
            while j <= 999:
                j += 1
                codesList.append(str(i)+"-"+str(j).zfill(3))
            j=0
        i=begin
        for j in range(0, int(a[3:6])):
            codesList.append(str(i)+"-"+str(j).zfill(3))
    return codesList

print(generateCodesBetween("79-900", "80-155"))


# def fillList(begin, end, sufA, sufB):
#     codesList = []
#     j = sufA
#     for i in range(begin, end):
#         while j <= 999:
#             j += 1
#             codesList.append(str(i)+"-"+str(j).zfill(3))
#         j=0
#         i=end
#         for j in range(0, int(sufB)):
#             codesList.append(str(i)+"-"+str(j).zfill(3))
#     return codesList