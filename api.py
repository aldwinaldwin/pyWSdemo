""" pyWSdemo - api """
#make python2 and python3 compatible
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

class Api:
    """ api functions """

    def myFuncOne(self, one, two):
        #always define a dictionary to return
        data = { 'data': None }
        data['data'] = str(one)+' + '+str(two)
        return data

    def myFuncTwo(self):
        data = { 'data': None }
        data['data'] = [ i for i in range(10) ]
        return data
