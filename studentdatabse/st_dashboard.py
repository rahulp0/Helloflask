from flask import Flask,render_template,request
import sqlite3 as sql
app=Flask(__name__)

'''
>>import sqlite3
>>> conn=sqlite3.connect('studatabase.db')
>>> conn.execute('CREATE TABLE student(usn TEXT,name TEXT,city TEXT,BrId TEXT,phone TEXT,sem TEXT)')
<sqlite3.Cursor object at 0x0000022C74CDC420>
>>> conn.close()
>>> conn=sqlite3.connect('studatabase.db')
>>> conn.execute('CREATE TABLE branch(br_id TEXT,br_name TEXT)')
<sqlite3.Cursor object at 0x0000022C74CDC650>
>>> conn.close()
>>> exit()
'''

# studatabase.db
@app.route('/')
def home():
    con=sql.connect("studatabase.db")
    con.row_factory=sql.Row
    
    cur=con.cursor()
    cur.execute("select count(*) from student")
    row1=cur.fetchone()
    con.close()
    con=sql.connect("studatabase.db")
    con.row_factory=sql.Row
    
    cur=con.cursor()
    cur.execute("select count(*) from branch")
    row2=cur.fetchone()
    con.close()
    
    
    con=sql.connect("studatabase.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select count(*) as cnt,br_name from student,branch where BrId=br_id group by br_name ")
    res1=cur.fetchall()
    
    #res2=cur.fetchone()
    return render_template('dashboard_home.html',row1=row1[0],row2=row2[0],res1=res1)

@app.route('/enterstudent')
def new_stud():
    return render_template('newstudent.html')

@app.route('/add_stud',methods=['POST','GET'])
def add_stud():
     if(request.method=='POST'):
        try:
            usn=request.form['usn']
            nm=request.form['nm']
            city=request.form['city']
            br_id=request.form['br_id']
            ph=request.form['ph']
            sm=request.form['sm']
            
            with sql.connect("studatabase.db") as con:
                cur=con.cursor()
                cur.execute("INSERT INTO student(usn,name,city,BrId,phone,sem) VALUES(?,?,?,?,?,?)",(usn,nm,city,br_id,ph,sm))
                con.commit()
                msg="Record succesfully added"
        except:
            con.rollback()
            msg="Error inserting the record"
        
        finally:
            return render_template("result.html",msg=msg)
            con.close()

@app.route('/enterbranch')
def new_branch():
    return render_template('newbranch.html')

@app.route('/delete_record',methods=['POST','GET'])
def delete_record():
    if(request.method=='POST'):
        try:
            
            tbname=request.form['tbname']
            val=request.form['val']
            if(tbname=="branch"):
                myid='br_id'
            else:
                myid='usn'
            stmt = 'DELETE FROM '+tbname+' WHERE '+myid+'=?'
            with sql.connect("studatabase.db") as con:
                cur=con.cursor()
                cur.execute(stmt,(val,))
                con.commit()
                msg="Record succesfully deleted"
        except:
            con.rollback()
            msg="Error Deleting the record"
        finally:
            return render_template("result.html",msg=msg)
            con.close()
        
@app.route('/add_branch',methods=['POST','GET'])
def add_branch():
     if(request.method=='POST'):
        try:
            br_id=request.form['br_id']
            br_name=request.form['br_name']
            
            
            with sql.connect("studatabase.db") as con:
                cur=con.cursor()
                
                cur.execute("INSERT INTO branch(br_id,br_name) VALUES(?,?)",(br_id,br_name))
                con.commit()
                msg="Record succesfully added"
        except:
            con.rollback()
            msg="Error inserting the record"
        
        finally:
            return render_template("result.html",msg=msg)
            con.close()


@app.route('/liststud')
def list_stud():
    con=sql.connect("studatabase.db")
    con.row_factory=sql.Row
    
    cur=con.cursor()
    cur.execute("select * from student")
    
    rows=cur.fetchall()
    con.close()
    return render_template("liststud.html",rows=rows)

@app.route('/listbranch')
def list_branch():
    con=sql.connect("studatabase.db")
    con.row_factory=sql.Row
    
    cur=con.cursor()
    cur.execute("select * from branch")
    
    rows=cur.fetchall()
    con.close()
    return render_template("listbr.html",rows=rows)

if(__name__=='__main__'):
    app.run(debug=True)