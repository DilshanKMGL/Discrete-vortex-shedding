# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 21:01:34 2019

@author: Lahiru Dilshan
"""

import joukowiski
import plot_fun
import numpy as np

# define circle center
a = 2.0                                   # transfoormation constant
x_cir, y_cir = -0.2, 0.2                # circle center x and y
circle_center = complex(x_cir, y_cir)         # convert center into complex number
r = np.sqrt(y_cir**2 + (a - x_cir)**2)        # calculate the corresponding r
t_step = 0.05 #0.005

# freestream
vel = 5.0 #20.0             # freestream
aoa = 10.0                   # freestream
x_vor, y_vor = x_cir, y_cir # vortex

cir_com_cor = joukowiski.circle(circle_center, a)
jou = joukowiski.get_z(cir_com_cor, a)

plot_fun.plot_aerofoil(jou, [], [], 1)