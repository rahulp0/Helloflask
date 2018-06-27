from flask import Flask,redirect,url_for
app = Flask(__name__)

@app.route('/gtest/<int:n1>/<int:n2>')
def gtest(n1,n2):
	if n1>n2:
		return '%s is greater than %s' %(str(n1),str(n2))
	elif n1<n2:
		return '%s is greater than %s' %(str(n2),str(n1))
	else:
		return '%s is equal to %s' %(str(n1),str(n2))

@app.route('/sumOll/<int:n1>/<int:n2>')
def gtestAmong(n1,n2):
	n=n1+n2
	return '%s + %s  = %s' %(str(n1),str(n2),str(n))
	
if __name__=='__main__':
	app.run(debug=True)
