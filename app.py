from flask import Flask  , render_template
flask_app = Flask(__name__)
@flask_app.route("/")
def Home():
    return render_template("home.html")
    return 
    
    