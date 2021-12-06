from flask import Flask
from flask import render_template, request, redirect, url_for, session, logging, jsonify
# this just imports modules then class functions from those modules

app = Flask(__name__)
#creating the object app and telling flask to execute it with the required name from __main__

def validation(name, password):
   pass
#making a definition but using the pass option to overlook it but its there as a placeholder for future use
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404
# decorator for app error handler from flask, as it sounds its an error handler with a stated return

@app.route('/')
def index():
# decorator for app route, the root (/) of the page will return the stated return statement
    return render_template("index.html", name="Siamak")
#above we referance another file in the return statement to prevent our main code being blown up with html text

@app.route('/validate', methods=['GET', 'POST'])
#this decorator for app route at file validate employs the get and post for the site pages.
def validate():
    if request.method == 'POST':
        first_name = request.form['fname']
        return f"Hello {first_name}"
    elif request.method == 'GET':
        pass
    
    return "Otherwise"
# another decorator for the app with a if, elif, pass and return statement
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
#here we have the html text in the main code file but this could be stored else where and referanced into the code as in line 19

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
# this runs the app, host is set to open to all through port 500.