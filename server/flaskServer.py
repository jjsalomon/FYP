import flask
from modelManager import UnetModel
class Server(flask.Flask):
	def __init__(self,import_name):
		super(Server,self).__init__(import_name)
		# Set up routes
		self.route("/")(self.index)
		self.route("/uploaded",methods=['GET','POST'])(self.uploadScan)
		self.ctScans = None
		# Load Unet Model
		self.unetModel = UnetModel()
	
	# index.html
	def index(self):
		try:
			return flask.render_template('index.html')
		except Exception as e:
			return flask.render_template('error.html', errormsg = e)
			
	# upload scan
	def uploadScan(self):
		try:
			if request.method == 'POST':
				self.ctScans = request.files['file']
				return flask.render_template('success.html')
		except Exception as e:
			return flask.render_template('error.html',errormsg=e)
			
	# preprocess and infer the data to the model
	def predictData(self):
		try:
			processedData = self.unetModel.preprocess(self.ctScans)
			results = self.unetModel.predict(processedData)
			return flask.render_template('results.html',results)
		except Exception as e:
			return flask.render_template('error.html',errormsg=e)
app = Server(__name__)

if __name__ == '__main__':
	app.run(debug=True)
	