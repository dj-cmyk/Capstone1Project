"""SQLAlchemy models for Costume Inventory DB Management App."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Level(db.Model):
    """docstring"""

    __tablename__ = 'levels'

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    levelName = db.Column(
        db.Text,
        nullable=False,
        unique=True,
    )



class Production(db.Model):
    '''docstring'''

    __tablename__ = 'productions'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.Text,
        nullable=False,
        unique=True
    )

    is_current = db.Column(
        db.Boolean,
        nullable=False,
        default=False
    )



class Headpiece(db.Model):
    '''docstring'''

    __tablename__ = 'headpieces'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.Text, 
        nullable=False
    )

    image_url = db.Column(
        db.Text,
        default="/static/images/***************",
    )

    description = db.Column(
        db.Text,
    )

    quantity = db.Column(
        db.Integer, 
        nullable=False
    )

    current_location = db.Column(
        db.Text, 
        nullable=False
    )

    storage_location = db.Column(
        db.Text, 
        nullable=False
    )



class CostumeGroup(db.Model):
    '''docstring'''

    __tablename__ = 'costume_groups'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.Text, 
        nullable=False
    )

    image_url = db.Column(
        db.Text,
        default="/static/images/***************",
    )

    description = db.Column(
        db.Text,
    )

    quantity = db.Column(
        db.Integer, 
        nullable=False
    )

    current_location = db.Column(
        db.Text, 
        nullable=False
    )

    storage_location = db.Column(
        db.Text, 
        nullable=False
    )

    color = db.Column(
        db.Text,
    )

    size_chart_url = db.Column(
        db.Text, 
        default="/static/images/***************",
    )

    assignment_sheet_url = db.Column(
        db.Text, 
        default="/static/images/***************",
    )

    headpiece_id = db.Column(
        db.Integer,
        db.ForeignKey('headpieces.id', ondelete='SET NULL'),
    )


class Prop(db.Model):
    '''docstring'''

    __tablename__ = 'props'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.Text, 
        nullable=False
    )

    image_url = db.Column(
        db.Text,
        default="/static/images/***************",
    )

    description = db.Column(
        db.Text,
    )

    quantity = db.Column(
        db.Integer, 
        nullable=False
    )

    current_location = db.Column(
        db.Text, 
        nullable=False
    )

    storage_location = db.Column(
        db.Text, 
        nullable=False
    )

    costume_group_id = db.Column(
        db.Integer,
        db.ForeignKey('costume_groups.id', ondelete='SET NULL'),
    )



class Role(db.Model):
    '''docstring'''

    __tablename__ = 'roles'

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    name = db.Column(
        db.Text, 
        nullable=False
    )

    production_id = db.Column(
        db.Integer,
        db.ForeignKey('productions.id', ondelete='SET NULL'),
    )

    level_id = db.Column(
        db.Integer,
        db.ForeignKey('levels.id', ondelete='SET NULL'),
    )


class Role_Costume(db.Model):
    '''docstring'''

    __tablename__ = 'roles_costumes'

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    role_id = db.Column(
        db.Integer,
        db.ForeignKey('roles.id', ondelete='SET NULL'),
    )

    costume_group_id = db.Column(
        db.Integer,
        db.ForeignKey('costume_groups.id', ondelete='SET NULL'),
    )




def connect_db(app):
    """Connect this database to Flask app """

    db.app = app
    db.init_app(app)
