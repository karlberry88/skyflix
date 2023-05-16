from application import app
from application.forms import BasicForm
from flask import render_template, request, g, flash,redirect, url_for
import pymysql
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

### HTTP Authorisation
auth = HTTPBasicAuth()

users = {
	"admin": generate_password_hash("admin"),
	"eoghan": generate_password_hash("password")
}
roles = {
	"admin": ['admin'],
	"eoghan": []
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
    """ Function to return (fake) date - TASK: Update this - Add the code to pass the current date to the home 	HTML template.
    """
    today = "Today"
    app.logger.info(f"In get_date function! Update so it returns the correct date! {today}")
    return today


# Section 4: APPLICATION ROUTES (WEB PAGE DEFINITIONS)

@app.route('/', methods = ['GET','POST'])
def home():
    """Landing page. Showing Films    """
    cursor = get_db().cursor()
    cursor.execute("SELECT film_id, title, description, trailer from Film order by title desc ")
    result = cursor.fetchall()
    app.logger.info(result)
    return render_template(
                'home.html',
                title="All Films",
                description=f"Python, MySQL, Flask & Jinja. {get_date()}",
                records=result,
        user = auth.current_user()
    )
@app.route('/register1', methods = ['GET','POST'])
@auth.login_required
def register():
    """ Basic form.
    """
    error = ""
    form = BasicForm() # create form instance

    # if page is loaded as a post i.e. user has submitted the form
    if request.method == "POST":
        first_name = form.first_name.data
        last_name = form.last_name.data

        app.logger.info(f"We were given: {first_name} {last_name}")

        if len(first_name) == 0 or len(last_name) == 0:
            error = "Please supply both first and last names."
        else:
            return 'Thank you!'

    return render_template(
                'form1.html',
                title="Simple form!",
                description=f"Using Flask with  a form on {get_date()}",
                form=form,
                message=error,
    user = auth.current_user()
    )
@app.route('/register2',  methods = ['GET','POST'])
@auth.login_required(role='admin')
def register2():
    """ Second form.
    """
    message = ""
    form = BasicForm() # create form instance
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        app.logger.info(f" {first_name} {last_name} being added.")
        try:
            cursor = get_db().cursor()
            sql = "INSERT INTO `actor` (first_name, last_name) VALUES (%s, %s)"
            app.logger.info(sql)
            cursor.execute(sql, (first_name.upper(), last_name.upper()))
            message = "Record successfully added"
            app.logger.info(message)
            flash(message)
            return redirect(url_for('home'))
        except Exception as e:
            message = f"error in insert operation: {e}"
            flash(message)
    return render_template('form1.html', message=message, form=form, title='Form Test 2 - Add', description='DB test', user = auth.current_user()
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

@app.route('/actor/delete/<int:id>')
@auth.login_required(role='admin')
def actor_delete(id):
    """ Fourth route. Param for deleting from Actor table
    """
    app.logger.info(id)
    cursor = get_db().cursor()
    cursor.execute("DELETE FROM Actor WHERE actor_id=%s ",id)
    message=f"Deleted actor id {id}"
    app.logger.info(message)
    flash(message)
    return redirect(url_for('home'))

