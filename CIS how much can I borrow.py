# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 17:38:15 2023

@author: rfranco11


Pmt = r * PV/(1-(1+r)**-n)
Pmt is how much you pay back/mo
n is number of months
r is interest rate per month 
n is number of months
"""


def computesPmt(PV, r, n):
    
    """
    
    Parameters 
    ----------
    PV : TYPE Float
    DESCRIPTION, Present value (amt borrow)
    r : TYPE Float 
    DESCRIPTION, Interest rate APR
    n: TYPE Integer
    DESCRIPTION, Number of months to pay back loan 
    
    Returns
    -------
    Pmt : TYPE Float
    DESCRIPTION, amt paid per month 
    
   """
    
    Pmt =  r * PV/(1-(1+r)**-n)
    return Pmt 

def computesPV (Pmt, r, n):
    """
    Parameters
    ----------
    Pmt : TYPE float
        DESCRIPTION. how much I can afford for monthly payment
        
    r : TYPE float
        DESCRIPTION. interest rate APR
        
    n : TYPE integer
        DESCRIPTION. number of months 
        
    Returns
    -------
    PV: Type float 
        DESCRIPTION, amount of $$ I can afford to borrow
    formula:
    Pv = (1-(1+r)**(-n) *Pmt/r)
    """
   
    r = r/100
    r = r/12
    
    PV = (1-(1+r)**(-n)) * Pmt/r
    return PV

#input the pv
import numpy as np

while(True):
    choice = int(input('enter choice 1 for PV, 2 for Pmt -> '))
    if(choice == 1 or choice ==2):
       break
    else:
        print(f"enter a 1 or a 2, you entered {choice}")

if choice == 2:    
    PV = input('enter PV: ')
    PV = float(PV)
    #equivalently PV = float(input('enter PV: '))
    print(f"PV = {PV} \n")

    r = input ('interest APR: ')
    r = float(r)/100
    r = r/12
    print(f"interest = {r: 0.3f}")

    n = int(input('how many months: '))
    print(f"\nn = {n} months: ")

    Pmt = computesPmt(PV, r, n)
    Pmt = np.round(Pmt, 2)
    print(f"payment is {Pmt: } per month ")

if choice == 1:
    Pmt = input('enter Pmt: ')
    Pmt = float(Pmt)
    print(f"Pmt = {Pmt} \n")
    
    r = input('interest APR: ')
    r = float(r)/100
    r = r/12
    
    n = int(input('number of months: '))
    print(f"\mm = {n} months")

PV = computesPV(85.61, 5, 12 )
print(PV)