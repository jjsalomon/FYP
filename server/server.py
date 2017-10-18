import flask
import os
import pandas as pd
import numpy as pd


class Server(flask.Flask):
	def __init__(self,import_name):
		super(Server,self).__init__(import_name)
		self.route("/")(self.index)
		
	def index(self):
		try:
			return flask.render_template('index.html')
		except Exception as e:
			return flask.render_template('error.html', errormsg = e)
			
			
app = Server(__name__)

if __name__ == '__main__':
	app.run()