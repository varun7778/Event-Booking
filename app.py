from flask import Flask,request,render_template,flash,redirect,url_for
import mysql.connector
app = Flask(__name__)
app.secret_key = 'my unobvious secret key'
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="varunasd1",
  database="work"
) 
x=0
bid=0
ename=" "
cursor = mydb.cursor(buffered=True)
@app.route('/')
def showcase():
        return render_template('index.html')

@app.route('/login')
def login():
        return render_template('login.html')

@app.route('/Wazza')
def Wazzaa():
        return "Hello World"

@app.route('/something', methods=['GET','POST'])
def something():
  if request.method == "POST":
    email=request.form['email']
    username=request.form['username']
    password=request.form['password']
    sql1 = "select max(id)+1 from suser;"
    cursor.execute(sql1)
    data1=cursor.fetchall()
    idd=data1[0][0]
    sql2 = "select * from suser where username = '%s';"%username
    cursor.execute(sql2)
    data2=cursor.fetchall()
    print(x)
    if len(data2)!=0:
      return render_template('register.html',error="User aready exists!")
    else:
      print('registering')
      sql3="insert into suser values (%s,'%s','%s','%s');"%(idd,username,email,password)
      cursor.execute(sql3)
      mydb.commit()
      return render_template('login.html')
  return render_template('register.html')

@app.route('/anything',methods=['GET','POST'])
def anything(): 
  if request.method=="POST":
    global ename
    ename = request.form['ename']
  return render_template('building.html')

@app.route('/notspl',methods=['GET','POST'])
def notspl():
  if request.method == "POST":
    i1=request.form['item1']
    i2=request.form['item2']
    i3=request.form['item3']
    sql1="call p1(%s,%s,%s,%s,@a)"%(i1,i2,i3,x)
    cursor.execute(sql1)
    return render_template('status.html')

@app.route('/AB1',methods=['GET','POST'])
def AB1():
  global x
  global ename
  global bid
  '''
  sql1 = "select max(booking_id)+1 from suser;"
  cursor.execute(sql1)
  data1=cursor.fetchone()
  idd=data1[0]
  bid='AB1'
  sql2="call p2(%s,%s,%s,%s,@a);"%(bid,idd,x,ename)
  cursor.execute(sql2);
  '''
  sql1 = "select max(booking_id)+1 from booking;"
  cursor.execute(sql1)
  data1=cursor.fetchone()
  idd=data1[0]
  bid=idd
  sql2="select * from room where building = 'AB1' and status =0;"
  cursor.execute(sql2)
  data2=cursor.fetchone()
  roomidd=data2[0]
  sql3 = "insert into booking values(%s,%s,%s,'%s');"%(idd,roomidd,x,ename)
  cursor.execute(sql3)
  mydb.commit()
  return render_template('perm.html')

@app.route('/AB2',methods=['GET','POST'])
def AB2():
  global x
  global ename
  global bid
  '''
  sql1 = "select max(booking_id)+1 from suser;"
  cursor.execute(sql1)
  data1=cursor.fetchone()
  idd=data1[0]
  bid='AB2'
  sql2="call p2(%s,%s,%s,%s,@a);"%(bid,idd,x,ename)
  cursor.execute(sql2);
  '''
  sql1 = "select max(booking_id)+1 from booking;"
  cursor.execute(sql1)
  data1=cursor.fetchone()
  idd=data1[0]
  bid=idd
  sql2="select * from room where building = 'AB2' and status =0;"
  cursor.execute(sql2)
  data2=cursor.fetchone()
  roomidd=data2[0]
  sql3 = "insert into booking values(%s,%s,%s,'%s');"%(idd,roomidd,x,ename)
  cursor.execute(sql3)
  mydb.commit()
  return render_template('perm.html')

@app.route('/AB4',methods=['GET','POST'])
def AB4():
  global x
  global ename
  global bid
  '''
  sql1 = "select max(booking_id)+1 from suser;"
  cursor.execute(sql1)
  data1=cursor.fetchone()
  idd=data1[0]
  bid='AB4'
  sql2="call p2(%s,%s,%s,%s,@a);"%(bid,idd,x,ename)
  cursor.execute(sql2);
  '''
  sql1 = "select max(booking_id)+1 from booking;"
  cursor.execute(sql1)
  data1=cursor.fetchone()
  idd=data1[0]
  bid=idd
  sql2="select * from room where building = 'AB4' and status =0;"
  cursor.execute(sql2)
  data2=cursor.fetchone()
  roomidd=data2[0]
  sql3 = "insert into booking values(%s,%s,%s,'%s');"%(idd,roomidd,x,ename)
  cursor.execute(sql3)
  mydb.commit()
  return render_template('perm.html')

@app.route('/AB5',methods=['GET','POST'])
def AB5():
  global x
  global ename
  global bid
  '''
  sql1 = "select max(booking_id)+1 from suser;"
  cursor.execute(sql1)
  data1=cursor.fetchone()
  idd=data1[0]
  bid='AB5'
  sql2="call p2(%s,%s,%s,%s,@a);"%(bid,idd,x,ename)
  cursor.execute(sql2);
  '''
  sql1 = "select max(booking_id)+1 from booking;"
  cursor.execute(sql1)
  data1=cursor.fetchone()
  idd=data1[0]
  bid=idd
  sql2="select * from room where building = 'AB5' and status =0;"
  cursor.execute(sql2)
  data2=cursor.fetchone()
  roomidd=data2[0]
  sql3 = "insert into booking values(%s,%s,%s,'%s');"%(idd,roomidd,x,ename)
  cursor.execute(sql3)
  mydb.commit()
  return render_template('perm.html')


@app.route('/reque',methods=['GET','POST'])
def reque():
  if request.method=="POST":
        global x
        name=request.form['name']
        subject=request.form['subject']
        sql1 = "select max(splreq_id)+1 from splreq;"
        cursor.execute(sql1)
        data1=cursor.fetchall()
        idd=data1[0][0]
        sql2 = "select * from splreq where id =%s;"%x
        cursor.execute(sql2)
        data2=cursor.fetchall()
        if len(data2)>=3:
            return render_template('register.html')
        else:
            sql3="insert into splreq values (%s,'%s','%s',%s);"%(idd,name,subject,x)
            cursor.execute(sql3)
            mydb.commit()
            return render_template('status.html')


@app.route('/landing', methods=['GET','POST'] )
def land():
        res = ""
        t=0
        if request.method == "POST":
           username =request.form["username"]
           passw = request.form["password"]
           sql='SELECT username,password FROM suser'
           cursor.execute(sql)
           rs = cursor.fetchall()
           for row in rs:
                        if username == row[0] and passw == row[1]:
                                t=1
                                break
        if t == 0:
           flash('Invalid user credentials')
           return render_template('login.html')
        else:
           sql1="SELECT * FROM suser where username= '%s';"%username
           cursor.execute(sql1)
           rs = cursor.fetchall()
           global x 
           x = rs[0][0]
           flash(username)
           return render_template('user_home.html')

#@app.route('/spec_requests',methods=['GET','POST'])
#def spec_requests():
#       if request.method=='GET'
        # put all the results you get back from the table onto a variable(set) called "reqs"
#       return render_template('admin_home.html',see_req=reqs)

#@app.route('/see_perm',methods=['GET','POST'])
#def see_perm():
##      return render_templte('admin_perm.html',see_perm=nightperm              

@app.route('/permi',methods=['GET','POST'])
def permi():
  global bid
  global x
  if request.method=="POST":
    name=request.form["name"]
    email = request.form["email"]
    time = request.form["time"]
    message = request.form["message"]
    date = request.form["Date"]
    date1 = request.form["Date1"]
    sql1 = "select max(perm_id)+1 from perms;"
    cursor.execute(sql1)
    data1=cursor.fetchone()
    idd=data1[0]
    print(idd)
    x1 = message.split(",")
    print(x1)
    print(bid)
    #sql3="insert into perms values (%s,'%s',%s,%s,%s,%s,%s,'%s','%s');"%(idd,name,x1[0],bid,x,x1[1],time,date,date1)
    #sql3="insert into perms values (%s,'%s',17095,%s,%s,%s,%s,'%s','%s');"%(idd,name,bid,x,message,time,date,date1)
    #cursor.execute(sql3)
    #mydb.commit()
    return render_template('request.html')        

@app.route('/register',methods=['GET','POST'])
def register():
  return render_template('register.html')

@app.route('/user_home',methods=['GET','POST'])
def user_home():
        flash(' Leaders of tomorrow ')
        return render_template('user_home.html')

@app.route('/building',methods=['GET','POST'])
def building():
        return render_template('building.html')

@app.route('/status',methods=['GET','POST'])
def status():
        return render_template('status.html')

@app.route('/requestt',methods=['GET','POST'])
def requestt():
        return render_template('request.html')

@app.route('/perm',methods=['GET','POST'])
def perm():
        return render_template('perm.html')


if __name__ == '__main__':
        app.config['SESSION_TYPE'] = 'filesystem'
        sess.init_app(app)
        app.debug = True
        app.run(host = '0.0.0.0',port =5000)
