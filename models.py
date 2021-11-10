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

    name = db.Column(
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

    last_performed = db.Column(
        db.Integer
    )

    image_url = image_url = db.Column(
        db.Text,
        default="/static/images/productions/default.jpg",
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
        default="/static/images/headpieces/default.jpg",
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
        default="/static/images/costumes/default.jpg",
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

    assignment_sheet_url = db.Column(
        db.Text, 
        default="/static/assignmentSheets/default.pdf",
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
        default="/static/images/props/default.jpg",
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
        db.ForeignKey('productions.id'),
        nullable=False
    )

    level_id = db.Column(
        db.Integer,
        db.ForeignKey('levels.id'),
        nullable=False
    )

    cg1_id = db.Column(
        db.Integer,
        db.ForeignKey('costume_groups.id'),
        nullable=False
    )

    cg2_id = db.Column(
        db.Integer,
        db.ForeignKey('costume_groups.id'),
    )

    cg3_id = db.Column(
        db.Integer,
        db.ForeignKey('costume_groups.id'),
    )

    headpiece_id = db.Column(
        db.Integer,
        db.ForeignKey('headpieces.id'),
        nullable=False
    )

    prop_id = db.Column(
        db.Integer,
        db.ForeignKey('props.id'),
    )

    costume = db.relationship('CostumeGroup', foreign_keys=[cg1_id], backref='roles')
    skirt = db.relationship('CostumeGroup', foreign_keys=[cg2_id])
    armpuffs = db.relationship('CostumeGroup', foreign_keys=[cg3_id])
    prop = db.relationship('Prop', backref='roles')
    level = db.relationship('Level', backref='roles')
    headpiece = db.relationship('Headpiece', backref='roles')
    production = db.relationship('Production', backref='roles')




def connect_db(app):
    """Connect this database to Flask app """

    db.app = app
    db.init_app(app)
