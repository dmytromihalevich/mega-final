from flask import Flask, render_template, redirect,  request, url_for,  session
from my_db import get_all_menu, get_menu_by_id,add_menu


app = Flask(__name__, template_folder= '', static_folder='')



@app.route('/')
def home():
    return render_template('indexhome.html', data=get_all_menu())



@app.route('/profile')
def profile():
    if not 'user' in session.keys() or not session['user']:
        return redirect(url_for('login'))
    
    return render_template('user/index.html')

@app.route('/login', methods=["GET", "POST"])
def login(inccorect_password=False):
    print(inccorect_password)
    if request.method == "POST":
        if request.form['username'] == 'admin' and request.form['password'] == 'admin':
            return redirect(url_for('home'))
        else:
            return redirect(url_for('login', inccorect_password=True))

    
        
    return render_template('login.html', inccorect_password=inccorect_password)




@app.route('/menu/<id>')
def menu(id):
    item=get_menu_by_id(id)[0]
    print(item)
    return render_template('menu.html', title=item[1], description=item[2], cost=item[4],image=item[3])

    return redirect('/')


app.secret_key = 'secret'
app.run(debug=True, host="0.0.0.0")