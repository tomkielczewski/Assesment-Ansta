# -*- coding: utf-8 -*-
#NALEŻY WYGENEROWAĆ LISTĘ LICZB OD 2 DO 5.5 ZE SKOKIEM CO 0.5, 
#DANE WYNIKOWE MUSZĄ BYĆ TYPU DECIMAL.
#2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5
from decimal import *
miltiplier = 0.5
def generateDigits(begin, end):
    digitsList = []
    begin = int (begin / miltiplier)
    end = int (end / miltiplier)
    for i in range(begin, end):
        digitsList.append(Decimal(i * miltiplier))
        i += miltiplier
    return digitsList

print(generateDigits(2, 5.5))