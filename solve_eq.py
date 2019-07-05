# -*- coding: utf-8 -*-
"""
Created on Wed May 15 23:57:24 2019

@author: Lahiru Dilshan
"""
import sympy as sp
import derivative

def calculate_circulation(function, tev_edge):
    zeta, vor1 = sp.symbols('zeta, vor1',real=False) 
    function = sp.diff(function,zeta)
    function = function.subs([(zeta,tev_edge)])
    answer = list(sp.solveset(function).evalf())[0]
    return answer

def calculate_velocity(function, center_point, a, strength):
    zeta = sp.symbols('zeta',real=False)
    function = sp.diff(function, zeta) * derivative.first_derivative(a)
    function -= 1j * strength / (4 * sp.pi) * derivative.second_derivative(a) / derivative.first_derivative(a)
    #print 'function before',function
    function = function.evalf()
    function = function.subs([(zeta, center_point)])
    #print 'function after',function
    answer = function.evalf()
    return answer
    