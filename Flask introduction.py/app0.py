from flask import Flask
from flask import render_template, request, redirect, url_for, session, logging, jsonify
# from flask_mysqldb import MySQL

app = Flask(__name__)
# mysql = MySQL()

def validation(name, password):
   pass

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.route('/')
def index():
    # Got to database and select a list of name
    # fileter that list for the name starting with S and ending with k and then pass that to our page.
    return render_template("index.html", name="Siamak")


@app.route('/validate', methods=['GET', 'POST'])
def validate():
    if request.method == 'POST':
        first_name = request.form['fname']
        return f"Hello {first_name}"
    elif request.method == 'GET':
        pass
    
    return "Otherwise"

@app.route('/login')
def login():
    return """
        <!DOCTYPE html>
        <html>
        <body>

        <h2>HTML Forms</h2>

        <form method="post" action="/validate">
        <label for="fname">First name:</label><br>
        <input type="text" id="fname" name="fname" value="John"><br>
        <label for="lname">Last name:</label><br>
        <input type="text" id="lname" name="lname" value="Doe"><br><br>
        <input type="submit" value="Submit">
        </form> 

        <p>If you click the "Submit" button, the form-data will be sent to a page called "/action_page.php".</p>

        </body>
        </html>
    """


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

