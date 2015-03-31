#!/Users/varunsatrawla/virt3.3/bin/python


### Author: Varun Satrawla (vsatrawla@yahoo.com) - 3/19/2015

# Echo client program
import socket
import json
import sys

# Open clients profile from a json file and fetch record based on client's port
def find_dataset (fname, port):
    with open(fname) as json_data_file:
        data = json.load(json_data_file)
        allrows = data['clients']
        for row in allrows:
            print(row['port'])
            if int(row['port']) == port:
                return ((row['port'], row['Name'], row['datafile']))
        return((0,0,0))

if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: %s <client profile file> <port#>\n" % __file__)
        sys.exit()
    
    val = find_dataset(sys.argv[1], sys.argv[2])
    print(val)
