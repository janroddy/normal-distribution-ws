import matplotlib.pyplot as plt
import scipy.stats
import numpy as np
from scipy.stats import norm
#STUDENT PART

x_min = 55
x_max = 85
#z represents a variable folllowing a standard normal distribution 
#(This could be a part the student fills in with a disucssion of parameters and functions)
z_score = 4.33
cato = 83.0 #do we use this 
#STUDENT PART  
mean = 70.0 
std_dev = 3.0

#calculate the proportion here 
prop_lower = norm.cdf(z_score,0,1) 
proportion =  1 - prop_lower

#output probability  to the console 
print ( "The proportion of men taller than Cato is  "+ str( proportion ) )


x = np.linspace(x_min, x_max, 200)
y = norm.pdf(x, mean, std_dev)
plt.plot(x,y, color='purple')

plt.grid()
plt.xlim(x_min,x_max)
plt.ylim(0,.15)
#----------------------------------------------------------------------------------------#
# SHADE AREA 
pt1 = 83
pt2 = x_max

plt.plot([pt1 ,pt1 ],[0.0,scipy.stats.norm.pdf(pt1 ,mean, std_dev)], color='purple')
plt.plot([pt2 ,pt2 ],[0.0,scipy.stats.norm.pdf(pt2 ,mean, std_dev)], color='purple')

ptx = np.linspace(pt1, pt2, 25)
pty = scipy.stats.norm.pdf(ptx,mean,std_dev)

plt.fill_between(ptx, pty, color='purple', alpha='1.0')
#---------------------------------------------------------------------------------------#
plt.rcParams['figure.figsize'] = [10, 5]
plt.title('Normal Distribution Curve',fontsize=14)

plt.show()