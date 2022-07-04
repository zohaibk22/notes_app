from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['GET', 'POST'] )
def login():
    data = request.form
    return render_template('login.html', text='Zohaib', boolean=False)

  
@auth.route('signup',  methods = ['GET', 'POST'])
def signup():

    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password = request.form.get('password')
    return render_template('signup.html')

@auth.route('/logout')
def logout():
    return render_template('logout.html')