import json
import os

import pyrebase
import flask

with open("firebase-config.ignore.json", encoding="utf-8") as f:
    firebaseConfig = json.loads(f.read())
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

with open("database.json", encoding="utf-8") as f:
    database = json.loads(f.read())

app = flask.Flask(__name__)
app.config["SECRET_KEY"] = os.urandom(24)


@app.route("/login", methods=["GET", "POST"])
def login():
    if flask.request.method == "GET":
        return flask.render_template("login.html", msg="")

    print(flask.request.form)
    print(flask.request)

    email = flask.request.form["email"]
    password = flask.request.form["password"]
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        print("login", user)
        flask.session["usr"] = email
        return flask.redirect(flask.url_for("index"))
    except Exception:
        return flask.render_template("login.html", msg="メールアドレスまたはパスワードが間違っています。")


@app.route("/", methods=["GET"])
def index():
    usr = flask.session.get("usr")
    if usr is None:
        return flask.redirect(flask.url_for("login"))
    return flask.render_template("index.html", database=database, usr=usr)


@app.route("/logout")
def logout():
    del flask.session["usr"]
    return flask.redirect(flask.url_for("login"))


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if flask.request.method == "GET":
        return flask.render_template("signup.html")

    email = flask.request.form["email"]
    password = flask.request.form["password"]
    try:
        user = auth.create_user_with_email_and_password(email, password)
        print("signup", user)
        return flask.redirect(flask.url_for("login"))
    except Exception:
        return flask.render_template("signup.html")


if __name__ == "__main__":
    app.debug = True
    app.run(port=5000)
