from flask import Flask,redirect,url_for
app = Flask(__name__)

@app.route('/')
def hello_world():
	return ' Hello World'

@app.route('/hi/<name>')
def say_hi(name):
	return 'Hello, %s'%(name)

@app.route('/age/<int:age>')
def show_age(age):
	return 'Age is %d'%(age)

@app.route('/admin/')
def hello_admin():
	return 'Hello from the other side'

@app.route('/guest/<guest>')
def hello_guest(guest):
	return 'Hello %s as Guest' %guest

@app.route('/user/<name>')
def hello_user(name):
	if name == 'admin':
		return redirect(url_for('hello_admin'))
	else:
		return redirect(url_for('hello_guest',guest=name))

if __name__=='__main__':
	app.run()
