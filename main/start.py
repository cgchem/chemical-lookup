from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify, current_app

from main.lookup import names_to_synonyms

bp = Blueprint('lookup_page', __name__, url_prefix='')


def sanitize(astr):

    """discard everything that isn't a number or a dash for now"""

    out = ""
    for q in astr:
        if q in "0123456789-":
            out += q
        if len(out) > 20:
            return out
    return out


@bp.route('/', methods=('GET', 'POST'))
def begin():

    error = None

    if request.method == 'POST':

        query = request.form['qry']
        qries = [sanitize(z) for z in query.split("\n")]
        results = names_to_synonyms(qries)
        # OLD: a dict of id: list of identifiers
        # NEW: a list of tuples (name, [list of identifiers])

        # results = {"1":["cake", "bread"], "2":["apples", "pears"]}

        return render_template('page1/page1.html', results=results)

    if request.method == 'GET':

        pass

    if error:
        flash(error)
    return render_template('page1/page1.html')



