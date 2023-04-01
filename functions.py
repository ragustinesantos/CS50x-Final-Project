from flask import redirect, render_template, request, session
from functools import wraps

# Create a format function for desired currency
def cad(value):
    return f"C$ {value:,.2f}"

# Create a login required decorator
def login_required(f):

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

# Error message return
def error(message):

    return render_template("error.html", message=message)

