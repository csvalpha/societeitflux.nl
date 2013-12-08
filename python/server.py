from bottle import Bottle, run, static_file, redirect, request

app = Bottle()

@app.route('/')
def index():
	redirect('/index.html')

@app.route('/sendform',method="POST")
def sendform():
	print request.forms.get('addressStreet')

@app.route('/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root="../")

run(app,host='vivaan.csvalpha.nl', port=8080, debug=True)