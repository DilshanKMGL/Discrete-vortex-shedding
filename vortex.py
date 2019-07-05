# -*- coding: utf-8 -*-
"""
Created on Wed May 15 22:54:43 2019

@author: Lahiru Dilshan
"""

import sympy as sp

def create_circulation(circle_center, r):
    zeta, vor1 = sp.symbols('zeta, vor1',real=False)
    function1 = -1j * vor1 * sp.log(zeta - circle_center) / (2*sp.pi)
    #function2 = 1j * vor1 * sp.log((r**2 / (zeta - circle_center)) - circle_center) / (2*sp.pi)
    return function1

def get_circulation(circle_center, r, strength):
    zeta = sp.symbols('zeta',real=False)
    function1 = -1j * strength * sp.log(zeta - circle_center) / (2*sp.pi)
    return function1

def create_vortex(circle_center, vortex_center, sum_strength, r):
    zeta, vor1 = sp.symbols('zeta, vor1', real=False)
    function1 = -1j * (- sum_strength - vor1) * sp.log(zeta - vortex_center) / (2*sp.pi)
    function2 = 1j * (- sum_strength - vor1) * sp.log((r**2 / (zeta - circle_center)) - vortex_center) / (2*sp.pi)
    function = function1 + function2
    return function
    
def get_vortex(circle_center, vortex_center, r, strength):
    zeta = sp.symbols('zeta', real=False)
    function1 = -1j * strength * sp.log(zeta - vortex_center) / (2*sp.pi)
    function2 = 1j * strength * sp.log((r**2 / (zeta - circle_center)) - vortex_center) / (2*sp.pi)
    function = function1 + function2
    return function


