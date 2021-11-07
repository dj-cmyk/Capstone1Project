from app import app
from models import db, Level, Production, Headpiece, CostumeGroup, Prop, Role


db.drop_all()
db.create_all()

# ***************************************************************************
# seed for all ballet levels

l1 = Level(name="PCM")
l2 = Level(name="Pre-Ballet")
l3 = Level(name="Ballet 1")
l4 = Level(name="Boys Elementary Ballet")
l5 = Level(name="Ballet 2")
l6 = Level(name="Ballet 3")
l7 = Level(name="Ballet 4")
l8 = Level(name="Ballet 5")
l9 = Level(name="Ballet 6A")
l10 = Level(name="Ballet 6B1")
l11 = Level(name="Ballet 6B2")
l12 = Level(name="Ballet 7")
l13 = Level(name="Pre-Pro")
l14 = Level(name="Men")

db.session.add_all([l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12, l13, l14])
db.session.commit()

# ***************************************************************************
# seed for all ballet productions

p1 = Production(
    name="Nutcracker",
    is_current=True,
    last_performed=2020,
    image_url="/static/images/productions/nutcracker.jpg"
)

p2 = Production(
    name="Sleeping Beauty",
    last_performed=2021,
    image_url="/static/images/productions/sleepingBeauty.jpg"
)

p3 = Production(
    name="Swan Lake",
    last_performed=2018,
    image_url="/static/images/productions/swanLake.jpg"
)

p4 = Production(
    name="Don Quixote",
    last_performed=2019,
)

p5 = Production(
    name="Wonderful Wizard of Oz",
    last_performed=2016,
)

db.session.add_all([p1, p2, p3, p4, p5])
db.session.commit()

