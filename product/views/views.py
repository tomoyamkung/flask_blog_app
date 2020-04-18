from flask import flash, redirect, render_template, request, url_for
from flask_login import login_user, logout_user

from product import app
from product.models.users import User


@app.route("/login", method=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form["username"] != app.config["USERNAME"]:
            flash("ユーザ名が異なります")
        elif request.form["password"] != app.config["PASSWORD"]:
            flash("パスワードが異なります")
        else:
            login_user(User(request.form["username"]))
            flash("ログインしました")
            return redirect(url_for("show_entries"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    logout_user()
    flash("ログアウトしました")
    return redirect(url_for("login"))


@app.errorhandler(404)
def non_existant_route(error):
    return redirect(url_for("login"))
