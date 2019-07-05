# -*- coding: utf-8 -*-
"""
Created on Wed May 15 17:47:00 2019

@author: Lahiru Dilshan
"""
import xlwt
from xlwt import Workbook
import sympy as sp

def create_excel(aoa, circulation, circulation_theoritical):
    # create new workbook
    wb = Workbook()
    sheet1 = wb.add_sheet('Sheet 1') 
    
    sheet1.write(0, 0, 'aoa')
    sheet1.write(0, 1, 'circulation code')
    sheet1.write(0, 2, 'circulation theoritical')    
    sheet1.write(0, 3, 'error')
    
    for i in range(len(aoa)):
        sheet1.write(i+1, 0, aoa[i])
        sheet1.write(i+1, 1, str(circulation[i]))
        sheet1.write(i+1, 2, str(circulation_theoritical[i]))
        
        sheet1.write(i+1, 3, str((circulation[i]-circulation_theoritical[i])/circulation[i]*100))
    
    wb.save('circulation.xls')
    
def write_circulation_with_point(a, point, circulation):
    wb = Workbook()
    sheet1 = wb.add_sheet('Sheet 1') 
    
    sheet1.write(0, 0, 'a')
    sheet1.write(0, 1, 'point')
    sheet1.write(0, 2, 'circulation real')
    sheet1.write(0, 3, 'circulation imaginary')
    sheet1.write(0, 4, 'error')
    
    sheet1.write(1, 0, a)
    for i in range(len(point)):
        sheet1.write(i+1, 1, str(point[i]))
        real = sp.re(circulation[i])
        imaginary = sp.im(circulation[i])
        
        sheet1.write(i+1, 2, str(real))
        sheet1.write(i+1, 3, str(imaginary))
        
        sheet1.write(i+1, 4, str(100- ((abs(real)-abs(imaginary))/abs(real)*100)))
    
    wb.save('circulation error.xls')
    
def write_file(a, circle_center, t_step, vel, aoa, distance, theta, iteration, circulation, strength_vortex, x_vortex_zeta, y_vortex_zeta, x_vortex_z, y_vortex_z, circulation_array):
    heading = 'a '+str(a)+' circle_center '+str(circle_center)+' t_step '+str(t_step)+' vel '+str(vel)+' aoa '+str(aoa)+' distance '+str(distance)+' theta '+str(theta)+'.txt'
    file1 = open(heading,"w") 
    
    file1.write('a\n')
    file1.write(str(a))
    file1.write('\ncircle_center\n')
    file1.write(str(circle_center))
    file1.write('\nt_step\n')
    file1.write(str(t_step))
    file1.write('\nvelocity\n')
    file1.write(str(vel))
    file1.write('\naoa\n')
    file1.write(str(aoa))
    file1.write('\ndistance\n')
    file1.write(str(distance))
    file1.write('\ntheta\n')
    file1.write(str(theta))
    file1.write('\niteration\n')
    file1.write(str(iteration))
    file1.write('\ncirculation\n')
    file1.write(str(circulation))
    file1.write('\nstrength_vortex\n')
    file1.write(str(strength_vortex))
    file1.write('\nx_vortex_zeta\n')
    file1.write(str(x_vortex_zeta))
    file1.write('\ny_vortex_zeta\n')
    file1.write(str(y_vortex_zeta))
    file1.write('\nx_vortex_z\n')
    file1.write(str(x_vortex_z))
    file1.write('\ny_vortex_z\n')
    file1.write(str(y_vortex_z))
    file1.write('\ncirculation_array\n')
    file1.write(str(circulation_array))
    
    file1.close()
    
def write_jou(jou):
    file1 = open("joukowski.txt","w")
    file1.write('x\ty\n')
    x = jou.real
    y = jou.imag
    for i in range(len(x)):
        file1.write(str(x[i])+'\t'+str(y[i])+'\n')
    
    file1.close()