from flask import Flask, render_template, request, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy import desc
# from sqlalchemy.exc import IntegrityError
import os
from werkzeug.utils import secure_filename

from forms import PropAndHeadpieceForm, ProductionForm, RoleForm
from models import db, connect_db, Level, Production, Headpiece, CostumeGroup, Prop, Role
from user_models import User


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///costume_inventory'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'secretANDrandom101010'

app.config['MAX_CONTENT_LENGTH'] = 8 * 1024 * 1024  # 8MB max-limit.

# debug = DebugToolbarExtension(app)

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
    productions = Production.query.order_by(desc(Production.is_current)).order_by(desc(Production.last_performed))
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
        image = request.files.get('image_url', production.image_url)

        if image:
            image_path = os.path.join(os.path.dirname(app.instance_path), 'static')
            filename = secure_filename(image.filename)
            image.save(os.path.join(image_path, 'images/productions', filename))
            production.image_url = f"/static/images/productions/{filename}"
       

        if request.form.get("is_current") == "y":
            production.is_current = True
        else:
            production.is_current = False   


        production.name = request.form.get("name", production.name)
        production.last_performed = request.form.get("last_performed", production.last_performed)
        
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
    roles = Role.query.filter_by(headpiece_id = h_id)
    return render_template('headpieces-detail.html', headpiece=headpiece, roles=roles)


# add new headpiece
@app.route('/headpieces/new', methods=['GET', 'POST'])
def add_headpiece():
    '''docstring'''
    form = PropAndHeadpieceForm()

    if form.validate_on_submit():
        image_path = os.path.join(
            os.path.dirname(app.instance_path), 'static'
        )
        image = form.image_url.data
        filename = secure_filename(image.filename)
        image.save(os.path.join(image_path, 'images/headpieces', filename))

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
@app.route('/headpieces/<int:h_id>/edit', methods=['GET', 'POST'])
def edit_headpiece(h_id):
    '''docstring'''
    
    headpiece = Headpiece.query.get_or_404(h_id)
    form = PropAndHeadpieceForm(obj=headpiece)

    if form.validate_on_submit():
        image = request.files.get('image_url', headpiece.image_url)

        if image:
            image_path = os.path.join(os.path.dirname(app.instance_path), 'static')
            filename = secure_filename(image.filename)
            image.save(os.path.join(image_path, 'images/headpieces', filename))
            headpiece.image_url = f"/static/images/headpieces/{filename}"

        headpiece.name = request.form.get("name", headpiece.name)
        headpiece.description = request.form.get("description", headpiece.description)
        headpiece.quantity = request.form.get("quantity", headpiece.quantity)
        headpiece.current_location = request.form.get("current_location", headpiece.current_location)
        headpiece.storage_location = request.form.get("storage_location", headpiece.storage_location)
        
        db.session.commit()

        return redirect(f"/headpieces/{h_id}")

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
@app.route('/props')
def list_all_props():
    '''docstring'''
    props = Prop.query.all()
    return render_template('props.html', props=props)

# list single prop
@app.route('/props/<int:prop_id>')
def list_prop_detail(prop_id):
    '''docstring'''
    prop = Prop.query.get_or_404(prop_id)
    roles = Role.query.filter_by(prop_id = prop_id)
    return render_template('props-detail.html', prop=prop, roles=roles)

# add new prop
@app.route('/props/new', methods=['GET', 'POST'])
def add_new_prop():
    '''docstring'''
    form = PropAndHeadpieceForm()

    if form.validate_on_submit():
        image_path = os.path.join(
            os.path.dirname(app.instance_path), 'static'
        )
        image = form.image_url.data
        filename = secure_filename(image.filename)
        image.save(os.path.join(image_path, 'images/props', filename))

        prop = Prop(
            name=form.name.data,
            image_url=f"/static/images/props/{filename}",
            description=form.description.data,
            quantity=form.quantity.data,
            current_location=form.current_location.data,
            storage_location=form.storage_location.data
        )

        db.session.add(prop)
        db.session.commit()

        return redirect("/props")

    else:
        return render_template('props-add.html', form=form)

# edit existing prop
@app.route('/props/<int:prop_id>/edit', methods=['GET', 'POST'])
def edit_prop(prop_id):
    '''docstring'''
    
    prop = Prop.query.get_or_404(prop_id)
    form = PropAndHeadpieceForm(obj=prop)

    if form.validate_on_submit():
        image = request.files.get('image_url', prop.image_url)

        if image:
            image_path = os.path.join(os.path.dirname(app.instance_path), 'static')
            filename = secure_filename(image.filename)
            image.save(os.path.join(image_path, 'images/props', filename))
            prop.image_url = f"/static/images/props/{filename}"

        prop.name = request.form.get("name", prop.name)
        prop.description = request.form.get("description", prop.description)
        prop.quantity = request.form.get("quantity", prop.quantity)
        prop.current_location = request.form.get("current_location", prop.current_location)
        prop.storage_location = request.form.get("storage_location", prop.storage_location)
        
        db.session.commit()

        return redirect(f"/props/{prop_id}")

    else:
        return render_template('props-edit.html', form=form, prop=prop)

# delete existing prop
@app.route('/props/<int:prop_id>/delete', methods=['GET', 'POST'])
def delete_prop(prop_id):
    '''docstring'''
    prop = Prop.query.get_or_404(prop_id)
    db.session.delete(prop)
    db.session.commit()
    return redirect('/props')

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
@app.route('/costumes/<int:costume_id>')
def get_costume_details(costume_id):
    '''docstring'''
    costume = CostumeGroup.query.get_or_404(costume_id)
    cg1 = Role.query.filter_by(cg1_id = costume_id)
    cg2 = Role.query.filter_by(cg2_id = costume_id)
    cg3 = Role.query.filter_by(cg3_id = costume_id)
    roles = [cg1, cg2, cg3]
    return render_template('costumes-details.html', costume=costume, roles=roles)


# add new costume
@app.route('/costumes/new', methods=['GET', 'POST'])
def add_new_costume():
    '''docstring'''
    form = PropAndHeadpieceForm()

    if form.validate_on_submit():
        image_path = os.path.join(
            os.path.dirname(app.instance_path), 'static'
        )
        image = form.image_url.data
        filename = secure_filename(image.filename)
        image.save(os.path.join(image_path, 'images/costumes', filename))

        costume = CostumeGroup(
            name=form.name.data,
            image_url=f"/static/images/costumes/{filename}",
            description=form.description.data,
            quantity=form.quantity.data,
            current_location=form.current_location.data,
            storage_location=form.storage_location.data
        )

        db.session.add(costume)
        db.session.commit()

        return redirect("/costumes")

    else:
        return render_template('costumes-add.html', form=form)

# edit existing costume
@app.route('/costumes/<int:costume_id>/edit', methods=['GET', 'POST'])
def edit_costume(costume_id):
    '''docstring'''
    
    costume = CostumeGroup.query.get_or_404(costume_id)
    form = PropAndHeadpieceForm(obj=costume)

    if form.validate_on_submit():
        image = request.files.get('image_url', costume.image_url)

        if image:
            image_path = os.path.join(os.path.dirname(app.instance_path), 'static')
            filename = secure_filename(image.filename)
            image.save(os.path.join(image_path, 'images/costumes', filename))
            costume.image_url = f"/static/images/costumes/{filename}"

        costume.name = request.form.get("name", costume.name)
        costume.description = request.form.get("description", costume.description)
        costume.quantity = request.form.get("quantity", costume.quantity)
        costume.current_location = request.form.get("current_location", costume.current_location)
        costume.storage_location = request.form.get("storage_location", costume.storage_location)
        
        db.session.commit()

        return redirect(f"/costumes/{costume_id}")

    else:
        return render_template('costumes-edit.html', form=form, costume=costume)

# delete existing costume
@app.route('/costumes/<int:c_id>/delete', methods=['GET', 'POST'])
def delete_costume(c_id):
    '''docstring'''
    costume = CostumeGroup.query.get_or_404(c_id)
    db.session.delete(costume)
    db.session.commit()
    return redirect('/costumes')


# ***********************************************************************************
# COSTUME CRUD Routes - ROLES 
# ***********************************************************************************

# list all roles
@app.route('/roles')
def list_all_roles():
    '''docstring'''
    roles = Role.query.all()
    return render_template('roles.html', roles=roles)

# list one role
@app.route('/roles/<int:role_id>')
def list_one_role(role_id):
    '''docstring'''
    role = Role.query.get_or_404(role_id)
    return render_template('roles-details.html', role=role)

# add new role
@app.route('/roles/new', methods=['GET', 'POST'])
def add_new_role():
    '''docstring'''
    form = RoleForm()
    costumes = [("", "---")]+[(c.id, c.name) for c in CostumeGroup.query.all()]

    form.production_id.choices = [(p.id, p.name) for p in Production.query.all()]
    form.level_id.choices = [(l.id, l.name) for l in Level.query.all()]
    form.cg1_id.choices = [(c.id, c.name) for c in CostumeGroup.query.all()]
    form.cg2_id.choices = costumes
    form.cg3_id.choices = costumes
    form.headpiece_id.choices = [(h.id, h.name) for h in Headpiece.query.all()]
    form.prop_id.choices = [("", "---")]+[(p.id, p.name) for p in Prop.query.all()]

    if form.validate_on_submit():

        role_data = {
            'name': form.name.data,
            'production_id': form.production_id.data,
            'level_id': form.level_id.data,
            'cg1_id': form.cg1_id.data,
        }
        if form.cg2_id.data != "":
            role_data['cg2_id'] = form.cg2_id.data
        if form.cg3_id.data != "":
            role_data['cg3_id'] = form.cg3_id.data

        role_data['headpiece_id'] = form.headpiece_id.data

        if form.prop_id.data != "":
            role_data['prop_id'] = form.prop_id.data
        
        role = Role(**role_data)

        db.session.add(role)
        db.session.commit()

        return redirect("/roles/")

    else:
        return render_template('roles-add.html', form=form)


# edit existing role
@app.route('/roles/<int:role_id>/edit', methods=['GET', 'POST'])
def edit_role(role_id):
    '''docstring'''
    
    role = Role.query.get_or_404(role_id)
    form = RoleForm(obj=role)
    costumes = [("", "---")]+[(c.id, c.name) for c in CostumeGroup.query.all()]
    # populate additional choices in the form? 
    form.production_id.choices = [(p.id, p.name) for p in Production.query.all()]
    form.level_id.choices = [(l.id, l.name) for l in Level.query.all()]
    form.cg1_id.choices = [(c.id, c.name) for c in CostumeGroup.query.all()]
    form.cg2_id.choices = costumes
    form.cg3_id.choices = costumes
    form.headpiece_id.choices = [(h.id, h.name) for h in Headpiece.query.all()]
    form.prop_id.choices = [("", "---")]+[(p.id, p.name) for p in Prop.query.all()]

    if form.validate_on_submit():
        
        role.name = request.form.get("name", role.name)
        role.production_id = request.form.get("production_id", role.production_id)
        role.level_id = request.form.get("level_id", role.level_id)
        role.cg1_id = request.form.get("cg1_id", role.cg1_id)
        role.cg2_id = request.form.get("cg2_id", role.cg2_id)
        role.cg3_id = request.form.get("cg3_id", role.cg3_id)
        role.headpiece_id = request.form.get("headpiece_id", role.headpiece_id)
        role.prop_id = request.form.get("prop_id", role.prop_id)
        
        db.session.commit()

        return redirect(f"/roles/{role_id}")

    else:
        return render_template('roles-edit.html', form=form)


# delete existing role
@app.route('/roles/<int:role_id>/delete', methods=['GET', 'POST'])
def delete_role(role_id):
    '''docstring'''
    role = Role.query.get_or_404(role_id)
    db.session.delete(role)
    db.session.commit()
    return redirect('/roles')