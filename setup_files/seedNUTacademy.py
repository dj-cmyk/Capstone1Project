from app import app
from models import db, Headpiece, CostumeGroup, Prop, Role


# ***************************************************************************
# data for nutcracker academy headpieces
# ***************************************************************************

h1 = Headpiece(
    name="PCM Polichinelle Headband",
    image_url="/static/images/headpieces/nut_pcm_poli.jpg",
    description="Hot pink headband with pink, white, and green pompons",
    quantity=25,
    current_location="In Use",
    storage_location="Studio B Cupboard"
)

h2 = Headpiece(
    name="PCM Marzipan Headband",
    image_url="/static/images/headpieces/nut_pcm_marz.jpg",
    description="green trim headband with pink flowers",
    quantity=18,
    current_location="In Use",
    storage_location="Studio B Cupboard"
)

h3 = Headpiece(
    name="PCM Candy Cane Headband",
    image_url="/static/images/headpieces/nut_pcm_cc.jpg",
    description="red and white striped headband with candy decorations and white LED lights",
    quantity=18,
    current_location="Storage",
    storage_location="Studio B Cupboard"
)

h4 = Headpiece(
    name="PCM Sugar Plum Headband",
    image_url="/static/images/headpieces/nut_pcm_sugar.jpg",
    description="burgundy ribbon headband with pink and burgundy flowers",
    quantity=17,
    current_location="Storage",
    storage_location="Studio B Cupboard"
)

h5 = Headpiece(
    name="Pre-Ballet Snowflake Tiara",
    image_url="/static/images/headpieces/nut_preB.jpg",
    description="Small crystal rhinestone tiara ",
    quantity=21,
    current_location="In Use",
    storage_location="Studio B Cupboard"
)

h6 = Headpiece(
    name="B1 Party Girl Bows",
    image_url="/static/images/headpieces/nut_b1.jpg",
    description="ivory, red, dark blue, and light blue bows",
    quantity=35,
    current_location="In Use",
    storage_location="Studio B Cupboard"
)

h7 = Headpiece(
    name="B2 Polichinelle Hats",
    image_url="/static/images/headpieces/nut_b2.jpg",
    description="White sailor hats with pink pompons",
    quantity=23,
    current_location="In Use",
    storage_location="Studio B Cupboard"
)

h8 = Headpiece(
    name="B3 Candy Cane Hats",
    image_url="/static/images/headpieces/nut_b3.jpg",
    description="Red and White Striped pillbox hats",
    quantity=22,
    current_location="In Use",
    storage_location="Studio B Cupboard"
)

h9 = Headpiece(
    name="B4 Chinese Tea headpieces",
    image_url="/static/images/headpieces/nut_b4.jpg",
    description="Silver circular pipe cleaner cages with pink flowers and ribbons - pairs",
    quantity=18,
    current_location="In Use",
    storage_location="Studio B Cupboard"
)

h10 = Headpiece(
    name="B5 Party Girl Bows",
    image_url="/static/images/headpieces/nut_b5.jpg",
    description="Ivory ribbon bows",
    quantity=30,
    current_location="In Use",
    storage_location="Studio B Cupboard"
)



db.session.add_all([h1, h2, h3, h4, h5, h6, h7, h8, h9, h10])
db.session.commit()

# ***************************************************************************
# data for nutcracker academy props
# ***************************************************************************

prop1 = Prop(
    name = "Lambs",
    image_url = "/static/images/props/nut_lambs.jpg",
    description = "Soft stuffed lambs",
    quantity = 17,
    current_location = "In Use",
    storage_location = "Prop Room"
)

prop2 = Prop(
    name = "Floral Umbrellas",
    image_url = "/static/images/props/nut_umbrellas.jpg",
    description = "paper umbrellas with floral design",
    quantity = 17,
    current_location = "In Use",
    storage_location = "Prop Room",
)


db.session.add_all([prop1, prop2])
db.session.commit()

# ***************************************************************************
# data for nutcracker academy costume groups
# ***************************************************************************

c1 = CostumeGroup(
    name = "PCM Polichinelle Dresses",
    image_url="/static/images/costumes/nut_pcm_poli.jpg",
    description="Bright green spandex dresses with white accents, pink ribbon and pink pompon trim",
    quantity=24, 
    current_location="In Use",
    storage_location="Up Top in PCM area",
)

c2 = CostumeGroup(
    name = "PCM Marzipan Leotards",
    image_url="/static/images/costumes/nut_pcm_marz.jpg",
    description="Pink velvet leotard with white top and sleeves, pink and green trim",
    quantity=44, 
    current_location="In Use",
    storage_location="Up Top in PCM Area",
)

c3 = CostumeGroup(
    name = "PCM Marzipan Tutus",
    image_url="/static/images/costumes/nut_pcm_marz.jpg",
    description="White tutus with pink floral trim at waistband and pink and green ribbon trim",
    quantity=41, 
    current_location="In Use",
    storage_location="Up Top in PCM Area",
)

c4 = CostumeGroup(
    name = "PCM Candy Cane Leotards",
    image_url="/static/images/costumes/nut_pcm_cc.jpg",
    description="Red leotard with red and white striped tulle sleeve ruffles and white and rhinestone trim",
    quantity=31, 
    current_location="Storage",
    storage_location="Up Top in PCM Area",
)

c5 = CostumeGroup(
    name = "PCM Candy Cane Tutus",
    image_url="/static/images/costumes/nut_pcm_cc.jpg",
    description="Red and White striped tulle tutus",
    quantity=26, 
    current_location="Storage",
    storage_location="Up Top in PCM Area",
)

c6 = CostumeGroup(
    name = "PCM Sugar Plum Dresses",
    image_url="/static/images/costumes/nut_pcm_sp.jpg",
    description="Burgundy velvet leotard with pale pink center accent and pale pink attached tutu skirt, flowers at neckline",
    quantity=35, 
    current_location="Storage",
    storage_location="Up Top in PCM Area",
)

c7 = CostumeGroup(
    name = "PreBallet Snowflake Leotards",
    image_url="/static/images/costumes/nut_preB.jpg",
    description="white leotards with attached tulle sleeve ruffles and silver trim",
    quantity=30, 
    current_location="In Use",
    storage_location="Bin in Back Room",
)

c8 = CostumeGroup(
    name = "PreBallet Snowflake Tutus",
    image_url="/static/images/costumes/nut_preB.jpg",
    description="White tulle romantic style tutus with silver sparkle tulle overlay",
    quantity=30, 
    current_location="In Use",
    storage_location="Hanging in Studio A",
)

c9 = CostumeGroup(
    name = "Ballet 1 Party Girl Dresses",
    image_url="/static/images/costumes/nut_b1.jpg",
    description="Party Girl dresses in a base color of either red, ivory, light blue, or royal blue, with various colors of sashes",
    quantity=60, 
    current_location="In Use",
    storage_location="Hanging in Studio A",
)

c10 = CostumeGroup(
    name = "Ballet 2 Polichinelle Dresses",
    image_url="/static/images/costumes/nut_b2.jpg",
    description="Bright green satin dresses with white underskirt, pink ribbon trim and pink pompons",
    quantity=35, 
    current_location="In Use",
    storage_location="Hanging in Studio A",
)

c11 = CostumeGroup(
    name = "Ballet 3 Candy Cane Leotards",
    image_url="/static/images/costumes/nut_b3.jpg",
    description="Red leotards with white trim and red and white striped candies",
    quantity=42, 
    current_location="In Use",
    storage_location="Bins in Back Room",
)

c12 = CostumeGroup(
    name = "Ballet 3 Candy Cane Tutus",
    image_url="/static/images/costumes/nut_b3.jpg",
    description="Red and White striped tulle tutus",
    quantity=31, 
    current_location="In Use",
    storage_location="Bins in Back Room",
)

c13 = CostumeGroup(
    name = "Ballet 3 Candy Cane Arm Puffs",
    image_url="/static/images/costumes/nut_b3.jpg",
    description="Red and White striped tulle arm puffs - pairs",
    quantity=18, 
    current_location="In Use",
    storage_location="Studio B Cupboard",
)

c14 = CostumeGroup(
    name = "Ballet 4 Chinese Tea Tunics",
    image_url="/static/images/costumes/nut_b4.jpg",
    description="Dark blue and silver damask fabric tunic with hot pink frog closures",
    quantity=28, 
    current_location="In Use",
    storage_location="Hanging in Studio A",
)

c15 = CostumeGroup(
    name = "Chinese Tea Leggings",
    image_url="/static/images/costumes/nut_leggings.jpg",
    description="Hot Pink Leggings",
    quantity=59, 
    current_location="In Use",
    storage_location="Hanging in Studio A",
)

c16 = CostumeGroup(
    name = "Ballet 5 Party Girls",
    image_url="/static/images/costumes/nut_b5.jpg",
    description="Ivory Party Girl dresses with sashes in various colors",
    quantity=48, 
    current_location="In Use",
    storage_location="Hanging in Studio A",
)

c17 = CostumeGroup(
    name = "White Bloomers",
    image_url="/static/images/costumes/nut_bloomers.jpg",
    description="White bloomers with iridescent lace trim",
    quantity=39, 
    current_location="In Use",
    storage_location="Bin in Back Room",
)



db.session.add_all([c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17])
db.session.commit()

# ***************************************************************************
# data for nutcracker academy roles
# ***************************************************************************


r1 = Role(
    name = "PCM Little Polichinelles",
    production_id = 1,
    level_id = 1,
    cg1_id = c1.id,
    headpiece_id = h1.id, 
)

r2 = Role(
    name = "PCM Little Marzipan",
    production_id = 1,
    level_id = 1,
    cg1_id = c2.id,
    cg2_id = c3.id,
    headpiece_id = h2.id, 
    prop_id = prop1.id
)

r3 = Role(
    name = "PCM Little Candy Canes",
    production_id = 1,
    level_id = 1,
    cg1_id = c4.id,
    cg2_id = c5.id,
    headpiece_id = h3.id, 
)

r4 = Role(
    name = "PCM Little Sugar Plum Fairies",
    production_id = 1,
    level_id = 1,
    cg1_id = c6.id,
    headpiece_id = h4.id, 
    prop_id = 5
)

r5 = Role(
    name = "Pre-Ballet Snowflakes",
    production_id = 1,
    level_id = 2, 
    cg1_id = c7.id,
    cg2_id = c8.id,
    headpiece_id = h5.id, 
)

r6 = Role(
    name = "Ballet 1 Party Girls",
    production_id = 1,
    level_id = 3,
    cg1_id = c9.id,
    headpiece_id = h6.id, 
)

r7 = Role(
    name = "Ballet 2 Polichinelles",
    production_id = 1,
    level_id = 5, 
    cg1_id = c10.id,
    headpiece_id = h7.id, 
)

r8 = Role(
    name = "Ballet 3 Candy Canes",
    production_id = 1,
    level_id = 6,
    cg1_id = c11.id,
    cg2_id = c12.id,
    cg3_id = c13.id,
    headpiece_id = h8.id, 
)

r9 = Role(
    name = "Ballet 4 Chinese Tea",
    production_id = 1,
    level_id = 7,
    cg1_id = c14.id,
    cg2_id = c15.id,
    headpiece_id = h9.id, 
    prop_id = prop2.id
)

r10 = Role(
    name = "Ballet 5 Party Girls",
    production_id = 1,
    level_id = 8,
    cg1_id = c16.id,
    cg2_id = c17.id,
    headpiece_id = h10.id, 
)

db.session.add_all([r1, r2, r3, r4, r5, r6, r7, r8, r9, r10])
db.session.commit()