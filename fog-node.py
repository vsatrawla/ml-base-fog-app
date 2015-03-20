#!/Users/varunsatrawla/virt3.3/bin/python


### Author: Varun Satrawla (vsatrawla@yahoo.com) - 3/19/2015

# Echo client program
import socket
import time
import numpy as np
import scipy.io
import numpy.matlib as M
import pickle


#read the cross validation dataset
A = scipy.io.loadmat('ex8data1.mat')
Xval = A['Xval']

n=Xval.shape
elems = 0

HOST = 'localhost'
PORT = 50007     #local server port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while (elems<n[0]):
    str = pickle.dumps(Xval[elems,:])
    s.send(str)
    #print 'Received', repr(data)
    elems = elems + 1
    time.sleep(.05)
s.close()
