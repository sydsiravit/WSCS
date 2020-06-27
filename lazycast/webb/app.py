from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SECRET_KEY'] = "qwerty"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

class nodename(db.Model):
   id = db.Column('_id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))

   def __init__(self, name):
      self.name = name

@app.route('/')
def show_all():
   nn = nodename.query.get(1)
   db.session.commit()
   
   return render_template('show_all.html',current_node_name = nn.name )

@app.route('/new', methods = ['GET', 'POST'])
def new():
   if request.method == 'POST':
      if not request.form['name'] :
         flash('Please enter all the fields', 'error')
      else:
         nnn = nodename(request.form['name'])
         
         query = nodename.query.get(1)
         query.name = nnn.name
         
         db.session.commit()
         
         flash('Record was successfully change')
         return redirect(url_for('show_all'))
   return render_template('new.html')

if __name__ == '__main__':
   db.create_all()
   app.run()
