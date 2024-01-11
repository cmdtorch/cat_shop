from flask import current_app as app
from flask import make_response, redirect, render_template, request, url_for

from . import db
from .model import Cat


@app.route('/')
@app.route('/cats/')
def cats_list():
    cats = Cat.query.all()
    cats = db.paginate(db.select(Cat), max_per_page=5)
    return render_template("list.html", cats=cats, title="All Cats")


@app.route('/cat/<int:pk>/')
def cat_detail(pk: int):
    cat = Cat.query.get(pk)
    related_cats = Cat.query.filter(Cat.id != cat.id).all()[:3]
    return render_template("detail.html", cat=cat, related_cats=related_cats, title=cat.name)
