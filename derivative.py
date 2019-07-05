# -*- coding: utf-8 -*-
"""
Created on Thu May 16 11:46:28 2019

@author: Lahiru Dilshan
"""
import sympy as sp

def first_derivative(a):
    zeta = sp.symbols('zeta',real=False)
    derivative_1 = 1 / (1 - (a**2/zeta**2))
    return derivative_1

def second_derivative(a):
    zeta = sp.symbols('zeta',real=False)
    derivative_2 = (-2*a**2) / (zeta**3) / (1 - (a**2/zeta**2))**3
    return derivative_2