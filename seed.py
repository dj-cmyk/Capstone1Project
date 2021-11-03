from app import app
from models import db, Level, Production, Headpiece, CostumeGroup, Prop, Role, Role_Costume


db.drop_all()
db.create_all()

# ***************************************************************************
# seed for all ballet levels

l1 = Level(levelName="PCM")
l2 = Level(levelName="Pre-Ballet")
l3 = Level(levelName="Ballet 1")
l4 = Level(levelName="Boys Elementary Ballet")
l5 = Level(levelName="Ballet 2")
l6 = Level(levelName="Ballet 3")
l7 = Level(levelName="Ballet 4")
l8 = Level(levelName="Ballet 5")
l9 = Level(levelName="Ballet 6A")
l10 = Level(levelName="Ballet 6B1")
l11 = Level(levelName="Ballet 6B2")
l12 = Level(levelName="Ballet 7")
l13 = Level(levelName="Pre-Pro")
l14 = Level(levelName="Men")


# ***************************************************************************
# seed for all ballet productions

p1 = Production(
    name="Nutcracker",
    is_current=True
)

p2 = Production(
    name="Sleeping Beauty"
)

p3 = Production(
    name="Swan Lake"
)

p4 = Production(
    name="Don Quixote"
)

p5 = Production(
    name="Wonderful Wizard of Oz"
)

# ***************************************************************************


h1 = Headpiece(
    name="Sugar Plum Tiara",
    image_url="",
    description="pink rhinestone tiara with front point",
    quantity=1,
    current_location="Tiara Bin in Studio A Cupboard",
    storage_location="Tiara bin in Prop Room"
)



db.session.add_all([l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12, l13, l14, p1, p2, p3, p4, p5, h1 ])
db.session.commit()

c1 = CostumeGroup(
    name = "Sugar Plum Fairy Platter Tutus",
    image_url="",
    description="Pink platter tutus",
    quantity=2, 
    current_location="back room",
    storage_location="back room",
    color="pink",
    size_chart_url="",
    assignment_sheet_url="",
    headpiece_id = h1.id
)


db.session.add(c1)
db.session.commit()

r1 = Role(
    name = "Sugar Plum Fairy",
    production_id = p1.id,
    level_id = l13.id
)

db.session.add(r1)
db.session.commit()

rc1 = Role_Costume(
    role_id = r1.id,
    costume_group_id = c1.id
)

db.session.add(rc1)
db.session.commit()