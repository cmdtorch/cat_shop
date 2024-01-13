import sqlalchemy
from flask import current_app as app
from flask import make_response, redirect, render_template, request, url_for
from sqlalchemy import func, or_

from . import db
from .model import Cat, CatBreed


@app.route('/')
def index():
    return render_template(
        "index.html",
        title="FuzzyCats"
    )


@app.route('/cats/')
def cats_list():
    sort_value = request.args.get('sort', '-date')
    selected_breeds = request.args.getlist('breed')
    search_query = request.args.get('query')
    sort = {
        '-date': Cat.created_at.desc(),
        '-age': Cat.dob.desc(),
        'age': Cat.dob,
    }

    if search_query:
        stmt = (db.select(Cat).filter(or_(
            Cat.name.icontains(f'%{search_query}%'),
            Cat.description.icontains(f'%{search_query}%'),
        )).order_by(sort.get(sort_value)))
    elif selected_breeds:
        stmt = db.select(Cat).filter(Cat.breed.in_(selected_breeds)).order_by(sort.get(sort_value))
    else:
        stmt = db.select(Cat).order_by(sort.get(sort_value))
    cats = db.paginate(stmt, max_per_page=6)

    return render_template(
        "list.html",
        cats=cats,
        breeds=CatBreed,
        sort=sort_value,
        search_query=search_query,
        selected_breeds=selected_breeds,
        title="FuzzyCats"
    )


@app.route('/cat/<int:pk>/')
def cat_detail(pk: int):
    cat = Cat.query.get(pk)
    related_cats = Cat.query.filter(Cat.id != cat.id).order_by(func.random())[:4]
    return render_template("detail.html", cat=cat, related_cats=related_cats, title=cat.name)


@app.route('/error_page/')
def error_page():
    5 / 0


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(e):
    return render_template('500.html'), 500
