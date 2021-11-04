from flask import Flask, render_template, request, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
# from sqlalchemy.exc import IntegrityError
import os
from werkzeug.utils import secure_filename

from forms import HeadpieceForm, SearchForm
from models import db, connect_db, Level, Production, Headpiece, CostumeGroup, Prop, Role, Role_Costume
from user_models import User


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///costume_inventory'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'secretANDrandom101010'

app.config['MAX_CONTENT_LENGTH'] = 8 * 1024 * 1024  # 8MB max-limit.

debug = DebugToolbarExtension(app)

connect_db(app)



# ***********************************************************************************
# Routes
# ***********************************************************************************

@app.route('/')
def display_homepage():
    '''docstring'''
    return render_template('index.html')



# ***********************************************************************************
# USER Sign up, log in, log out Routes
# ***********************************************************************************


# ***********************************************************************************
# COSTUME CRUD Routes
# ***********************************************************************************

@app.route('/api/headpieces/add', methods=['GET', 'POST'])
def add_headpiece():
    '''docstring'''
    form = HeadpieceForm()

    if form.validate_on_submit():
        image_path = os.path.join(
            os.path.dirname(app.instance_path), 'static'
        )
        image = form.image_url.data
        filename = secure_filename(image.filename)
        image.save(os.path.join(image_path, 'images', filename))

        headpiece = Headpiece(
            name=form.name.data,
            image_url=f"/static/images/{filename}",
            description=form.description.data,
            quantity=form.quantity.data,
            current_location=form.current_location.data,
            storage_location=form.storage_location.data
        )

        db.session.add(headpiece)
        db.session.commit()

        return redirect("/api/headpieces")

    else:
        return render_template('add.html', form=form)


@app.route('/api/headpieces')
def get_all_headpieces():
    '''docstring'''
    headpieces = Headpiece.query.all()
    return render_template('headpieces.html', headpieces=headpieces)



@app.route('/search', methods=['GET', 'POST'])
def search_for_costume():
    '''docstring'''
    form = SearchForm()

    productions = [(p.id, p.name) for p in Production.query.all()]
    levels = [(l.id, l.levelName) for l in Level.query.all()]

    form.production.choices = productions
    form.level.choices = levels

    if form.validate_on_submit():
        selected_production = form.production.data
        print(selected_production)
        selected_level = form.level.data
        return redirect(f'/production/{selected_production}/{selected_level}')

    return render_template('search.html', form=form)

@app.route('/list')
def list_productions():
    '''docstring'''
    productions = Production.query.all()
    return render_template('list.html', productions=productions)

@app.route('/production/<id>/<level_id>')
def get_costumes_by_production(id, level_id):
    '''docstring'''
    production = Production.query.get_or_404(id)
    level = Level.query.get_or_404(level_id)
    return render_template('production.html', production=production, level=level)



@app.route('/select')
def by_prod_and_level():
    production = Production.query.get(1)
    level = Level.query.get(13)

    return render_template('test.html', level=level, production=production)
