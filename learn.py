#!/Users/varunsatrawla/virt3.3/bin/python


### Author: Varun Satrawla (vsatrawla@yahoo.com) - 3/19/2015

import numpy as np
import scipy.io
import matplotlib.pyplot as plt
import matplotlib.font_manager
import math
from jsonparse import find_dataset 
from scipy.stats import multivariate_normal

import numpy.matlib as M
client_info = {}

def plotgraph (Xval):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    x = Xval[:,0]
    y = Xval[:,1]

    plt.xlabel('Latency (ms)');
    plt.ylabel('Throughput (mb/s)');

    ax.scatter(x, y)
    plt.show()
    return

def mvpdf (x, mu, sigma):
    # Just use the library functions. It's too arduous to implement
    # your own.
    #
    p = multivariate_normal.pdf(x, mu, sigma);
    return p

def select_epsilon ():
    #
    # based on heuristics for this dataset.
    # This can and should be learned from the dateset itself
    #
    return (8.99/100000)

#
# Reads dataset and fits it to multivariate gaussian distribution
# and saves mu and sigma in global variable for efficiency
#
def mv_gausian_fit (portno):
    global client_info
    
    (port,name,fname) = find_dataset('clients.js', portno)
        
    if port == 0:
        print("No data set found for this client %s\n" % portno)
        return 0
    
    A = scipy.io.loadmat(fname)    
    print("Using %s for this client\n" % fname)
    
    Xval = A['Xval']
    Yval = A['yval']
    X=A['X']
 
    mu = np.mean(X, axis=0)
    sigma = np.std(X, axis=0)
    sigma = sigma**2
    
    print_client_info()
    
    n=Xval.shape
    elems = 0

    epsilon = select_epsilon()

    client_info[port] = (mu,sigma, epsilon)
    
    print_client_info()
    
    return

def print_client_info():
    global client_info
    return (client_info)
    

def is_sample_anamalous (X, p):
    global client_info

    # add error statements
    
    mu = client_info[str(p)][0]
    sigma = client_info[str(p)][1]
    epsilon = client_info[str(p)][2]
    
    # Find probability based on learned parms (vectors)
    pb = mvpdf(X, mu, sigma)

    if pb < epsilon:
        return(1)

    return(0)
   
def main():
    global mu
    global sigma
    #load dataset from matlab formatted file 
    global A
    

main()
