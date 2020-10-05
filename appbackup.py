from flask import Flask,request,render_template,flash,redirect,url_for
import mysql.connector
app = Flask(__name__)
app.secret_key = 'my unobvious secret key'
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="varunasd1",
  database="test2"
) 
cursor = mydb.cursor()
@app.route('/')
def showcase():
        return render_template('index.html')

@app.route('/login')
def login():
        return render_template('login.html')

@app.route('/Wazza')
def Wazzaa():
        return "Hello World"



# @app.route('/index',methods=['GET','POST'])
# def index():
#       #if request=="POST":
#               #DEFINE registration that is putting username password in database



@app.route('/landing', methods=['GET','POST'] )
def land():
        res = ""
        t=0
        if request.method == "POST":
           email =request.form["email"]
           passw = request.form["password"]
           sql="INSERT into user values(2,'me','me','me')"
           cursor.execute(sql)
           print("inserted")
           mydb.commit()
           sql='SELECT uemail,upassword FROM user'
           cursor.execute(sql)
           rs = cursor.fetchall()
           for row in rs:
           	print(rs[0])
           	if email == row[0] and passw == row[1]:
           		t=1
           		break
        if t == 0:
           flash('Invalid user credentials')
           return render_template('login.html')
        else:
           flash(email)
           return render_template('user_home.html')

# @app.route('/permi',methods=['GET','POST'])
# def permi():
#       if request.method=='POST'
        # put all the fields from the form in the table         

# @app.route('/reqi',methods=['GET','POST'])
# def permi():
#       if request.method=='POST'
#       # put all the fields from the form in the table         

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
