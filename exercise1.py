#!/usr/bin/env python

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

This module prints the amount of money that Lakshmi has remaining
after the stock transactions

"""

__author__ = 'Mib_Ani'
share_count=2000
buy_value=900
total_investment=(share_count*buy_value)*1.03
sell_value=942.75
total_sold_amount=(share_count*sell_value)*.97
money = total_sold_amount-total_investment
if money > 0:
    print 'Lakshmi is having Profit'
else:
    print 'Lakshmi is having Loss'
print(money)
