# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 09:07:47 2019

@author: Lahiru Dilshan
"""
import joukowiski
import vortex
import freestream
import solve_eq
import Excel_write
import derivative
import plot_fun

import numpy as np
import sympy as sp
import time

# calculate time
start = time.time()

# define circle center
a = 0.0375                                   # transfoormation constant
x_cir, y_cir = -0.0025, 0.0025#0.0125                # circle center x and y 
circle_center = complex(x_cir, y_cir)                  # convert center into complex number
r = np.sqrt(y_cir**2 + (a - x_cir)**2)           # calculate the corresponding r
t_step = 0.05

# freestream
vel = 5.0                   # 35.0   # freestream
aoa = 2.0                   # freestream
x_vor, y_vor = x_cir, y_cir # vortex
####

tep_x, tep_y = a, 0.0
x1_z, y1_z = 2*a+ 2*a*0.015, 0.0
zeta1, zeta2 = joukowiski.maptozeta(x1_z, y1_z, a)

strength_vortex = []
x_vortex_zeta = []
y_vortex_zeta = []

x_vortex_z = []
y_vortex_z = []
circulation_array = []

cir_com_cor = joukowiski.circle(circle_center, a)
jou = joukowiski.get_z(cir_com_cor, a)

plot_fun.plot_aerofoil(jou, [], [], 1)

Excel_write.write_jou(jou)
'''
# input value that mentioned in the text file if the simulation is a continued
iteration = 170 
end_condition = 172
print 'iteration', 'circulation','time'
################################################################################

while True:
    
    function = 0
    # get circulation
    function_cir = vortex.create_circulation(circle_center, r)
    function += function_cir
    
    # get vortex
    #### can be modified to get new placement
    vortex_center = zeta1               # vortex center coordinates
    x_vortex_zeta.append(float(sp.re(zeta1)))
    y_vortex_zeta.append(float(sp.im(zeta1)))
    
    x_vortex_z.append(float(x1_z))
    y_vortex_z.append(float(y1_z))
    
    ####
    
    sum_strength = sum(strength_vortex)
    function_vor = vortex.create_vortex(circle_center, vortex_center, sum_strength, r)
    function += function_vor
    
    # create vortex
    for i in range(len(strength_vortex)):
        vortex_center_temp = complex(x_vortex_zeta[i], y_vortex_zeta[i])
        strength = strength_vortex[i]
        function_vor = vortex.get_vortex(circle_center, vortex_center_temp, r, strength)
        function += function_vor
    
    #freestream
    function_freestream = freestream.get_freestream(circle_center, r, vel, aoa)
    function += function_freestream
    
    tep = complex(tep_x, tep_y)
    circulation = sp.re(solve_eq.calculate_circulation(function, tep))
    vortex_strength = - sum_strength - circulation
    strength_vortex.append(float(vortex_strength))
    circulation_array.append(circulation)
    
    vortex_velocity = []
    
    for i in range(len(strength_vortex)):
        function = 0
        for j in range(len(strength_vortex)):
            if i!=j:
                vortex_center_temp = complex(x_vortex_zeta[j],y_vortex_zeta[j])
                strength = strength_vortex[j]
                function += vortex.get_vortex(circle_center, vortex_center_temp, r, strength)
                
        function += vortex.get_circulation(circle_center, r, circulation)
        function += freestream.get_freestream(circle_center, r, vel, aoa)       
        center_point = complex(x_vortex_zeta[i], y_vortex_zeta[i])
        strength = strength_vortex[i]
        
        velocity = solve_eq.calculate_velocity(function, center_point, a, strength)
        vortex_velocity.append(velocity)
        
    ### move the vortex
    for i in range(len(vortex_velocity)):
        new_x = x_vortex_z[i] + float(sp.re(vortex_velocity[i])) * t_step
        new_y = y_vortex_z[i] - float(sp.im(vortex_velocity[i])) * t_step
        
        x_vortex_z[i] = float(new_x)
        y_vortex_z[i] = float(new_y)
        
        zeta1_temp, zeta2_temp = joukowiski.maptozeta(new_x, new_y, a)
        x_vortex_zeta[i] = float(sp.re(zeta1_temp))
        y_vortex_zeta[i] = float(sp.im(zeta1_temp))
    
    
    
    print iteration,'\t',circulation,'\t',time.time()-start,'s'
    
    jou_new = plot_fun.transpose_airfoil(jou, aoa)
    x_vortex_z_rotate, y_vortex_z_rotate = plot_fun.transpose_array(x_vortex_z, y_vortex_z, aoa)    
    
    plot_fun.plot_aerofoil(jou_new, x_vortex_z_rotate, y_vortex_z_rotate, iteration)
    
    iteration += 1
    if iteration >= end_condition:
        break

Excel_write.write_file(iteration, circulation, strength_vortex, x_vortex_zeta, y_vortex_zeta, x_vortex_z, y_vortex_z, circulation_array)
################################################################################

# calculate time
end = time.time()
print 'time:', (end-start), 's'
'''