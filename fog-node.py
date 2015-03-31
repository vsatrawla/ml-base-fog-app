#!/Users/varunsatrawla/virt3.3/bin/python


### Author: Varun Satrawla (vsatrawla@yahoo.com) - 3/19/2015

# Echo client program
import socket
import time
import numpy as np
import scipy.io
import numpy.matlib as M
import pickle
import sys

if __name__ == "__main__":
    if len(sys.argv) != 6:
        print(sys.argv[0])
        print("\n Usage: %s <gw> <client port#> <sample1> <sample2> <# of samples> \n" % __file__)
        sys.exit()
        

    #read the cross validation dataset
    A = scipy.io.loadmat('ex8data1.mat')
    Xval = A['Xval']

    n=Xval.shape
    elems = 0

    HOST = sys.argv[1]
    REM_PORT = 50007  # hardcode gw port
    LOC_PORT = int(sys.argv[2])     ##TODO: check port ranges

    #TODO: check port ranges
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", LOC_PORT)) # use port specified in the command line

    try:
        s.connect((HOST, REM_PORT))
    except Exception as e:
        print('Error occured %s' % e)
        sys.exit()

    try:
        while (elems< int(sys.argv[5])):
            xval = [sys.argv[3], sys.argv[4]]
            #    str = pickle.dumps(Xval[elems,:])
            str = pickle.dumps(xval)
            s.send(str)
            elems = elems + 1
            time.sleep(.5)

    except socket.error as msg:
       print("An error occurred:", repr(msg))
       sys.exit()
