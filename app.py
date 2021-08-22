from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm , Authenticate_Employee_Form
import mysql.connector as sql


mydb=sql.connect(host='localhost',
  user="root",
  password="12345",
  database="employee")
cursor=mydb.cursor()
app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'


vl=()
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template('about.html', title='About')

try:

    @app.route("/register", methods=['GET', 'POST'])
    def register():
        form = RegistrationForm()
        if form.validate_on_submit():
            value=[]
            value.append(form.firstname.data)
            value.append(form.lastname.data)
            value.append(form.dob.data)
            value.append(form.username.data)
            value.append(form.email.data)
            value.append(form.password.data)
            value.append(form.confirm_password.data)
            inssql="INSERT INTO EMPLOYEEINFO(firstname,lastname,date_of_birth,username,email,password,confirm_password) VALUES(%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(inssql,value)
            mydb.commit()
            flash(f'Account created for {form.username.data}!', 'success')
            return redirect(url_for('home'))
        return render_template('register.html', title='Register', form=form)


    @app.route("/login", methods=['GET', 'POST'])
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            if form.email.data == 'admin@blog.com' and form.password.data == 'password':
                flash('You have been logged in!', 'success')
                cursor.execute("SELECT username,email,date_of_birth FROM EMPLOYEEINFO")
                res=cursor.fetchall()
                flash("employee details:")
                
                for i in res:
                    flash(i)
                
                return redirect(url_for('home'))
            else:
                flash('Login Unsuccessful. Please check username and password', 'danger')
        return render_template('login.html', title='Login', form=form)


    ver=[]

    @app.route("/login2",methods=['GET','POST'])
    def login2():
        form=Authenticate_Employee_Form()
        if form.validate_on_submit():
            cursor.execute('SELECT email,password FROM EMPLOYEEINFO')
            result=cursor.fetchall()
            for i in result:
                ver.append(i)

            count=0
            for j in ver:
                count+=1
            count1=0
            email_verification=str(form.email_ver.data)
            for j in range(count):            
                if ver[j][0]==form.email_ver.data:
                    if ver[j][1]==form.password_ver.data:
                        cursor.execute(f"SELECT firstname,lastname,date_of_birth,email,username FROM EMPLOYEEINFO WHERE email='{email_verification}'")
                        res=cursor.fetchall()
                        flash("here is the details of the employee")
                        flash(res)
                        
                        count1=1
                
                
            if count1==0:
                flash("Unsuccesful Authentication")

            
                    
            return redirect(url_for('home'))

        return render_template('login2.html',title='Authentication',form=form)


    if __name__ == '__main__':
        app.run(debug=True, host="localhost")
except Exception as e:
    print("exception arised:",e)
finally:
    mydb.close()