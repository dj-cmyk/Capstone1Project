from flask import Flask, render_template, request, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
# from sqlalchemy.exc import IntegrityError
import os
from werkzeug.utils import secure_filename

from forms import PropAndHeadpieceForm, ProductionForm
from models import db, connect_db, Level, Production, Headpiece, CostumeGroup, Prop, Role
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
# COSTUME CRUD Routes - PRODUCTIONS
# ***********************************************************************************

# list all productions
@app.route('/productions')
def list_all_productions():
    '''list of all productions currently in rotation'''
    productions = Production.query.all()
    return render_template('productions.html', productions=productions)


# list single production
@app.route('/productions/<int:prod_id>')
def list_one_production(prod_id):
    '''docstring'''
    production = Production.query.get_or_404(prod_id)
    return render_template('productions-detail.html', production=production)


# add new production
@app.route('/productions/new', methods=['GET', 'POST'])
def add_new_production():
    '''docstring'''
    form = ProductionForm()

    if form.validate_on_submit():
        image_path = os.path.join(
            os.path.dirname(app.instance_path), 'static'
        )
        image = form.image_url.data
        filename = secure_filename(image.filename)
        image.save(os.path.join(image_path, 'images', filename))

        production = Production(
            name=form.name.data,
            image_url=f"/static/images/productions/{filename}",
            last_performed=form.last_performed.data,
            is_current=form.is_current.data,
        )

        db.session.add(production)
        db.session.commit()

        return redirect("/productions")

    else:
        return render_template('productions-new.html', form=form)


# edit existing production
@app.route('/productions/<int:prod_id>/edit', methods=['GET', 'POST'])
def edit_productions(prod_id):
    '''docstring'''
    production = Production.query.get_or_404(prod_id)
    form = ProductionForm(obj=production)

    if form.validate_on_submit():
        
        # if form.image_url.data:
        #     image_path = os.path.join(os.path.dirname(app.instance_path), 'static')
        #     image = form.image_url.data
        #     filename = secure_filename(image.filename)
        #     image.save(os.path.join(image_path, 'images', filename))
        #     production.image_url = f"/static/images/productions/{filename}"

       
        production.name = request.form.get("name", production.name)
        production.last_performed = request.form.get("last_performed", production.last_performed)
        production.is_current = request.form.get("is_current", production.is_current)

        db.session.commit()

        return redirect("/productions")

    else:
        return render_template('productions-edit.html', production=production, form=form)


# delete existing production
@app.route('/productions/<int:prod_id>/delete', methods=['GET', 'POST'])
def delete_production(prod_id):
    '''docstring'''
    production = Production.query.get_or_404(prod_id)
    db.session.delete(production)
    db.session.commit()
    return redirect('/productions')


# ***********************************************************************************
# COSTUME CRUD Routes - HEADPIECES
# ***********************************************************************************

# list all headpieces
@app.route('/headpieces')
def list_all_headpieces():
    '''docstring'''
    headpieces = Headpiece.query.all()
    return render_template('headpieces.html', headpieces=headpieces)


# list single headpiece
@app.route('/headpieces/<int:h_id>')
def list_one_headpiece(h_id):
    '''docstring'''
    headpiece = Headpiece.query.get_or_404(h_id)
    return render_template('headpieces-detail.html', headpiece=headpiece)


# add new headpiece
@app.route('/headpieces/add', methods=['GET', 'POST'])
def add_headpiece():
    '''docstring'''
    form = PropAndHeadpieceForm()

    if form.validate_on_submit():
        image_path = os.path.join(
            os.path.dirname(app.instance_path), 'static'
        )
        image = form.image_url.data
        filename = secure_filename(image.filename)
        image.save(os.path.join(image_path, 'images', filename))

        headpiece = Headpiece(
            name=form.name.data,
            image_url=f"/static/images/headpieces/{filename}",
            description=form.description.data,
            quantity=form.quantity.data,
            current_location=form.current_location.data,
            storage_location=form.storage_location.data
        )

        db.session.add(headpiece)
        db.session.commit()

        return redirect("/headpieces")

    else:
        return render_template('headpieces-add.html', form=form)


# edit existing headpiece
@app.route('/headpieces/<int:h_id>/edit', methods=['GET', 'PATCH'])
def edit_headpiece(h_id):
    '''docstring'''
    
    headpiece = Headpiece.query.get_or_404(h_id)
    form = PropAndHeadpieceForm(obj=headpiece)

    if form.validate_on_submit():
        # if form.image_url.data:
        #     image_path = os.path.join(os.path.dirname(app.instance_path), 'static')
        #     image = form.image_url.data
        #     filename = secure_filename(image.filename)
        #     image.save(os.path.join(image_path, 'images', filename))

        headpiece.name = request.form.get("name", headpiece.name)
        # headpiece.image_url = request.form.get("image_url", headpiece.image_url)
        headpiece.description = request.form.get("description", headpiece.description)
        headpiece.quantity = request.form.get("quantity", headpiece.quantity)
        headpiece.current_location = request.form.get("current_location", headpiece.current_location)
        headpiece.storage_location = request.form.get("storage_location", headpiece.storage_location)
        
        db.session.commit()

        return redirect("/headpieces")

    else:
        return render_template('headpieces-edit.html', form=form, headpiece=headpiece)


# delete existing headpiece
@app.route('/headpieces/<int:h_id>/delete', methods=['GET', 'POST'])
def delete_headpiece(h_id):
    '''docstring'''
    headpiece = Headpiece.query.get_or_404(h_id)
    db.session.delete(headpiece)
    db.session.commit()
    return redirect('/headpieces')


# ***********************************************************************************
# COSTUME CRUD Routes - PROPS
# ***********************************************************************************

# list all props
# @app.route('/props')
# def list_all_props():
#     '''docstring'''
#     props = Prop.query.all()
#     return render_template('props.html', props=props)

# # list single prop
# @app.route('/props/<int:prop_id>')
# def list_prop_detail(prop_id):
#     '''docstring'''
#     prop = Prop.query.get_or_404(prop_id)
#     return render_template('props-detail.html', prop=prop)

# # add new prop
# @app.route('/props/new')
# def add_new_prop():
#     '''docstring'''
#     form = PropAndHeadpieceForm()
#     return render_template('props-add.html', form=form)

# edit existing prop
# delete existing prop

# ***********************************************************************************
# COSTUME CRUD Routes - COSTUME GROUPS
# ***********************************************************************************

# list all costumes
@app.route('/costumes')
def list_all_costumes():
    '''docstring'''
    costumes = CostumeGroup.query.all()

    return render_template('costumes.html', costumes=costumes)


# list of costumes by production
@app.route('/<int:prod_id>/costumes')
def list_costumes_by_production(prod_id):
    '''list of all costumes in a specific production'''

    production = Production.query.get_or_404(prod_id)
    roles = Role.query.filter_by(production_id = prod_id)

    return render_template('costumes-production.html', production=production, roles=roles)


# list costume detail 
@app.route('/costumes/<int:role_id>')
def get_costume_details(role_id):
    '''docstring'''
    role = Role.query.get_or_404(role_id)

    return render_template('costume-details.html', role=role)


# add new costume

# edit existing costume

# delete existing costume


# ***********************************************************************************
# COSTUME CRUD Routes - ROLES GROUPS
# ***********************************************************************************

# list all roles
@app.route('/roles')
def list_all_roles():
    '''docstring'''
    roles = Role.query.all()
    return render_template('roles.html', roles=roles)

# add new role
# edit existing role
# delete existing role