from app import app
from models import db, Headpiece, CostumeGroup, Prop, Role


# ***************************************************************************
# data for sleeping beauty dvbt headpieces
# ***************************************************************************


h1 = Headpiece(
    name="Emerald green and white floral and tulle headpiece",
    image_url="/static/images/headpieces/sb_6a",
    description="Emerald green tulle with white flower and gold trim",
    quantity=12,
    current_location="Storage",
    storage_location="Up Top in Sleeping Beauty Area"
)

h2 = Headpiece(
    name="Yellow floral headpiece",
    image_url="/static/images/headpieces/sb_6b1.jpg",
    description="yellow floral headpiece with small rhinestones",
    quantity=21,
    current_location="Storage",
    storage_location="Up Top in Sleeping Beauty Area"
)

h3 = Headpiece(
    name="Pink floral headpiece with LED lights",
    image_url="/static/images/headpieces/sb_6b1_pink.jpg",
    description="larger pink floral headpiece with LED lights",
    quantity=20,
    current_location="Storage",
    storage_location="Up Top in Sleeping Beauty Area"
)

h4 = Headpiece(
    name="purple and yellow floral rainbows",
    image_url="/static/images/headpieces/sb_6b2.jpg",
    description="purple and yellow flowers in a rainbow shape that goes over the bun, with long ribbons hanging down the back",
    quantity=26,
    current_location="Storage",
    storage_location="Up Top in Sleeping Beauty Area"
)

h5 = Headpiece(
    name="lavender floral headpiece",
    image_url="/static/images/headpieces/sb_b7.jpg",
    description="lavender floral bunch for side of the bun",
    quantity=20,
    current_location="Storage",
    storage_location="Up Top in Sleeping Beauty Area"
)

h6 = Headpiece(
    name="purple and yellow floral crown",
    image_url="/static/images/headpieces/sb_ds_bridesmaids.jpg",
    description="dark and light purple flowers with yellow accent flowers and purple ribbons, purple and yellow ribbons trailing down the back",
    quantity=8,
    current_location="Storage",
    storage_location="Up Top in Sleeping Beauty Area"
)

h7 = Headpiece(
    name="rhinestone tiara with floral edges",
    image_url="/static/images/headpieces/sb_s_princesses.jpg",
    description="various color florals on rhinestone tiaras to match various color bodices",
    quantity=9,
    current_location="Storage",
    storage_location="Prop Room"
)

h8 = Headpiece(
    name="green and white floral piece with separate rhinestone 'v'",
    image_url="/static/images/headpieces/sb_fairies.jpg",
    description="green and white floral headpieces with separate rhinestone 'v' shape a the front of the head",
    quantity=10,
    current_location="Storage",
    storage_location="Up Top in Sleeping Beauty Area"
)

h9 = Headpiece(
    name="Lilac Fairy - rhinestone and purple floral tiara in 3 parts",
    image_url="/static/images/headpieces/lilac_headpiece.jpg",
    description="rhinestone and purple floral tiara in 3 parts",
    quantity=1,
    current_location="Storage",
    storage_location="Bin in back room"
)

h10 = Headpiece(
    name="Queen - Tall Crystal AB Rhinestone Tiara",
    image_url="/static/images/headpieces/queen_headpiece.jpg",
    description="tall rhinestone tiara with crystal AB rhinestones",
    quantity=1,
    current_location="Storage",
    storage_location="Bin in back room"
)

h11 = Headpiece(
    name="Bluebird - crystal AB and pale blue rhinestone tiara in 2 parts",
    image_url="/static/images/headpieces/bluebird_headpiece.jpg",
    description="crystal AB and pale blue rhinestone tiara in 2 parts",
    quantity=1,
    current_location="Storage",
    storage_location="Bin in back room"
)

h12 = Headpiece(
    name="Aurora - Birthday Tiara",
    image_url="/static/images/headpieces/sb_aurora_birthday.jpg",
    description="crystal AB and pink rhinestone tiara",
    quantity=1,
    current_location="Storage",
    storage_location="Bin in back room"
)

h13 = Headpiece(
    name="Aurora - Wedding Tiara",
    image_url="/static/images/headpieces/sb_aurora_wedding.jpg",
    description="2 layered rhinestone and crystal tiara",
    quantity=1,
    current_location="Storage",
    storage_location="Bin in back room"
)

h14 = Headpiece(
    name="Carabosse Tiara",
    image_url="/static/images/headpieces/sb_carabosse.jpg",
    description="2 layered rhinestone and crystal tiara, same as Aurora Wedding Tiara",
    quantity=1,
    current_location="Storage",
    storage_location="Tiara Bin in prop room"
)

h15 = Headpiece(
    name="Jewels Headpieces",
    image_url="/static/images/headpieces/sb_jewels.jpg",
    description="half circle rhinestone tiaras in several colors",
    quantity=6,
    current_location="Storage",
    storage_location="Tiara Bin in prop room"
)

db.session.add_all([h1, h2, h3, h4, h5, h6, h7, h8, h9, h10, h11, h12, h13, h14, h15])
db.session.commit()

# ***************************************************************************
# data for sleeping beauty props
# ***************************************************************************

prop1 = Prop(
    name = "Garlands",
    image_url = "/static/images/props/sb_garlands.jpg",
    description = "half circle green hoop with yellow, white, and pink flowers",
    quantity = 9,
    current_location = "Storage",
    storage_location = "Up Top in Sleeping Beauty Area"
)

prop2 = Prop(
    name = "Lilac Fairy Wand",
    image_url = "/static/images/props/lilac_fairy_wand.jpg",
    description = "silver wand with purple flowers and purple LED lights",
    quantity = 1,
    current_location = "Storage",
    storage_location = "Bin in Back Room"
)

prop3 = Prop(
    name = "Baby Princess Aurora",
    image_url = "/static/images/props/sb_baby.jpg",
    description = "Princess Aurora baby doll in pink and white christening gown",
    quantity = 1,
    current_location = "Storage",
    storage_location = "Prop Room"
)

prop4 = Prop(
    name = "Spindle",
    image_url = "/static/images/props/sb_spindle.jpg",
    description = "spindle with blue ribbons and rhinestones",
    quantity = 1,
    current_location = "Storage",
    storage_location = "Prop Room"
)

db.session.add_all([prop1, prop2, prop3, prop4])
db.session.commit()

# ***************************************************************************
# data for sleeping beauty costume groups
# ***************************************************************************

c1 = CostumeGroup(
    name = "Emerald Green Dresses",
    image_url="/static/images/costumes/sb_6a.jpg",
    description="Emerald Green velvet leotard with green sequins, gold trim, and attached green tulle and crinoline romantic length tutu",
    quantity=35, 
    current_location="Storage",
    storage_location="Hanging in Studio B",
)

c111 = CostumeGroup(
    name = "Emerald Green Arm Puffs",
    image_url="/static/images/costumes/sb_6a.jpg",
    description="Emerald Green tulle arm puffs with white flowers and gold trim in 2 sizes - pairs",
    quantity=21, 
    current_location="Storage",
    storage_location="Up Top in Sleeping Beauty Area",
)

c2 = CostumeGroup(
    name = "Yellow Fairy Dresses",
    image_url="/static/images/costumes/sb_6b1.jpg",
    description="yellow velvet leotard with tulle sleeve ruffles and attached pink and yellow tulle and crinoline romantic length tutu",
    quantity=33, 
    current_location="Storage",
    storage_location="Hanging in Studio B",
)

c3 = CostumeGroup(
    name = "Purple Juliet Dresses",
    image_url="/static/images/costumes/sb_6b2.jpg",
    description="Purple velvet empire waist dresses with gold lace overlay and long sleeves",
    quantity=28, 
    current_location="Storage",
    storage_location="Hanging in Studio B",
)

c4 = CostumeGroup(
    name = "Dark Purple Bodices",
    image_url="/static/images/costumes/sb_b7.jpg",
    description="Dark Purple bodices with iridescent purple and blue fabric trim and gold edging",
    quantity=18, 
    current_location="Storage",
    storage_location="Bin in Back Room",
)

c44 = CostumeGroup(
    name = "Lavender Arm Puffs",
    image_url="/static/images/costumes/sb_b7.jpg",
    description="Pale purple tulle with blue and gold floral and ribbon trim - pairs",
    quantity=20, 
    current_location="Storage",
    storage_location="Up Top in Sleeping Beauty Area",
)

c5 = CostumeGroup(
    name = "Dryad Skirts",
    image_url="/static/images/costumes/sb_b7.jpg",
    description="Blue and Purple romantic style tulle skirts with iridescent lace trim",
    quantity=30, 
    current_location="Storage",
    storage_location="Hanging in Studio B",
)

c6 = CostumeGroup(
    name = "Purple Peasant Dresses with Black bodice",
    image_url="/static/images/costumes/sb_bridesmaids.jpg",
    description="Purple satin chemise top, black bodice with yellow floral embroidery, purple long skirt with yellow crinoline underskirt",
    quantity=15, 
    current_location="Storage",
    storage_location="Hanging in Studio B",
)

c7 = CostumeGroup(
    name = "Princess Bodices",
    image_url="/static/images/costumes/sb_princesses.jpg",
    description="9 different colored bodices with matching champagne floral trim and attached mesh elbow-length sleeves",
    quantity=9, 
    current_location="Storage",
    storage_location="Up Top in Sleeping Beauty Area",
)

c8 = CostumeGroup(
    name = "Princess Tutu Skirts",
    image_url="/static/images/costumes/sb_princesses.jpg",
    description="Ivory and Peach romantic style tulle skirts with peach and pink ribbon trim",
    quantity=8, 
    current_location="Storage",
    storage_location="Hanging in Studio B",
)

c9 = CostumeGroup(
    name = "Gold Jewels Bodices",
    image_url="/static/images/costumes/sb_jewels.jpg",
    description="gold longline bodice with attached petal trim",
    quantity=2, 
    current_location="In Use",
    storage_location="Hanging in Studio A",
)

c10 = CostumeGroup(
    name = "Gold Jewels Tutus",
    image_url="/static/images/costumes/sb_jewels.jpg",
    description="Romantic style tutus in ivory with orange under-layer and sparkle tulle overlay",
    quantity=2, 
    current_location="In Use",
    storage_location="Hanging in Studio A",
)

c11 = CostumeGroup(
    name = "Ivory Jewels Bodices",
    image_url="/static/images/costumes/sb_jewels.jpg",
    description="Ivory longline bodices with attached petal trim",
    quantity=2, 
    current_location="Storage",
    storage_location="Hanging in Studio A",
)

c12 = CostumeGroup(
    name = "Ivory Jewels Tutus",
    image_url="/static/images/costumes/sb_6b2.jpg",
    description="Romantic style tutus in ivory with gold under-layer and sparkle tulle overlay",
    quantity=2, 
    current_location="Storage",
    storage_location="Hanging in Studio A",
)

c13 = CostumeGroup(
    name = "Emerald Jewels Bodices",
    image_url="/static/images/costumes/sb_jewels.jpg",
    description="Emerald Green longline bodices - there are three sets of petals that can be attached",
    quantity=24, 
    current_location="Storage",
    storage_location="Up Top in WWOO area",
)

c14 = CostumeGroup(
    name = "Emerald Jewels Tutus",
    image_url="/static/images/costumes/sb_jewels.jpg",
    description="Romantic style tutus in ivory with green under-layer and sparkle tulle overlay",
    quantity=24, 
    current_location="Storage",
    storage_location="Hanging in Studio B",
)

c15 = CostumeGroup(
    name = "Fairy Tutus",
    image_url="/static/images/costumes/sb_fairies.jpg",
    description="various color classical bodices with gold and green floral trim, matching classical tutu bases. multiple sizes",
    quantity=11, 
    current_location="Storage",
    storage_location="Bodices are up top in bin in sleeping beauty area, bases are in top of the 3rd bay in the back",
)

c16 = CostumeGroup(
    name = "Lilac Fairy Tutus",
    image_url="/static/images/costumes/sb_lilac_fairy.jpg",
    description="purple classical bodice and tutu base with purple floral and silver trim and lace",
    quantity=2, 
    current_location="Storage",
    storage_location="Top of 3rd bay in Back Room",
)

c17 = CostumeGroup(
    name = "Bluebird Tutu",
    image_url="/static/images/costumes/sb_bluebird.jpg",
    description="pale blue classical bodice and tutu base with rhinestone neckpiece",
    quantity=1, 
    current_location="Storage",
    storage_location="Top of 3rd bay in Back Room",
)

c18 = CostumeGroup(
    name = "Queen Leotard",
    image_url="/static/images/costumes/sb_queen.jpg",
    description="ivory long sleeve leotard with shiny mesh top yoke, gold trim, and gold rhinestones",
    quantity=1, 
    current_location="Storage",
    storage_location="?",
)

c19 = CostumeGroup(
    name = "Queen Skirt",
    image_url="/static/images/costumes/sb_queen.jpg",
    description="Ivory skirt with beaded trim",
    quantity=1, 
    current_location="Storage",
    storage_location="Hanging in Studio B",
)

c20 = CostumeGroup(
    name = "Aurora Birthday Tutu",
    image_url="/static/images/costumes/sb_aurora_birthday.jpg",
    description="pale pink tutu with pink and gold floral trim, pink sparkle tulle and mesh sleeves",
    quantity=1, 
    current_location="Storage",
    storage_location="Top of 3rd bay in back room",
)

c21 = CostumeGroup(
    name = "Aurora Wedding Tutu",
    image_url="/static/images/costumes/sb_aurora_wedding.jpg",
    description="Ivory classical bodice (2 sizes) and tutu base (1) with gold and crystal ab rhinestone trim, white mesh and sparkle tulle sleeves (2 sets)",
    quantity=1, 
    current_location="Storage",
    storage_location="Top of 3rd bay in back room",
)

c22 = CostumeGroup(
    name = "Carabosse Dress",
    image_url="/static/images/costumes/sb_carabosse.jpg",
    description="black bodice with gold trim, black mesh sleeves, and black and gold petaled longer romantic length skirt",
    quantity=1, 
    current_location="Storage",
    storage_location="Hanging in Studio B",
)

c23 = CostumeGroup(
    name = "Carabosse Cape",
    image_url="/static/images/costumes/sb_carabosse.jpg",
    description="Long black cape with gold trim and hood",
    quantity=1, 
    current_location="Storage",
    storage_location="Hanging in Studio B",
)

c24 = CostumeGroup(
    name = "Bluebird Arm Puffs",
    image_url="/static/images/costumes/sb_bluebird.jpg",
    description="pale blue tulle arm puffs with floral trim and rhinestones - pair",
    quantity=1, 
    current_location="Storage",
    storage_location="Bin in Back Room",
)

c25 = CostumeGroup(
    name = "Lilac Fairy Wings",
    image_url="/static/images/costumes/sb_lilac_fairy.jpg",
    description="Large Cellophane Wings - pairs",
    quantity=2, 
    current_location="Storage",
    storage_location="Up Top in Sleeping Beauty Area",
)

c26 = CostumeGroup(
    name = "Fairy Wings",
    image_url="/static/images/costumes/sb_fairies.jpg",
    description="Cellophane Wings - pairs",
    quantity=10, 
    current_location="Storage",
    storage_location="Up Top in Sleeping Beauty Area",
)

c27 = CostumeGroup(
    name = "Carabosse Wings",
    image_url="/static/images/costumes/sb_carabosse.jpg",
    description="Large Cellophane Wings with gold and iridescent - pairs",
    quantity=2, 
    current_location="Storage",
    storage_location="Up Top in Sleeping Beauty Area",
)

db.session.add_all([c1, c111, c2, c3, c4, c44, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21, c22, c23, c25, c26, c27])
db.session.commit()

# ***************************************************************************
# data for sleeping beauty roles
# ***************************************************************************


r1 = Role(
    name = "Emerald Princesses",
    production_id = 2,
    level_id = 9,
    cg1_id = c1.id,
    cg3_id = c111.id,
    headpiece_id = h1.id, 
)

r2 = Role(
    name = "Garland Dancers",
    production_id = 2,
    level_id = 10, 
    cg1_id = c2.id,
    headpiece_id = h2.id, 
    prop_id = prop1.id
)

r3 = Role(
    name = "Princesses",
    production_id = 2,
    level_id = 11,
    cg1_id = c3.id,
    headpiece_id = h4.id, 
)

r4 = Role(
    name = "Lilac Fairy Attendants",
    production_id = 2,
    level_id = 12,
    cg1_id = c4.id,
    cg2_id = c5.id,
    cg3_id = c44.id,
    headpiece_id = h5.id, 
)

r5 = Role(
    name = "Demi Soloist Bridesmaids",
    production_id = 2,
    level_id = 13,
    cg1_id = c6.id,
    headpiece_id = h6.id, 
)

r6 = Role(
    name = "Soloist Princesses",
    production_id = 2,
    level_id = 13,
    cg1_id = c7.id,
    cg2_id = c8.id,
    headpiece_id = h7.id, 
)

r7 = Role(
    name = "Gold Jewels",
    production_id = 2,
    level_id = 13,
    cg1_id = c9.id,
    cg2_id = c10.id,
    headpiece_id = h15.id, 
)

r8 = Role(
    name = "Ivory Jewels",
    production_id = 2,
    level_id = 13,
    cg1_id = c11.id,
    cg2_id = c12.id,
    headpiece_id = h15.id, 
)

r9 = Role(
    name = "Emerald Jewels",
    production_id = 2,
    level_id = 13,
    cg1_id = c13.id,
    cg2_id = c14.id,
    headpiece_id = h15.id, 
)

r10 = Role(
    name = "Soloist Fairies",
    production_id = 2,
    level_id = 13,
    cg1_id = c15.id,
    cg2_id = c26.id,
    headpiece_id = h8.id, 
)

r11 = Role(
    name = "Lilac Fairy",
    production_id = 2,
    level_id = 13,
    cg1_id = c16.id,
    cg2_id = c25.id,
    headpiece_id = h9.id, 
    prop_id = prop2.id
)

r12 = Role(
    name = "Queen",
    production_id = 2,
    level_id = 13,
    cg1_id = c18.id,
    cg2_id = c19.id,
    headpiece_id = h10.id, 
    prop_id = prop3.id
)

r13 = Role(
    name = "Bluebird",
    production_id = 2,
    level_id = 13,
    cg1_id = c17.id,
    cg3_id = c24.id,
    headpiece_id = h11.id, 
)

r14 = Role(
    name = "Carabosse",
    production_id = 2,
    level_id = 13,
    cg1_id = c22.id,
    cg2_id = c27.id,
    cg3_id = c23.id,
    headpiece_id = h14.id, 
    prop_id = prop4.id
)

r15 = Role(
    name = "Aurora Birthday",
    production_id = 2,
    level_id = 13,
    cg1_id = c20.id,
    headpiece_id = h12.id, 
)

r16 = Role(
    name = "Aurora Wedding",
    production_id = 2,
    level_id = 13,
    cg1_id = c21.id,
    headpiece_id = h13.id, 
)

db.session.add_all([r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15, r16])
db.session.commit()