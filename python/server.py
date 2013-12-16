from bottle import Bottle, run, static_file, redirect, request, template
import smtplib
from email.mime.text import MIMEText

app = Bottle()

@app.route('/')
def index():
	redirect('/index.html')

@app.route('/sendform',method="GET")
def sendformGet():
	redirect('/index.html')

@app.route('/sendform',method="POST")
def sendform():
	print request.POST.get('name.first')


	# Import the email modules we'll need


	# Open a plain text file for reading.  For this example, assume that
	# the text file contains only ASCII characters.
	# Create a text/plain message
	msg = MIMEText("TEST")

	me = request.POST.get('email')
	you = "peter.somhorst@gmail.com"
	msg['Subject'] = 'Dit is een testmail'
	msg['From'] = me
	msg['To'] = you

	# Send the message via our own SMTP server, but don't include the
	# envelope header.
	s = smtplib.SMTP('localhost')
	s.sendmail(me, [you], msg.as_string())
	s.quit()



@app.route('/<filepath:path>')
def server_static(filepath):
		return static_file(filepath, root="/home/flux/website/front")

run(app,host='localhost', port=8080, debug=True)