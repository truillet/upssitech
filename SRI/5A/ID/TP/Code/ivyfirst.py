#!/usr/bin/env/python
# Mon agent ivy en python
from ivy.ivy import IvyServer
    
class MyAgent(IvyServer):
	def __init__(self, name):
        	IvyServer.__init__(self,'MonAgentPython')
        	self.name = name
        	self.start('127.255.255.255:2010')
        	self.bind_msg(self.handle_hello, '^hello (.*)')
        
	def handle_hello(self, agent, arg):
        	print '[Agent %s] GOT hello from %r'%(self.name, agent)
		self.send_msg('Hello Back from %s' %arg)
     

a=MyAgent('HelloBack')
