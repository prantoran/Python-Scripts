# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 22:14:55 2016

@author: pinku
"""

#testing non-linear objective function
#tutorial: http://apmonitor.com/wiki/index.php/Main/PythonApp

#import APMonitor as apm
from apm import *
import numpy as np
import matplotlib.pyplot as plt
from random import randint

#server
s = 'http://xps.apmonitor.com'
#application name + random number
a = 'demo' + str(randint(2,999))

#clear server
apm(s,a,'clear all')

#load model
apm_load(s,a,'nlp.apm')

#change the solver
#(1=APOPT ,2=BPOPT, 3=IPOPT)
apm_option(s,a,'nlc.solver',3)

#solve
output = apm(s,a,'solve') #send solve command to server
print(output)

#s = server, a = app
#retrieve solution
#(csv,solution) = apm_sol(s,a) #solution is an array
csv_solution = apm_sol(s,a)

print(csv_solution)

#open application root files
apm_web_root(s,a)

#open solution in web browser
apm_web_var(s,a)

##Generate a contour plot

# mesh points for x2 and x4
#x = np.array(1.0,5.0,0.1)
x = np.linspace(1.0,5.0,51)
#y = np.array(1.0,5.0,0.1)
y = np.linspace(1.0,5.0,51)

x2,x4 = np.meshgrid(x,y)

#record fixed optimal values 
x1 = csv_solution['x1']
x3 = csv_solution['x3']

#going to show two variables in contour plots
#objective function:
#minimize x1*x4*(x1+x2+x3) + x3

obj = x1*x4*(x1+x2+x3) + x3

# inequality constrains:
#x1*x2*x3*x4 > 25
ic = x1*x2*x3*x4

#equality constraints:
#x1^2 + x2^2 + x3^2 + x4^2 = 40
eq = np.power(x1,2)+ np.power(x2,2)+ np.power(x3,2)+np.power(x4,2)

#creating contour plot 
plt.figure()
plt.title('NLP Contour Plot')
CS = plt.contour(x2,x4,obj)
plt.clabel(CS) #label of contours
plt.xlabel('x_2')
plt.ylabel('x_3')

#CS = plt.contour(x2,x4,ic,[25.0,26.0,27.0,28.0],colors='b',linewidths=[4.0,3.0,2.0.1.0])
CS = plt.contour(x2,x4,ic,[25.0,26.0,27.0,28.0],colors='b')
plt.clabel(CS,inline=1,fontsize=10)
CS = plt.contour(x2,x4,eq,[40.0],colors='r',linewidths=[4.0])
#[25,..28]=diminishing line widths
plt.clabel(CS,inline=1,fontsize=10)

#don't show legends
#display the plots
plt.show()
