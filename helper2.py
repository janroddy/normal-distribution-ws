import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm


x_min = -5.0
x_max = 5.0

#z represents a variable following a standard normal distribution
#here we assign a variable z's value to 2.00. STUDENT PART: Add 2.00 after the "z =" ------------
z = 2.0

mean = 0 
std_dev = 1.0

#calculate the proportion with the normalcdf function
proportion = norm.cdf(z,mean,std_dev) 
#output proportion to the console 
print ( "The proportion that is less than z = "+ str(z) + " is approximatley " + str( round(proportion, 4) ) )
print ("The proportion that is less than z = % %.4f" % z_score)

# Plots normal distribution curve
x = np.linspace(x_min, x_max, 200) 
y = norm.pdf(x, mean, std_dev)
plt.plot(x,y, color='purple')
plt.grid()
plt.xlim(x_min,x_max)
plt.ylim(0,.5)


# Shades the portion of the plot under the curve 
start_pt = x_min
end_pt = z

plt.plot([start_pt ,start_pt ],[0.0,norm.pdf(start_pt, mean, std_dev)], color='purple')
plt.plot([end_pt ,end_pt ],[0.0,norm.pdf(end_pt, mean, std_dev)], color='purple')

ptx = np.linspace(start_pt, end_pt, 200)
pty = norm.pdf(ptx,mean,std_dev)

plt.fill_between(ptx, pty, color='purple', alpha='1.0')
plt.rcParams['figure.figsize'] = [10, 5]
plt.show()