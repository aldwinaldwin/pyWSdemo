""" pyWSdemo - ws """
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division
####
from pycnic.core import WSGI, Handler
####
from api import Api

api = Api()

class RootRoute(Handler):
    """ / """
    def get(self):
        """ GET / """
        return { 'empty': ' as my mind' }

class funcOneRoute(Handler):
    """ /funcOne/ """
    def get(self, params):
        """ GET /funcOne/{one}/{two} """
        paramLst = params.split('/')
        if len(paramLst)==2:
            return api.myFuncOne( paramLst[0], paramLst[1] )
        else:
            return { 'error': 'wrong amount of parameters' }

    def post(self):
        """ POST /functOne   parameters: paramOne, paramTwo """
        paramOne = self.request.data.get('paramOne','hi')
        paramTwo = self.request.data.get('paramTwo','you')
        return api.myFuncOne( paramOne, paramTwo )

class funcTwoRoute(Handler):
    """ /funcTwo """
    def get(self):
        return api.myFuncTwo()      #example without parameters needed

class App(WSGI):
    """ pycnic app - routes """
    headers = [("Access-Control-Allow-Origin", "*")]
    routes = [('/', RootRoute()),
            ('/funcOne/(.*)', funcOneRoute()),                                  #funcOne GET
            ('/funcOne', funcOneRoute()),                                       #funcOne POST
            ('/funcTwo', funcTwoRoute()),                                       #funcTwo GET
            ]
