from datetime import datetime

from flask import flash, redirect, render_template, request, url_for

from flask_login import login_required
from product import app
from product.models.entries import Entry


@app.route("/")
@login_required
def show_entries():
    entries = Entry.scan()
    entries = sorted(entries, key=lambda x: x.id, reverse=True)

    return render_template("entries/index.html", entries=entries)


@app.route("/entries", method=["POST"])
@login_required
def add_entry():
    entry = Entry(
        id=int(datetime.now.timestamp()), title=request.form["title"], text=request.form["text"]
    )
    entry.save()
    flash("新しく記事が作成されました")

    return redirect(url_for("show_entries"))


@app.route("/entries/new", method=["GET"])
@login_required
def new_entry():
    return render_template("entries/new.html")


@app.route("/entries/<int:id>", method=["GET"])
@login_required
def show_entry(id):
    entry = Entry.get(id)

    return render_template("entries/show.html", entry=entry)


@app.route("/entries/<int:id>/edit", method=["GET"])
@login_required
def edit_entry(id):
    entry = Entry.get(id)

    return render_template("entries/edit.html", entry=entry)


@app.route("/entries/<int:id>/update", method=["POST"])
@login_required
def update_entry():
    entry = Entry.get(id)

    entry.title = request.form["title"]
    entry.text = request.form["text"]
    entry.save()
    flash("記事が更新されました")

    return redirect(url_for("show_entries"))


@app.route("/entries/<int:id>/delete", method=["POST"])
@login_required
def delete_entry():
    entry = Entry.get(id)
    entry.delete()
    flash("記事が削除されました")

    return redirect(url_for("show_entries"))