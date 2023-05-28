from application import app
from application.forms import BasicForm
from flask import render_template, request, g, flash,redirect, url_for
import pymysql
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

auth = HTTPBasicAuth()

users = {
    "admin": generate_password_hash("admin"),
    "susan": generate_password_hash("password"),
    "alamin": generate_password_hash("password"),
    "karl": generate_password_hash("password"),
    "mike": generate_password_hash("password"),
    "david": generate_password_hash("password"),
    "neil": generate_password_hash("password")
}
roles = {
    "admin": ['admin'],
    "susan": ['admin'],
    "alamin": ['admin'],
    "karl": ['admin'],
    "mike": ['admin'],
    "david": ['admin'],
    "neil": ['admin']
}
@auth.verify_password
def verify_password(username, password):
	if username in users and \
			check_password_hash(users.get(username), password):
		return username

@auth.get_user_roles
def get_user_roles(user):
	return roles[user]
### End HTTP Authorisation

# Section 1 above is used for importing Libraries that we will need.

# Section 2: HELPER FUNCTIONS e.g. DB connection code and methods
def connect_db():
    return pymysql.connect(
        user = 'root', password = '', database = 'skyflix',
        autocommit = True, charset = 'utf8mb4',
        cursorclass = pymysql.cursors.DictCursor)

def get_db():
    '''Opens a new database connection per request.'''
    if not hasattr(g, 'db'):
        g.db = connect_db()
    return g.db

@app.teardown_appcontext
def close_db(error):
    '''Closes the database connection at the end of request.'''
    if hasattr(g, 'db'):
        g.db.close()


# Helper methods
def get_date():

    now = datetime.now()
    today = now.strftime("%d/%m/%Y %H:%M:%S")
    app.logger.info({today})
    return today






@app.route('/home', methods = ['GET','POST'])
@auth.login_required
def home():
    """Landing page. Showing Films    """
    cursor = get_db().cursor()
    cursor.execute("SELECT film_id,title,description,genre,streams,age_rating, trailer from Film order by streams desc ")
    result = cursor.fetchall()
    app.logger.info(result)
    return render_template(
                'home.html',
                title="All Films",
                description=f"Blockbusters, Horror, Comedy, anything you want!  \n {get_date()}",
                records=result,
        user = auth.current_user()
    )
@app.route('/register2',  methods = ['GET','POST'])
def register2():
    """ Second form.
    """
    message = ""
    form = BasicForm() # create form instance
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        address = form.address.data
        phone_number = form.phone_number.data


        app.logger.info(f" {first_name} {last_name} {email} being added.")
        try:
            cursor = get_db().cursor()
            sql = "INSERT INTO `Customer` (firstname, lastname, email, address, phone) VALUES (%s, %s, %s, %s, %s)"
            app.logger.info(sql)
            cursor.execute(sql, (first_name.upper(), last_name.upper(), email.upper(), address.upper(), phone_number.upper()))
            message = f"Welcome To  SkyFlix!!"
            app.logger.info(message)
            flash(message)
            return redirect(url_for('home'))
        except Exception as e:
            message = f"error in insert operation: {e}"
            flash(message)
    return render_template('form1.html', message=message, form=form, title='Create a SkyFlix Account', description='Sign up', user=auth.current_user()
)


@app.route('/film/<int:id>')
def film_display(id):
    """ Third page. Param displaying from Film table
    """
    app.logger.info(id)
    cursor = get_db().cursor()
    cursor.execute("SELECT * FROM Film WHERE film_id=%s ",id)
    result = cursor.fetchone()
    app.logger.info(result)
    return render_template(
                'film.html',
                title="Third database query - using film template, passing parameter to query",
                description=f"Another db query with parameter from url: film_id={id}.",
                record=result
    )

@app.route('/film/purchase/<int:id>')
@auth.login_required(role='admin')
def film_purchase(id):
    """
    """
    app.logger.info(id)
    cursor = get_db().cursor()
    cursor.execute("UPDATE film SET streams = streams + 1 WHERE film_id=%s ",id)

    cursor.execute(" select title from film WHERE film_id=%s ", id)
    title=cursor.fetchone()
    message=f"Thank you for Purchasing  {title['title']}"
    app.logger.info(message)
    flash(message)
    return redirect(url_for('home'))

@app.route('/', methods = ['GET','POST'])
def landing():
    """Landing page. Showing Films    """

    return render_template(
                'landing.html',
                title="All Films",
                description=f"Blockbusters, Horror, Comedy, anything you want! {get_date()}",

        user = auth.current_user()
    )

@app.route('/contact')

def contact( ):
    """"contact us page"""
    return render_template(
        'contact.html'
    )


@app.route('/ts&cs', methods = ['GET','POST'])
def terms_of_use():
    """Landing page. Showing Films    """

    return render_template(
                'ts&cs.html',


    )