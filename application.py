from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

# route to handle the landing page of a website.


@app.route("/")
def index_page():
    """Show an index page."""

    #return "<html><body>This is the homepage.</body></html>"

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    return render_template("index.html")

# route to display a simple web page


@app.route("/application-form")
def application_form():
    """Shows application-form"""
 #return "<html><body>application-form.</body></html>"
    #I can paste the whole app-form info here OR
    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    return render_template("application-form.html")


@app.route("/application", methods=['GET', 'POST'])
def response():
    """Shows response.

    Thank you, Jessica McHackbright, for applying to be a QA Engineer. Your
    minimum salary requirement is 89000 dollars."""

    applicant_firstname = request.args.get("firstname")
    applicant_lastname = request.args.get("lastname")
    applicant_position = request.args.get("position")
    applicant_salary = request.args.get("salary")

    #return "<html><body>application-form.</body></html>"
    #I can paste the whole app-form info here OR
    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    return render_template("application-response.html", firstname=applicant_firstname, lastname=applicant_lastname,
                           position=applicant_position, salary=applicant_salary)



if __name__ == "__main__":
    app.run(debug=True)
