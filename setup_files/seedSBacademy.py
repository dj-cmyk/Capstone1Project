from app import app
from models import db, Level, Production, Headpiece, CostumeGroup, Prop, Role


# ***************************************************************************
# data for sleeping beauty academy headpieces
# ***************************************************************************

h1 = Headpiece(
    name="PCM Purple Floral Headband",
    image_url="/static/images/headpieces/sb_pcm.jpg",
    description="purple floral headband with gems",
    quantity=18,
    current_location="Storage",
    storage_location="Up Top in Sleeping Beauty Area"
)

h2 = Headpiece(
    name="Pre-Ballet Purple Floral Headband",
    image_url="/static/images/headpieces/sb_preB.jpg",
    description="dark and light purple flowers with a pink flower on a purple headband (matches their tutu trim)",
    quantity=21,
    current_location="Storage",
    storage_location="Up Top in Sleeping Beauty Area"
)

h3 = Headpiece(
    name="Silver and Sapphire tiara - small",
    image_url="/static/images/headpieces/sb_b1.jpg",
    description="small silver tiara with sapphire rhinestones",
    quantity=20,
    current_location="Storage",
    storage_location="Up Top in Sleeping Beauty Area"
)

h4 = Headpiece(
    name="Yellow Pink and White floral headpiece",
    image_url="/static/images/headpieces/sb_b2.jpg",
    description="triangular shape floral headpiece with white, pink, and yellow flowers on a green base",
    quantity=20,
    current_location="Storage",
    storage_location="Up Top in Sleeping Beauty Area"
)

h5 = Headpiece(
    name="Gold and White whimisacal floral headpieces",
    image_url="/static/images/headpieces/sb_b3.jpg",
    description="Gold and White whimsical floral headpieces",
    quantity=20,
    current_location="Storage",
    storage_location="Up Top in Sleeping Beauty Area"
)

h6 = Headpiece(
    name="Blue and Lavender Floral headpiece",
    image_url="/static/images/headpieces/sb_b4.jpg",
    description="blue and lavender floral headpiece on felt base, sits closer to the back of the head",
    quantity=16,
    current_location="Storage",
    storage_location="Up Top in Sleeping Beauty Area"
)

h7 = Headpiece(
    name="Burgundy, white, and gold floral headpiece",
    image_url="/static/images/headpieces/sb_b5.jpg",
    description="burgundy, white, and large gold floral headpiece sits closer to the back of the head",
    quantity=20,
    current_location="Storage",
    storage_location="Up Top in Sleeping Beauty Area"
)



db.session.add_all([h1, h2, h3, h4, h5, h6, h7])
db.session.commit()

# ***************************************************************************
# data for sleeping beauty academy props
# ***************************************************************************

prop1 = Prop(
    name = "Purple Fairy Ball Baskets",
    image_url = "/static/images/props/sb_pcm.jpg",
    description = "Grapevine twine ball shaped baskets with purple flowers, ribbons, rhinestones, and purple LED lights",
    quantity = 34,
    current_location = "Storage",
    storage_location = "Up Top in Sleeping Beauty Area"
)

prop2 = Prop(
    name = "Purple Fairy Wands",
    image_url = "/static/images/props/sb_preB.jpg",
    description = "purple roses on green wands with ribbons, gold leaves, and purple LED lights - pairs",
    quantity = 20,
    current_location = "Prop Room",
    storage_location = "Prop Room",
)

prop3 = Prop(
    name = "Silver Star Wands",
    image_url = "/static/images/props/sb_b1.jpg",
    description = "Silver star wands with long handles, blue and silver ribbon streamers, white LED lights - pairs",
    quantity = 20,
    current_location = "Prop Room",
    storage_location = "Prop Room",
)

prop4 = Prop(
    name = "Handheld Candles",
    image_url = "/static/images/props/sb_b2.jpg",
    description = "White handheld candles with yellow, pink, and green floral decorations - pairs",
    quantity = 16,
    current_location = "Storage",
    storage_location = "Up Top in Sleeping Beauty Area",
)

prop5 = Prop(
    name = "White and Gold wrist Corsage",
    image_url = "/static/images/props/sb_b3.jpg",
    description = "White and Gold wrist corsage with gold ribbon and leaf trim streamers, white LED lights",
    quantity = 20,
    current_location = "Storage",
    storage_location = "Bin in Studio B Cupboard",
)

db.session.add_all([prop1, prop2, prop3, prop4, prop5])
db.session.commit()

# ***************************************************************************
# data for sleeping beauty costume groups
# ***************************************************************************

c1 = CostumeGroup(
    name = "PCM Little Lilac Fairies Leotards",
    image_url="/static/images/costumes/sb_pcm.jpg",
    description="Pink leotards with pink sleeve ruffles and purple floral trim",
    quantity=20, 
    current_location="Storage",
    storage_location="Up Top in Sleeping Beauty Area",
)

c2 = CostumeGroup(
    name = "PCM Little Lilac Fairies Tutus",
    image_url="/static/images/costumes/sb_pcm.jpg",
    description="3 layer tulle skirt in various shades of purple with purple ribbon trim at the base and purple floral trim at the waistband",
    quantity=20, 
    current_location="Storage",
    storage_location="Up Top in Sleeping Beauty Area",
)

c3 = CostumeGroup(
    name = "Pre-Ballet Young Lilac Fairies Attendants",
    image_url="/static/images/costumes/sb_preB.jpg",
    description="Purple velvet leotards with attached purple tutu",
    quantity=38, 
    current_location="Storage",
    storage_location="Up Top in Sleeping Beauty Area",
)

c4 = CostumeGroup(
    name = "Ballet 1 Blue Sapphire Leotards",
    image_url="/static/images/costumes/sb_b1.jpg",
    description="Royal Blue Leotards with attached sparkle tulle arm ruffles and white and silver trim with single sapphire rhinestone",
    quantity=37, 
    current_location="Storage",
    storage_location="Up Top in Sleeping Beauty Area",
)

c5 = CostumeGroup(
    name = "Ballet 1 Blue Sapphire Tutus",
    image_url="/static/images/costumes/sb_b1.jpg",
    description="Royal blue pull on platter tutu with sparkle tull overlay",
    quantity=31, 
    current_location="Storage",
    storage_location="White House",
)

c6 = CostumeGroup(
    name = "Ballet 2 Green, Yellow, and Pink Forest Fairy Dresses",
    image_url="/static/images/costumes/sb_b2.jpg",
    description="Green velvet leotard with yellow and gold center panel and pink, white, and yellow floral trim, pink, green, and yellow attached tulle skirt",
    quantity=35, 
    current_location="Storage",
    storage_location="Up Top in Sleeping Beauty Area",
)

c7 = CostumeGroup(
    name = "Ballet 2 Green, Yellow, and Pink Forest Fairy Arm Puffs",
    image_url="/static/images/costumes/sb_b2.jpg",
    description="yellow tulle with pink and green floral trim arm puffs in 2 sizes - pairs",
    quantity=20, 
    current_location="Storage",
    storage_location="Up Top in Sleeping Beauty Area",
)

c8 = CostumeGroup(
    name = "Ballet 3 Navy, Ivory, and Gold Princess Dresses",
    image_url="/static/images/costumes/sb_b3.jpg",
    description="Navy velvet leotard with attached ivory tulle and crinoline skirt and navy velvet peplum, gold floral trim",
    quantity=35, 
    current_location="Storage",
    storage_location="Up Top in Sleeping Beauty Area",
)

c9 = CostumeGroup(
    name = "Ballet 4 Lavender Leotards",
    image_url="/static/images/costumes/sb_b4.jpg",
    description="Lavender camisole leotard with lavender and blue floral and silver leaf trim",
    quantity=24, 
    current_location="Storage",
    storage_location="Up Top in Sleeping Beauty Area",
)

c10 = CostumeGroup(
    name = "Ballet 4 Lilac Fairy Attendant Tutus",
    image_url="/static/images/costumes/sb_b4.jpg",
    description="romantic-style tutus with elastic waistbands in lavender and purple shades",
    quantity=23, 
    current_location="Storage",
    storage_location="Up Top in Sleeping Beauty Area",
)

c11 = CostumeGroup(
    name = "Ballet 4 Lilac Fairy Attendant Arm Puffs",
    image_url="/static/images/costumes/sb_b4.jpg",
    description="lavender tulle with gold trim arm puffs, elastic on top and bottom - pairs",
    quantity=16, 
    current_location="Storage",
    storage_location="Up Top in Sleeping Beauty Area",
)

c12 = CostumeGroup(
    name = "Burgundy and Gold dresses",
    image_url="/static/images/costumes/sb_b5.jpg",
    description="Burgundy crushed velvet leotard with gold lace and gold flowers, tiered gold lace skirt with burgundy and ivory tulle and crinoline",
    quantity=82, 
    current_location="Storage",
    storage_location="Up Top",
)

c13 = CostumeGroup(
    name = "Gold lace Arm Puffs",
    image_url="/static/images/costumes/sb_b5.jpg",
    description="Gold Lace arm puffs made with the same lace as the burgundy dress skirts",
    quantity=20, 
    current_location="Storage",
    storage_location="Up Top",
)



db.session.add_all([c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12])
db.session.commit()

# ***************************************************************************
# data for sleeping beauty costume groups
# ***************************************************************************


sb_PCM = Role(
    name = "PCM Little Lilac Fairies",
    production_id = 2,
    level_id = 1,
    cg1_id = c1.id,
    cg2_id = c2.id,
    headpiece_id = h1.id, 
    prop_id = prop1.id
)

sb_PreB = Role(
    name = "Pre-Ballet Lilac Fairy Attendants",
    production_id = 2,
    level_id = 2, 
    cg1_id = c3.id,
    headpiece_id = h2.id, 
    prop_id = prop2.id
)

sb_b1 = Role(
    name = "Ballet 1 Sapphire Jewels",
    production_id = 2,
    level_id = 3,
    cg1_id = c4.id,
    cg2_id = c5.id,
    headpiece_id = h3.id, 
    prop_id = prop3.id
)

sb_b2 = Role(
    name = "Ballet 2 Forest Fairies",
    production_id = 2,
    level_id = 5, 
    cg1_id = c6.id,
    cg3_id = c7.id,
    headpiece_id = h4.id, 
    prop_id = prop4.id
)

sb_b3 = Role(
    name = "Ballet 3 Princesses",
    production_id = 2,
    level_id = 6,
    cg1_id = c8.id,
    headpiece_id = h5.id, 
    prop_id = prop5.id
)

sb_b4 = Role(
    name = "Ballet 4 Lilac Fairy Attendants",
    production_id = 2,
    level_id = 7,
    cg1_id = c9.id,
    cg2_id = c10.id,
    cg3_id = c11.id,
    headpiece_id = h6.id, 
)

sb_b5 = Role(
    name = "Ballet 5 Aurora's Bridesmaids",
    production_id = 2,
    level_id = 8,
    cg1_id = c12.id,
    cg3_id = c13.id,
    headpiece_id = h7.id, 
)

db.session.add_all([sb_PCM, sb_PreB, sb_b1, sb_b2, sb_b3, sb_b4, sb_b5])
db.session.commit()