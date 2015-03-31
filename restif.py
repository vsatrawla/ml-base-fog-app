#!/Users/varunsatrawla/virt3.3/bin/python

### Author: Varun Satrawla (vsatrawla@yahoo.com) - 3/25/2015

from bottle import route, run
from learn import print_client_info
import json
from dicttoxml import dicttoxml

@route('/')
@route('/clients')
def hello():
    #st = repr(print_client_info())
    xml = dicttoxml(print_client_info())

    return(xml)
    #st = json.dumps(print_client_info(), ensure_ascii=False)
    #return(str(st))
   
def start_rest_api():
    run(host='localhost', port=8080, debug=True)

