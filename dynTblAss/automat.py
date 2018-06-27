from flask import Flask,render_template,request
import sqlite3 as sql
app=Flask(__name__)
global dbName

@app.route('/')
def home():
	return render_template('homeAuto.html')

@app.route('/newrec',methods=['POST','GET'])
def newrec():
	if request.method=='POST':
		try:

			dbName=request.form['dbName']
			tableName=request.form['tableName']

			with sql.connect(dbName) as con:
				cur=con.cursor()
				con.execute("Create table "+ tableName +"(name TEXT,addr TEXT,city TEXT,pin TEXT)")
				for i in range(1,5):
					a="gokul"+str(i)
					b="jayanagar"+str(i)
					c="tumkur"+str(i)
					d="57210"+str(i)
					query1="INSERT INTO "+tableName+" (name,addr,city,pin) VALUES('"+a+"','"+b+"','"+c+"','"+d+"')"
					cur.execute(query1)
					con.commit()
				msg="record succesfully added" 
		except:
			con.rollback()
			msg="error in insert operation"
		finally:
			# return render_template("result.html",msg=msg)
			# con=sql.connect(dbName)
			con.row_factory=sql.Row
			cur=con.cursor()
			cur.execute("select * from "+tableName)

			rows=cur.fetchall()
			return render_template("listAuto.html",rows=rows)
			con.close()
	

if __name__=="__main__":
	app.run(debug=True)
