#Authors: Daniel Duong and Long Nguyen

'''pi will be 3.14, e will be 2.718'''
e = 2.7182818284590452353602874713527
pi = 3.14159265359

import math
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
# Generate the values of the RV X

def normalDistrib(x, mean, sigma):
 exponentEquation = -(pow((x - mean), 2) / (2 * sigma * sigma))
 probNormal = (1 / (sigma * math.sqrt(2 * pi))) * (pow(e, exponentEquation))
 #print(probNormal)
 #print(type(probNormal))
 return probNormal


N=100000; nbooks=5; a=1; b=3;
mu_x=(a+b)/2 ; sig_x=np.sqrt((b-a)**2/12) #calculated the thickness of one book, mean and std dev of one book
X=np.zeros((N,1)) #numpy array returning an array of zeros
print("X is: ", X)
print("X has ",np.size(X), " elements")
sumofBigX = [] #we did a list to copy the big X's np array's value to work around the np array

for k in range(0,N): #100000 experiments
 x=np.random.uniform(a,b,nbooks) #generates books with random thicknesses within the range from 1 to 3 inclusively
 #print("size of little x is: ", np.size(x))
 #print("little x is: ", x)
 w=np.sum(x) #w is the sum of all thicknesses of the books
 #print("w is: ", w)
 X[k]=w #populates the values of thicknesses of one experiment into an numpy array
 sumofBigX.append(w)
 #X is the summation of the little x
 #print("Type of Big X is: ", type(X))
 #print("Big X is: ", X)
 #print("Big X size is: ", np.size(X))
# Create bins and histogram
nbins = 30; # Number of bins, the number of bars you will graph between the first and second parameters of bins
edgecolor='w'; # Color separating bars in the bargraph
#
bins=[float(x) for x in np.linspace(nbooks*a, nbooks*b,nbins+1)] #generating graph bars
#print("bins: ", bins)
h1, bin_edges = np.histogram(X,bins,density=True) #h1 is the array of probability of each thickess, bin_edges is the x label of the bar graph
#print("h1 is : ", h1)
#print("bin edges is: ", bin_edges)
# Define points on the horizontal axis
be1=bin_edges[0:np.size(bin_edges)-1] #the left side of each graph bar
print("be1 is: ", be1)
print("size of be1 is: ", np.size(be1))
be2=bin_edges[1:np.size(bin_edges)] #the right side of each graph bar
print("be2 is: ", be2)
print("size of be2 is: ", np.size(be2))
b1=(be1+be2)/2 #class mark of bin edges 1 and 2
print("b1 is: ", b1)
barwidth=b1[1]-b1[0] # Width of bars in the bar graph, subtract the 1st index of b1 by the 0th index of b1
#print("b1[1] is", b1[1])
#print("b1[0] is", b1[0])
#print("barwidth is: ", barwidth)
plt.close('all')
# PLOT THE BAR GRAPH
fig1=plt.figure(1)
plt.bar(b1,h1, width=barwidth, edgecolor=edgecolor)
#PLOT THE GAUSSIAN FUNCTION

'''print("sumOfBigX[0] is: ", sumofBigX[0])
print("X[0] is: ", X[0])

if(sumofBigX[0] == X[0]):
  print("copied successfully")

else:
 print("some error")'''


yValues = []
meanList = [2, 10, 30]
sigmaList = [0.577, 1.290, 2.235]

#test = normalDistrib(X[0], meanList[0], sigmaList[0])
#print("test is: ", test)

for l in range(0, N):
  yValues.append(normalDistrib(sumofBigX[l], meanList[0], sigmaList[0]))

print("yValues is: ", yValues)

def gaussian(mu,sig,z):
 f=np.exp(-(z-mu)**2/(2*sig**2))/(sig*np.sqrt(2*np.pi))
 return f

f=gaussian(mu_x*nbooks,sig_x*np.sqrt(nbooks),b1)
plt.plot(b1,f,'r')
#plt.plot(sumofBigX, yValues, 'm')

fig2 = plt.figure(2)
plt.plot(sumofBigX, yValues, 'm')

plt.show()