'''
Created on Jun 29, 2017

@author: jvazquez
'''


class Config(object):
    DEBUG = False
    PORT = 8000


class Development(Config):
    DEBUG = True


class Production(Config):
    DEBUG = False
