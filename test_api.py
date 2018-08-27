""" pyWSdemo - test_api """
#make python2 and python3 compatible
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division
####
from api import Api

api = Api()

print( 'test 1: '+ str(api.myFuncOne('hello', 'world')) )                       #dict returned
print( 'test 2: '+ str(api.myFuncTwo()) )                                       #dict returned
