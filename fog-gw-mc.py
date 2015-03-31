#!/Users/varunsatrawla/virt3.3/bin/python

### Author: Varun Satrawla (vsatrawla@yahoo.com) - 3/25/2015

import socketserver
import socket
import pickle
import time

from learn import mv_gausian_fit
from learn import is_sample_anamalous
from jsonparse import find_dataset 
from restif import start_rest_api


#mv_gausian_fit()

import socket
import threading
import socketserver

class fog_client_handler(socketserver.BaseRequestHandler):

    def handle(self):
        sock=self.request
        
        # Extract source port used by remote client to pull profile
        # from a json file
        #
        (a,p) = sock.getpeername()
        
        ret = mv_gausian_fit(p)
        
        if ret == 0:
            return
        
        while 1:
            self.data = self.request.recv(1024).strip()
            if not self.data: return
            arr = pickle.loads(self.data)
            if is_sample_anamalous(arr, p):
                print('Anamalous sample:', repr(arr))
            else:
                print('Normal sample:', repr(arr))

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

if __name__ == "__main__":
    #start REST api
    #start_rest_api()
    # Port 0 means to select an arbitrary unused port
    HOST, PORT = "localhost", 50007

    server = ThreadedTCPServer((HOST, PORT), fog_client_handler)

    # Start a thread with the server -- that thread will then start one
    # more thread for each request
    server_thread = threading.Thread(target=server.serve_forever)
    # Exit the server thread when the main thread terminates
    server_thread.daemon = True
    server_thread.start()

    #server.serve_forever()
    start_rest_api()
