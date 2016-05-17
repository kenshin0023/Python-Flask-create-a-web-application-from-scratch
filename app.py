from flask import Flask, render_template, json, request
import MySQLdb
from werkzeug import generate_password_hash, check_password_hash
app = Flask(__name__)

db= MySQLdb.connect(host="localhost", user="root", passwd="",
db="python-test")

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')


@app.route('/showSignUp',methods=['POST','GET'])
def signUp():
    if request.method == 'POST':
      try:
         _name = request.form['inputName']
         _email = request.form['inputEmail']
         _password = request.form['inputPassword']
         _hashed_password = generate_password_hash(_password)

         # validate the received values
         if _name and _email and _password:
             cursor = db.cursor()
             stmt = "INSERT INTO sp_createuser (p_name, p_username, p_password) VALUES ('" + _name + "', '" + _email + "', '" + _hashed_password + "')"
             cursor.execute(stmt)
             
             cursor.close()
             db.commit()
             msg = "Record successfully added"
         else:
            msg = "Please correct input"
      except:
         db.rollback()
         msg = "error in insert operation"
      
      finally:
         return render_template("signup.html",msg = msg)
         db.close()

if __name__ == "__main__":
    #app.run(port=5002)
   app.run(debug = True) 
