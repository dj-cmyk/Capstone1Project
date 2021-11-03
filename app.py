from flask import Flask, render_template, request, flash, redirect, session, g
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy.exc import IntegrityError

# from forms import UserAddForm, LoginForm, MessageForm, UserEditForm
from models import db, connect_db, Level, Production, Headpiece, CostumeGroup, Prop, Role, Role_Costume
from user_models import User


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'randomString101010'

debug = DebugToolbarExtension(app)

connect_db(app)



*************************************************************************************
# Routes
*************************************************************************************

@app.route('/')
def display_homepage():
    '''docstring'''
    return render_template('index.html')
