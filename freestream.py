# -*- coding: utf-8 -*-
"""
Created on Wed May 15 23:42:37 2019

@author: Lahiru Dilshan
"""

import sympy as sp

def get_freestream(circle_center, r, vel, aoa):
    aoa = sp.rad(aoa)
    zeta = sp.symbols('zeta',real=False)
    function1 = vel * zeta * (sp.cos(aoa) - 1j * sp.sin(aoa))
    function2 = vel * (r**2 / (zeta - circle_center)) * (sp.cos(aoa) + 1j * sp.sin(aoa))
    return function1+function2
