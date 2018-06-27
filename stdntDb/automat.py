from flask import Flask,render_template,request
import sqlite3 as sql
import sqlite3
app=Flask(__name__)
global dbName

@app.route('/')
def home():
	con=sql.connect("students_of_branch.db")
	cur=con.cursor()
	cur.execute("select count(*) from stdntDtls")
	tot=cur.fetchall()
	tot=tot[0][0]

	#con.row_factory=sql.Row

	#con.commit()
	cur.close()
	con.close()
	return render_template('homeAuto.html',tot=tot)


@app.route('/stdntDtls')
def stdntDtls():
	con=sql.connect("students_of_branch.db")
	con.row_factory=sql.Row
	cur=con.cursor()
	cur.execute("select * from stdntDtls")
	rows=cur.fetchall()
	con.close()
#	cur.close()
	return render_template("stdntDtls.html",rows=rows)
	cur.close()

	#return render_template('stdntDtls.html')


@app.route('/stdntDtls/<sid>')#methods=['POST','GET'])
def rfrsh(sid):
	withSid=sid
	return withSid
			#tableName=request.form['tabl']
"""
	con1=sqlite3.connect("students_of_branch.db")
	con1.row_factory=sql.Row

	cur1=con1.cursor()
	quer="DELETE FROM stdntDtls WHERE sid="+str(withSid) 
	cur1.execute(quer)
	msg="record succesfully removed"
	print(msg)
	con1.commit() 
	cur1.close()
	con1.close()
		
			# return render_template("result.html",msg=msg)
			# con=sql.connect(dbName)
	con=sql.connect("students_of_branch.db")
	con.row_factory=sql.Row
	cur=con.cursor()
	cur.execute("select * from stdntDtls")
	rows=cur.fetchall()
	return render_template("stdntDtls.html",rows=rows)
	con.close()
	cur.close()
"""


if __name__=="__main__":
	app.run(debug=True)






















