from app import app
from models import db, Level, Production, Headpiece, CostumeGroup, Prop, Role


# ***************************************************************************
# data for sleeping beauty headpieces
# ***************************************************************************


sb_6a_h = Headpiece(
    name="Emerald green and white floral and tulle headpiece",
    image_url="/static/images/headpieces/default.jpg",
    description="Emerald green tulle with white flower and gold trim",
    quantity=12,
    current_location="Storage",
    storage_location="Up Top in Sleeping Beauty Area"
)

sb_6b1_h = Headpiece(
    name="Yellow floral headpiece",
    image_url="/static/images/headpieces/default.jpg",
    description="yellow floral headpiece with small rhinestones",
    quantity=21,
    current_location="Storage",
    storage_location="Up Top in Sleeping Beauty Area"
)

sb_6b1_h2 = Headpiece(
    name="Pink floral headpiece with LED lights",
    image_url="/static/images/headpieces/default.jpg",
    description="larger pink floral headpiece with LED lights",
    quantity=20,
    current_location="Storage",
    storage_location="Up Top in Sleeping Beauty Area"
)

sb_6b2_h = Headpiece(
    name="purple and yellow floral rainbows",
    image_url="/static/images/headpieces/default.jpg",
    description="purple and yellow flowers in a rainbow shape that goes over the bun, with long ribbons hanging down the back",
    quantity=26,
    current_location="Storage",
    storage_location="Up Top in Sleeping Beauty Area"
)

sb_b7_h = Headpiece(
    name="lavender floral headpiece",
    image_url="/static/images/headpieces/default.jpg",
    description="lavender floral bunch for side of the bun",
    quantity=20,
    current_location="Storage",
    storage_location="Up Top in Sleeping Beauty Area"
)

sb_pp_h1 = Headpiece(
    name="purple and yellow floral crown",
    image_url="/static/images/headpieces/default.jpg",
    description="dark and light purple flowers with yellow accent flowers and purple ribbons, purple and yellow ribbons trailing down the back",
    quantity=8,
    current_location="Storage",
    storage_location="Up Top in Sleeping Beauty Area"
)

sb_pp_h2 = Headpiece(
    name="rhinestone tiara with floral edges",
    image_url="/static/images/headpieces/default.jpg",
    description="various color florals on rhinestone tiaras to match various color bodices",
    quantity=9,
    current_location="Storage",
    storage_location="Prop Room"
)

sb_pp_h3 = Headpiece(
    name="green and white floral piece with separate rhinestone 'v'",
    image_url="/static/images/headpieces/default.jpg",
    description="green and white floral headpieces with separate rhinestone 'v' shape a the front of the head",
    quantity=10,
    current_location="Storage",
    storage_location="Up Top in Sleeping Beauty Area"
)

sb_lilacfairy_h = Headpiece(
    name="Lilac Fairy - rhinestone and purple floral tiara in 3 parts",
    image_url="/static/images/headpieces/default.jpg",
    description="rhinestone and purple floral tiara in 3 parts",
    quantity=1,
    current_location="Storage",
    storage_location="Bin in back room"
)

sb_queen_h = Headpiece(
    name="Queen - Tall Crystal AB Rhinestone Tiara",
    image_url="/static/images/headpieces/default.jpg",
    description="tall rhinestone tiara with crystal AB rhinestones",
    quantity=1,
    current_location="Storage",
    storage_location="Bin in back room"
)

sb_bluebird_h = Headpiece(
    name="Bluebird - crystal AB and pale blue rhinestone tiara in 2 parts",
    image_url="/static/images/headpieces/default.jpg",
    description="crystal AB and pale blue rhinestone tiara in 2 parts",
    quantity=21,
    current_location="Storage",
    storage_location="Bin in back room"
)

db.session.add_all([h1, h2, h3, h4, h5, h6, h7, h8, h9])
db.session.commit()

# ***************************************************************************
# data for sleeping beauty props
# ***************************************************************************

prop1 = Prop(
    name = "Purple Fairy Ball Baskets"
    image_url = 
    description = "Grapevine twine ball shaped baskets with purple flowers, ribbons, rhinestones, and purple LED lights"
    quantity = 34
    current_location = "Storage"
    storage_location = "Up Top in Sleeping Beauty Area"
)

db.session.add_all([prop1])
db.session.commit()

# ***************************************************************************
# data for sleeping beauty costume groups
# ***************************************************************************

c1 = CostumeGroup(
    name = "PCM Little Lilac Fairies Leotards",
    image_url="/static/images/costumes/sleepingBeautyPCMclose.jpg",
    description="Pink leotards with pink sleeve ruffles and purple floral trim",
    quantity=20, 
    current_location="Storage",
    storage_location="Up Top in Sleeping Beauty Area",
)

c2 = CostumeGroup(
    name = "PCM Little Lilac Fairies Tutus",
    image_url="/static/images/costumes/sleepingBeautyPCM.jpg",
    description="3 layer tulle skirt in various shades of purple with purple ribbon trim at the base and purple floral trim at the waistband",
    quantity=20, 
    current_location="Storage",
    storage_location="Up Top in Sleeping Beauty Area",
)

c3 = CostumeGroup(
    name = "Pre-Ballet Young Lilac Fairies Attendants",
    image_url="/static/images/costumes/sleepingBeautyPreBallet.jpg",
    description="Purple velvet leotards with attached purple tutu",
    quantity=38, 
    current_location="Storage",
    storage_location="Up Top in Sleeping Beauty Area",
)



db.session.add_all([c1, c2, c3])
db.session.commit()

# ***************************************************************************
# data for sleeping beauty costume groups
# ***************************************************************************


sb_PCM = Role(
    name = "PCM Little Lilac Fairies",
    production_id = p2.id,
    level_id = l1.id
    costume_group_first_id = c1.id,
    costume_group_second_id = c2.id,
    headpiece_id = h1.id, 
    prop_id = prop1.id
)

sb_PreB = Role(
    name = "Pre-Ballet Lilac Fairy Attendants",
    production_id = p2.id,
    level_id = l2.id, 
    costume_group_first_id = c3.id,
    headpiece_id = h2.id, 
    prop_id = prop2.id
)

sb_b1 = Role(
    name = "Ballet 1 Sapphire Jewels",
    production_id = p2.id,
    level_id = l1.id
    costume_group_first_id = c1.id,
    costume_group_second_id = c2.id,
    headpiece_id = h1.id, 
    prop_id = prop1.id
)

sb_b2 = Role(
    name = "PCM Little Lilac Fairies",
    production_id = p2.id,
    level_id = l1.id
    costume_group_first_id = c1.id,
    costume_group_second_id = c2.id,
    headpiece_id = h1.id, 
    prop_id = prop1.id
)

sb_b3 = Role(
    name = "PCM Little Lilac Fairies",
    production_id = p2.id,
    level_id = l1.id
    costume_group_first_id = c1.id,
    costume_group_second_id = c2.id,
    headpiece_id = h1.id, 
    prop_id = prop1.id
)

sb_b4 = Role(
    name = "PCM Little Lilac Fairies",
    production_id = p2.id,
    level_id = l1.id
    costume_group_first_id = c1.id,
    costume_group_second_id = c2.id,
    headpiece_id = h1.id, 
    prop_id = prop1.id
)

sb_b5 = Role(
    name = "PCM Little Lilac Fairies",
    production_id = p2.id,
    level_id = l1.id
    costume_group_first_id = c1.id,
    costume_group_second_id = c2.id,
    headpiece_id = h1.id, 
    prop_id = prop1.id
)

db.session.add_all([sb_PCM, sb_PreB, sb_b1, sb_b2, sb_b3, sb_b4, sb_b5])
db.session.commit()