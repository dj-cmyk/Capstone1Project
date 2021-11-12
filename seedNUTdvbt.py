from app import app
from models import db, Headpiece, CostumeGroup, Prop, Role


# ***************************************************************************
# data for nutcracker dvbt headpieces
# ***************************************************************************


h1 = Headpiece(
    name="Soldier Hat",
    image_url="/static/images/headpieces/nut_6a_soldier",
    description="Blue pillbox hat with three gold stars and elastic chin strap",
    quantity=25,
    current_location="In Use",
    storage_location="Bin in Studio A Top Cupboard"
)

h2 = Headpiece(
    name="Pink Flower Wreath Crown",
    image_url="/static/images/headpieces/nut_6a_marz.jpg",
    description="Pink flowers on wreath shaped crown with green trim and pink and green ribbon streamers down the back",
    quantity=18,
    current_location="In Use",
    storage_location="Bin in Studio A Top Cupboard"
)

h3 = Headpiece(
    name="Pink wide ribbon bow",
    image_url="/static/images/headpieces/nut_6b1_ballerina.jpg",
    description="Pink wide ribbon bow",
    quantity=19,
    current_location="In Use",
    storage_location="Bin in Studio A Top Cupboard"
)

h4 = Headpiece(
    name="Red rose",
    image_url="/static/images/headpieces/nut_6b1_spanish.jpg",
    description="large red rose with horsehair attached",
    quantity=22,
    current_location="In Use",
    storage_location="Bin in Studio A Top Cupboard"
)

h5 = Headpiece(
    name="Purple satin bow",
    image_url="/static/images/headpieces/nut_6b2_party.jpg",
    description="Lavender purple large satin hair bow",
    quantity=26,
    current_location="In Use",
    storage_location="Bin in Studio A Top Cupboard"
)

h6 = Headpiece(
    name="Silver Tea Tiaras",
    image_url="/static/images/headpieces/nut_6b2_tea.jpg",
    description="Silver pipe cleaner tiara with bright pink beads and AB crystal rhinestones",
    quantity=18,
    current_location="In Use",
    storage_location="Bin in Studio A Top Cupboard"
)

h7 = Headpiece(
    name="White Bonnet",
    image_url="/static/images/headpieces/nut_b7_maid.jpg",
    description="White bonnet with various lace trims",
    quantity=4,
    current_location="In Use",
    storage_location="Bin in Studio A Top Cupboard"
)

h8 = Headpiece(
    name="Dream Fairy Corps",
    image_url="/static/images/headpieces/nut_b7_dreamfairy.jpg",
    description="2 parts - gold floral front headband with mauve and peach floral back piece that sits under bun",
    quantity=13,
    current_location="In Use",
    storage_location="Bin in Studio A Top Cupboard"
)

h9 = Headpiece(
    name="Snowflake Tiara",
    image_url="/static/images/headpieces/nut_snow.jpg",
    description="small crystal rhinestone tiara",
    quantity=30,
    current_location="In Use",
    storage_location="Bin in Studio A Top Cupboard"
)

h10 = Headpiece(
    name="Purple Floral headpiece with rhinestone extension",
    image_url="/static/images/headpieces/nut_waltz.jpg",
    description="Purple and Gold floral headpiece with rhinestone extension off the side",
    quantity=25,
    current_location="In Use",
    storage_location="Bin in Studio A Top Cupboard"
)

h11 = Headpiece(
    name="Clara party bow",
    image_url="/static/images/headpieces/nut_clara_party.jpg",
    description="White large hair bow with small blue accent flowers",
    quantity = 3,
    current_location="In Use",
    storage_location="Bin in Studio A Top Cupboard"
)

h12 = Headpiece(
    name="Clara tiara",
    image_url="/static/images/headpieces/nut_clara_act2.jpg",
    description="crystal rhinestone tiara on headband with hair clips",
    quantity = 10,
    current_location="In Use",
    storage_location="Tiara bin in prop room"
)

h13 = Headpiece(
    name="Sister Hair Bow",
    image_url="/static/images/headpieces/nut_sisters.jpg",
    description="Ivory wide ribbon hair bow with narrower accent ribbon that matches each dress",
    quantity = 5,
    current_location="In Use",
    storage_location="Bin in Studio A Top Cupboard"
)

h14 = Headpiece(
    name="Holly bunch",
    image_url="/static/images/headpieces/nut_mrsS.jpg",
    description="small bunch of green holly",
    quantity=1,
    current_location="In Use",
    storage_location="Hanging on Mrs. S dress"
)

h15 = Headpiece(
    name="Pink Half Circle Tiara",
    image_url="/static/images/headpieces/nut_ballerina_doll.jpg",
    description="half circle rhinestone tiara in pink",
    quantity=1,
    current_location="In Use",
    storage_location="Tiara Bin in prop room"
)

h16 = Headpiece(
    name="Red Columbine Hat",
    image_url="/static/images/headpieces/nut_columbine.jpg",
    description="Red french doll shaped hat",
    quantity=1,
    current_location="In Use",
    storage_location="Bin in Studio A Top Cupboard"
)

h17 = Headpiece(
    name="Red Harlequin Hat",
    image_url="/static/images/headpieces/nut_harlequin.jpg",
    description="Red french doll shaped hat",
    quantity=1,
    current_location="In Use",
    storage_location="Bin in Studio A Top Cupboard"
)

h18 = Headpiece(
    name="Soldier Doll Hat",
    image_url="/static/images/headpieces/nut_soldier.jpg",
    description="Tall blue pillbox hat with gold trim",
    quantity=1,
    current_location="In Use",
    storage_location="Bin in Studio A Top Cupboard"
)

h19 = Headpiece(
    name="Principal Dream Fairy",
    image_url="/static/images/headpieces/nut_principal_dreamfairy_back.jpg",
    description="2 parts - gold floral front headband with aqua and peach floral back piece that sits under bun",
    quantity=3,
    current_location="In Use",
    storage_location="Bin in Studio A Top Cupboard"
)

h20 = Headpiece(
    name="Gold Star Headpiece",
    image_url="/static/images/headpieces/nut_star.jpg",
    description="Gold pointed star headpiece with gold trim and white LED lights",
    quantity=1,
    current_location="In Use",
    storage_location="Bin in Studio A Top Cupboard"
)

h21 = Headpiece(
    name="Timekeeper Headpiece",
    image_url="/static/images/headpieces/nut_timekeeper.jpg",
    description="Black clock hands tiara with crystal AB rhinestones",
    quantity=1,
    current_location="In Use",
    storage_location="Bin in Studio A Top Cupboard"
)

h22 = Headpiece(
    name="White Half Circle Tiara",
    image_url="/static/images/headpieces/nut_sq.jpg",
    description="Half circle rhinestone tiara in white",
    quantity=1,
    current_location="In Use",
    storage_location="Tiara bin in prop room"
)

h23 = Headpiece(
    name="Sugar Plum Tiara",
    image_url="/static/images/headpieces/nut_sugarPlum.jpg",
    description="Pink and Gold large tiara with front point",
    quantity=1,
    current_location="In Use",
    storage_location="Tiara bin in prop room"
)

h24 = Headpiece(
    name="Burgundy and Gold Floral headpiece with Rhinestones",
    image_url="/static/images/headpieces/nut_principal_spanish.jpg",
    description="Burgundy and Gold floral headpiece with rhinestone half circles",
    quantity=4,
    current_location="In Use",
    storage_location="Bin in Studio A Top Cupboard"
)

h25 = Headpiece(
    name="Principal Arabian",
    image_url="/static/images/headpieces/nut_principal_arabian_back.jpg",
    description="Textured teal fabric veil in back with gold trim and rhinestone point at the front",
    quantity=3,
    current_location="In Use",
    storage_location="Bin in Studio A Top Cupboard"
)

h26 = Headpiece(
    name="Principal Candy Cane",
    image_url="/static/images/headpieces/nut_candy_cane.jpg",
    description="White broad tiara with red and white trim and red and white striped candies",
    quantity=1,
    current_location="In Use",
    storage_location="Bin in Studio A Top Cupboard"
)

h27 = Headpiece(
    name="Principal Tea",
    image_url="/static/images/headpieces/nut_chinese_tea.jpg",
    description="Tall silver lace tiara with hot pink rhinestones",
    quantity=1,
    current_location="In Use",
    storage_location="Bin in Studio A Top Cupboard"
)

h28 = Headpiece(
    name="Dew Drop Tiara",
    image_url="/static/images/headpieces/nut_dew_drop.jpg",
    description="crystal AB rhinestone tiara",
    quantity=1,
    current_location="In Use",
    storage_location="Bin in Studio A Top Cupboard"
)

h29 = Headpiece(
    name="Principal Marzipan",
    image_url="/static/images/headpieces/nut_principalmarz_back.jpg",
    description="gold half circle tiara with separate peach and white floral wreath that sits under the bun",
    quantity=4,
    current_location="In Use",
    storage_location="Bin in Studio A Top Cupboard"
)

h30 = Headpiece(
    name="Petals",
    image_url="/static/images/headpieces/NUT_petals_headpiece.jpg",
    description="Gold and crystal AB rhinestone chain with purple and green gems and bead work, purple flowers",
    quantity=4,
    current_location="In Use",
    storage_location="Bin in Studio A Top Cupboard"
)


db.session.add_all([h1, h2, h3, h4, h5, h6, h7, h8, h9, h10, h11, h12, h13, h14, h15, h16, h17, h18, h19, h20, h21, h22, h23, h24, h25, h26, h27, h28, h29, h30])
db.session.commit()

# ***************************************************************************
# data for nutcracker props
# ***************************************************************************

p1 = Prop(
    name = "Swords - Soldier Corps",
    image_url = "/static/images/props/nut_6a_soldiers.jpg",
    description = "grey swords with either silver or gold handle",
    quantity = 20,
    current_location = "In Use",
    storage_location = "White House?"
)

p2 = Prop(
    name = "Pink Fans - Tea Corps",
    image_url = "/static/images/props/nut_6b2_tea.jpg",
    description = "pink fans with silver trim, glued open - pairs",
    quantity = 1,
    current_location = "In Use",
    storage_location = "Prop Room?"
)

p3 = Prop(
    name = "Light Up Wands - Dream Fairy Corps",
    image_url = "/static/images/props/nut_b7_dream.jpg",
    description = "silver and gold long wands with white LED lights, ribbon streamers, and small floral bunches",
    quantity = 8,
    current_location = "In Use",
    storage_location = "Prop Room"
)

p4 = Prop(
    name = "Feather Dusters",
    image_url = "/static/images/props/nut_maid.jpg",
    description = "White feather duster with black handle",
    quantity = 2,
    current_location = "In Use",
    storage_location = "Prop Room??"
)

p5 = Prop(
    name = "Nutcracker Doll",
    image_url = "/static/images/props/nut_clara_doll.jpg",
    description = "Tall wooden Nutcracker Doll",
    quantity = 3,
    current_location = "In Use",
    storage_location = "Prop Room??"
)

p6 = Prop(
    name = "Pointe Shoe",
    image_url = "/static/images/props/nut_clara_shoe.jpg",
    description = "Single pointe shoe to hit mouse king",
    quantity = 1,
    current_location = "In Use",
    storage_location = "Prop Room??"
)

p7 = Prop(
    name = "Dolls",
    image_url = "/static/images/props/nut_dolls.jpg",
    description = "Ballerina Doll, Columbine Doll, Harlequin Doll, Soldier Doll - mini versions of the existing costumes",
    quantity = 4,
    current_location = "In Use",
    storage_location = "Prop Room??"
)

p8 = Prop(
    name = "Principal Dream Fairy Wand",
    image_url = "/static/images/props/nut_principal_dreamfairy_wand.jpg",
    description = "silver and gold long wand with white LED lights, ribbon streamers, and larger floral elements",
    quantity = 1,
    current_location = "In Use",
    storage_location = "Prop Room"
)

p9 = Prop(
    name = "Principal Tea Fans",
    image_url = "/static/images/props/nut_principal_tea_fans.jpg",
    description = "pink fan glued open with extra silver trim - pair",
    quantity = 1,
    current_location = "In Use",
    storage_location = "Prop Room"
)

p10 = Prop(
    name = "Principal Spanish Fans",
    image_url = "/static/images/props/nut_principal_spanish_fans.jpg",
    description = "gold, orange, and yellow sequin decorated fans with black base",
    quantity = 4,
    current_location = "In Use",
    storage_location = "Prop Room"
)


db.session.add_all([p1, p2, p3, p4, p5, p6, p7, p8, p9, p10])
db.session.commit()

# ***************************************************************************
# data for nutcracker costume groups
# ***************************************************************************

c1 = CostumeGroup(
    name = "Soldier Tutus",
    image_url="/static/images/costumes/nut_6a_soldier.jpg",
    description="Navy blue velvet leotard with attached puff tutu skirt, gold fringe trim on straps and gold star trim on center front",
    quantity=45, 
    current_location="In Use",
    storage_location="Hanging in Studio A",
)

c2 = CostumeGroup(
    name = "Soldier Gloves",
    image_url="/static/images/costumes/nut_6a_soldier_gloves.jpg",
    description="white gloves with satin finish - pairs",
    quantity=25, 
    current_location="In Use",
    storage_location="Bin in Studio A Cupboard",
)

c3 = CostumeGroup(
    name = "Marzipan Leotards",
    image_url="/static/images/costumes/nut_6a_marz_leo.jpg",
    description="Pink Velvet leotard with white and green trim and pink roses",
    quantity=51, 
    current_location="In Use",
    storage_location="Bin in Back Room",
)

c4 = CostumeGroup(
    name = "Maripan Tutus",
    image_url="/static/images/costumes/nut_6a_marz_tutu.jpg",
    description="white romantic tutu with pink and green ribbon trim, pink flowers at waistband",
    quantity=51, 
    current_location="In Use",
    storage_location="Bin in Back Room",
)


c5 = CostumeGroup(
    name = "Ballerina Doll Leotards",
    image_url="/static/images/costumes/nut_6b1_ballerina_leo.jpg",
    description="Pale pink camisole leotard with pink sequin applique, varied rhinestone, and attached pink arm puffs",
    quantity=31, 
    current_location="In Use",
    storage_location="Hanging in Studio A",
)

c6 = CostumeGroup(
    name = "Ballerina Doll Tutus",
    image_url="/static/images/costumes/nut_6b1_ballerina_tutu.jpg",
    description="pink pull on platter tutu with pink sequin applique, varied rhinestone, wide elastic waistband",
    quantity=19, 
    current_location="In Use",
    storage_location="Half in Back Room, Half in White House - after run all will be in white house",
)

c7 = CostumeGroup(
    name = "Ballerina Doll Gloves",
    image_url="/static/images/costumes/nut_6b1_ballerina_gloves.jpg",
    description="white gloves with seams on the back of the hand - pairs",
    quantity=12, 
    current_location="In Use",
    storage_location="bin in Studio A Cupboard",
)

c8 = CostumeGroup(
    name = "6B1 Spanish Leotards",
    image_url="/static/images/costumes/nut_6b1_spanish_leo.jpg",
    description="Black velvet leotard with black lace sleeve and pompon trim",
    quantity=28, 
    current_location="In Use",
    storage_location="Bin in back room",
)

c9 = CostumeGroup(
    name = "6B1 Spanish Skirts",
    image_url="/static/images/costumes/nut_6b1_spanish_skirt.jpg",
    description="red tiered romantic length skirt with black lace trim on each layer",
    quantity=28, 
    current_location="In Use",
    storage_location="Bin up top",
)

c10 = CostumeGroup(
    name = "DVBT Tea Tunics",
    image_url="/static/images/costumes/nut_6b2_tunic.jpg",
    description="Blue and Silver damask fabric tunic with hot pink frog closure",
    quantity=26, 
    current_location="In Use",
    storage_location="Hanging in Studio A",
)

c11 = CostumeGroup(
    name = "Tea Leggings",
    image_url="/static/images/costumes/nut_leggings.jpg",
    description="Hot Pink leggings",
    quantity=19, 
    current_location="In Use",
    storage_location="Hanging in Studio A",
)

c12 = CostumeGroup(
    name = "6B2 Party Girls Dresses",
    image_url="/static/images/costumes/nut_6b2_party.jpg",
    description="Red Party Girl Dresses with purple ribbon and purple cabachon trim",
    quantity=42, 
    current_location="In Use",
    storage_location="Hanging in Studio A",
)

c13 = CostumeGroup(
    name = "6B2 Party Sashes",
    image_url="/static/images/costumes/nut_6b2_sash.jpg",
    description="Lavender purple satin sash with snap",
    quantity=24, 
    current_location="In Use",
    storage_location="Bin in Studio A Cupboard",
)

c14 = CostumeGroup(
    name = "Dream Fairy Dresses",
    image_url="/static/images/costumes/nut_dreamfairy.jpg",
    description="Structured bodice in aqua and gold with three layer chiffon circle skirt in aqua, peach, and gold",
    quantity=16, 
    current_location="In Use",
    storage_location="Hanging in Studio A",
)

c15 = CostumeGroup(
    name = "Dream Fairy Wings - Corps",
    image_url="/static/images/costumes/nut_dreamfairy_wings.jpg",
    description="Silver and gold fabric wings with snap attachment",
    quantity=19, 
    current_location="In Use",
    storage_location="Bin in Prop Room",
)

c16 = CostumeGroup(
    name = "Dream Fairy Wings - Principal",
    image_url="/static/images/costumes/nut_dreamfairy_wings.jpg",
    description="Silver and gold fabric wings with larger floral and rhinestone embellishment and snap attachment",
    quantity=3, 
    current_location="In Use",
    storage_location="Bin in Prop Room",
)

c17 = CostumeGroup(
    name = "B7 - maids",
    image_url="/static/images/costumes/nut_b7_maid.jpg",
    description="Black velvet leotard with attached black tutu, white apron and white center front trim",
    quantity=4, 
    current_location="In Use",
    storage_location="Hanging in Studio A",
)

c18 = CostumeGroup(
    name = "Snow Dresses",
    image_url="/static/images/costumes/nut_snow.jpg",
    description="white leotard with attached romantic length white tulle skirt, various silver sequin appliques, rhinestones, sequins on skirt",
    quantity=46, 
    current_location="In Use",
    storage_location="Hanging in Studio A",
)

c19 = CostumeGroup(
    name = "Snow Arm Puffs",
    image_url="/static/images/costumes/nut_snow_armpuffs.jpg",
    description="White tulle arm puffs with sequins - pairs",
    quantity=34, 
    current_location="In Use",
    storage_location="Bin in Studio A Cupboard",
)

c20 = CostumeGroup(
    name = "Clara Party Dress",
    image_url="/static/images/costumes/nut_clara_party.jpg",
    description="Blue dress with white lace trim",
    quantity=3, 
    current_location="In Use",
    storage_location="Hanging in Studio A",
)

c21 = CostumeGroup(
    name = "Clara Nightgown",
    image_url="/static/images/costumes/nut_clara_nightgown.jpg",
    description="white empire waist leotard with attached long white skirt",
    quantity=3, 
    current_location="In Use",
    storage_location="Hanging in Studio A",
)

c22 = CostumeGroup(
    name = "Sister Party Dresses",
    image_url="/static/images/costumes/nut_sisters.jpg",
    description="ivory dresses with trim in one of the following colors: Pale Blue, Yellow, Pink, Teal, Navy",
    quantity=5, 
    current_location="In Use",
    storage_location="Hanging in Studio A",
)

c23 = CostumeGroup(
    name = "Mrs. Stahlbaum Dress",
    image_url="/static/images/costumes/nut_mrsS.jpg",
    description="Long, deep green, off the shoulder dress",
    quantity=2, 
    current_location="In Use",
    storage_location="Hanging in Studio A",
)

c24 = CostumeGroup(
    name = "Mrs. Stahlbaum Hoop underskirt",
    image_url="/static/images/costumes/nut_mrsS_hoop.jpg",
    description="white hooped underskirt",
    quantity=1, 
    current_location="In Use",
    storage_location="Hanging in Studio A",
)

c25 = CostumeGroup(
    name = "Ballerina Doll Tutu - 1",
    image_url="/static/images/costumes/nut_ballerina_doll_1.jpg",
    description="White longline bodice with pink and silver trim attached to white platter tutu base with pink and silver trim",
    quantity=1, 
    current_location="In Use",
    storage_location="Back Room - Nutcracker Tutu Pile",
)

c26 = CostumeGroup(
    name = "Ballerina Doll Tutu - 2",
    image_url="/static/images/costumes/nut_ballerina_doll_2.jpg",
    description="Ivory bodice with pink trim, attached to ivory platter tutu base with pink trim",
    quantity=1, 
    current_location="In Use",
    storage_location="Back Room - Nutcracker Tutu Pile",
)

c27 = CostumeGroup(
    name = "Ballerina Doll Tutu - 3",
    image_url="/static/images/costumes/nut_ballerina_doll_3.jpg",
    description="Pink bodice with white and iridescent lace center panel, pink trim, attached to white platter tutu base with pink and iridescent lace trim",
    quantity=1, 
    current_location="In Use",
    storage_location="Back Room - Nutcracker Tutu Pile",
)

c28 = CostumeGroup(
    name = "Columbine Dress",
    image_url="/static/images/costumes/nut_columbine.jpg",
    description="Orange and Yellow diamond patterned fabric bodice with attached orange romantic style tutu skirt",
    quantity=1, 
    current_location="In Use",
    storage_location="Hanging in Studio A",
)

c29 = CostumeGroup(
    name = "Columbine Accessories",
    image_url="/static/images/costumes/nut_columbine_accessory.jpg",
    description="White Organza collar, orange organza bloomers, orange organza arm puffs",
    quantity=1, 
    current_location="In Use",
    storage_location="Bin in Studio A Cupboard",
)

c30 = CostumeGroup(
    name = "Harlequin Unitard",
    image_url="/static/images/costumes/nut_harlequin.jpg",
    description="Orange and Yellow diamond patterned fabric unitard with red pompom 'buttons'",
    quantity=1, 
    current_location="In Use",
    storage_location="Hanging in Studio A",
)

c31 = CostumeGroup(
    name = "Harlequin Accessories",
    image_url="/static/images/costumes/nut_harlequin_accessory.jpg",
    description="White organza collar, red belt",
    quantity=1, 
    current_location="In Use",
    storage_location="Bin in Studio A Cupboard",
)

c32 = CostumeGroup(
    name = "Soldier Doll Tutu",
    image_url="/static/images/costumes/nut_soldier.jpg",
    description="Yellow satin bodice with gold trim, attached to blue Euro style tutu",
    quantity=1, 
    current_location="In Use",
    storage_location="Hanging in Studio A",
)

c33 = CostumeGroup(
    name = "Timekeeper Dress",
    image_url="/static/images/costumes/nut_timekeeper.jpg",
    description="White Bodice with black piping and rhinestone trim, attached to black romantic style tutu, white overlay with black roman numerals and rhinestones",
    quantity=1, 
    current_location="In Use",
    storage_location="Hanging in Studio A",
)

c34 = CostumeGroup(
    name = "Snow Queen Tutu - 1",
    image_url="/static/images/costumes/nut_sq_1.jpg",
    description="White longline bodice with white and silver trim, attached to white platter tutu with matching trim",
    quantity=1, 
    current_location="In Use",
    storage_location="Back Room - Nutcracker Tutu Pile",
)

c35 = CostumeGroup(
    name = "Snow Queen Tutu - 2",
    image_url="/static/images/costumes/nut_sq_2.jpg",
    description="Silver longline bodice with black trim, attached to white platter tutu with silver and black trim",
    quantity=1, 
    current_location="In Use",
    storage_location="Back Room - Nutcracker Tutu Pile",
)

c36 = CostumeGroup(
    name = "Snow Queen Tutu - 3",
    image_url="/static/images/costumes/nut_sq_3.jpg",
    description="White classical style bodice with silver trim, attached to white platter tutu with sparkle tulle overlay tinged with pale blue",
    quantity=1, 
    current_location="In Use",
    storage_location="Back Room - Nutcracker Tutu Pile",
)

c37 = CostumeGroup(
    name = "Sugar Plum Tutu",
    image_url="/static/images/costumes/nut_sugarplum.jpg",
    description="Pink classical bodice with pink and gold floral trim and rhinestones, attached to white platter tutu base with pink overlay, gold and iridescent lace trim",
    quantity=1, 
    current_location="In Use",
    storage_location="Back Room - Nutcracker Tutu Pile",
)

c38 = CostumeGroup(
    name = "Principal Arabian Dresses",
    image_url="/static/images/costumes/nut_arabian.jpg",
    description="teal leotard with gold applique, textured teal high low skirt attached",
    quantity=8, 
    current_location="In Use",
    storage_location="Hanging in Studio A",
)

c39 = CostumeGroup(
    name = "Principal Candy Cane Dresses",
    image_url="/static/images/costumes/nut_candycane.jpg",
    description="Red velvet leotard with white center panel, red ribbon trim, red and white tulle skirt attached",
    quantity=8, 
    current_location="In Use",
    storage_location="Hanging in Studio A",
)

c40 = CostumeGroup(
    name = "Principal Tea Dress",
    image_url="/static/images/costumes/nut_principal_tea_dress.jpg",
    description="Blue and silver damask fabric bodice with hot pink piping trim, hot pink rhinestones, hot pink and blue attached short romantic style tutu",
    quantity=2, 
    current_location="In Use",
    storage_location="Hanging in Studio A",
)

c41 = CostumeGroup(
    name = "Principal Marzipan Dress",
    image_url="/static/images/costumes/nut_principal_marz_dress.jpg",
    description="Iridescent pink bodice with pink sequin applique, pink and peach chiffon skirt with rhinestones, peach mesh sleeves",
    quantity=4, 
    current_location="In Use",
    storage_location="Hanging in Studio A",
)

c42 = CostumeGroup(
    name = "Black Velvet Bodices",
    image_url="/static/images/costumes/nut_black_bodice.jpg",
    description="Black velvet classical shape bodices",
    quantity=12, 
    current_location="In Use",
    storage_location="Bin in Back Room",
)

c43 = CostumeGroup(
    name = "Principal Spanish Bodice Trim",
    image_url="/static/images/costumes/nut_principal_spanish_bodice.jpg",
    description="Burgundy and gold bodice lace and ribbon trim",
    quantity=4, 
    current_location="In Use",
    storage_location="Stitched on bodices",
)

c44 = CostumeGroup(
    name = "Black + Gold Tiered Skirts",
    image_url="/static/images/costumes/nut_gold_skirt.jpg",
    description="Gold tulle romantic length tiered skirt with black elastic waistband, black lace trim",
    quantity=17, 
    current_location="In Use",
    storage_location="Hanging in Studio A",
)

c45 = CostumeGroup(
    name = "Dew Drop Dresses",
    image_url="/static/images/costumes/nut_dewdrop.jpg",
    description="Purple leotard with attached chiffon skirt, 2 in dark purple, 1 in pale purple, heavily decorated with crystal AB rhinestones, sheer mesh sleeves with rhinestones",
    quantity=3, 
    current_location="In Use",
    storage_location="Hanging in Studio A",
)

c46 = CostumeGroup(
    name = "Petals Dresses",
    image_url="/static/images/costumes/nut_petals_dress.jpg",
    description="Green bodice with purple floral applique, purple petaled three layer skirt with attached trunks",
    quantity=4, 
    current_location="In Use",
    storage_location="Hanging in Studio A",
)

c47 = CostumeGroup(
    name = "Flowers Corps Bodices",
    image_url="/static/images/costumes/nut_flowers_bodices.jpg",
    description="Lavender purple structured bodice with purple, gold, and green leaf trim",
    quantity=25, 
    current_location="In Use",
    storage_location="Hanging in Studio A",
)

c48 = CostumeGroup(
    name = "Flowers Corps Tutus",
    image_url="/static/images/costumes/nut_flowers_tutus.jpg",
    description="3 shades of purple tulle petals in a romantic length tutu - currently attached to bodices",
    quantity=25, 
    current_location="In Use",
    storage_location="Hanging in Studio A",
)

c49 = CostumeGroup(
    name = "Flowers Corps Trunks",
    image_url="/static/images/costumes/nut_flowers_trunks.jpg",
    description="Purple Trunks",
    quantity=25, 
    current_location="In Use",
    storage_location="Bin in Studio A Cupboard",
)


db.session.add_all([c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18, c19, c20, c21, c22, c23, c25, c26, c27, c28, c29, c30, c31, c32, c33, c34, c35, c36, c37, c38, c39, c40, c41, c42, c43, c44, c45, c46, c47, c48, c49])
db.session.commit()

# ***************************************************************************
# data for nutcracker roles
# ***************************************************************************


r1 = Role(
    name = "Soldier Corps",
    production_id = 1,
    level_id = 9,
    cg1_id = c1.id,
    cg3_id = c2.id,
    headpiece_id = h1.id, 
    prop_id = p1.id
)

r2 = Role(
    name = "Marzipan Corps",
    production_id = 1,
    level_id = 9, 
    cg1_id = c3.id,
    cg2_id = c4.id,
    headpiece_id = h2.id, 
)

r3 = Role(
    name = "Ballerina Dolls Corps",
    production_id = 1,
    level_id = 10,
    cg1_id = c5.id,
    cg2_id = c6.id, 
    cg3_id = c7.id,
    headpiece_id = h3.id, 
)

r4 = Role(
    name = "Spanish Corps",
    production_id = 1,
    level_id = 10,
    cg1_id = c8.id,
    cg2_id = c9.id,
    headpiece_id = h4.id, 
)

r5 = Role(
    name = "Tea Corps",
    production_id = 1,
    level_id = 11,
    cg1_id = c10.id,
    cg2_id = c11.id,
    headpiece_id = h6.id, 
    prop_id = p2.id
)

r6 = Role(
    name = "Party Girls",
    production_id = 1,
    level_id = 11,
    cg1_id = c12.id,
    cg2_id = 29,
    cg3_id = c13.id,
    headpiece_id = h5.id, 
)

r7 = Role(
    name = "Dream Fairy Corps",
    production_id = 1,
    level_id = 12,
    cg1_id = c14.id,
    cg3_id = c15.id,
    headpiece_id = h8.id, 
    prop_id = p3.id
)

r8 = Role(
    name = "Maids",
    production_id = 1,
    level_id = 12,
    cg1_id = c17.id,
    headpiece_id = h7.id, 
    prop_id = p4.id
)

r9 = Role(
    name = "Flurries and Snow Corps",
    production_id = 1,
    level_id = 12,
    cg1_id = c18.id,
    cg3_id = c19.id,
    headpiece_id = h9.id, 
)

r10 = Role(
    name = "Waltz of the Flowers Corps",
    production_id = 1,
    level_id = 13,
    cg1_id = c47.id,
    cg2_id = c48.id,
    cg3_id = c49.id,
    headpiece_id = h10.id, 
)

r11 = Role(
    name = "Clara - Party Scene",
    production_id = 1,
    level_id = 13,
    cg1_id = c20.id,
    headpiece_id = h11.id, 
    prop_id = p5.id
)

r12 = Role(
    name = "Clara - Nightgown",
    production_id = 1,
    level_id = 13,
    cg1_id = c21.id,
    headpiece_id = h12.id, 
    prop_id = p6.id
)

r13 = Role(
    name = "Clara's Sisters",
    production_id = 1,
    level_id = 13,
    cg1_id = c22.id,
    headpiece_id = h13.id, 
    prop_id = p7.id
)

r14 = Role(
    name = "Mrs. Stahlbaum",
    production_id = 1,
    level_id = 13,
    cg1_id = c23.id,
    cg2_id = c24.id,
    headpiece_id = h14.id, 
)

r15 = Role(
    name = "Ballerina Doll",
    production_id = 1,
    level_id = 13,
    cg1_id = c25.id,
    cg2_id = c26.id,
    cg3_id = c27.id,
    headpiece_id = h15.id, 
)

r16 = Role(
    name = "Columbine Doll",
    production_id = 1,
    level_id = 13,
    cg1_id = c28.id,
    cg3_id = c29.id,
    headpiece_id = h16.id, 
)

r17 = Role(
    name = "Harlequin Doll",
    production_id = 1,
    level_id = 13,
    cg1_id = c30.id,
    cg3_id = c31.id,
    headpiece_id = h17.id, 
)

r18 = Role(
    name = "Soldier Doll",
    production_id = 1,
    level_id = 13,
    cg1_id = c32.id,
    headpiece_id = h18.id, 
)

r19 = Role(
    name = "Principal Dream Fairy",
    production_id = 1,
    level_id = 13,
    cg1_id = c14.id,
    cg3_id = c16.id,
    headpiece_id = h19.id, 
    prop_id = p8.id
)

r20 = Role(
    name = "Drosselmeyer's Timekeeper",
    production_id = 1,
    level_id = 13,
    cg1_id = c33.id,
    headpiece_id = h21.id, 
)

r21 = Role(
    name = "Snow Queen",
    production_id = 1,
    level_id = 13,
    cg1_id = c34.id,
    cg2_id = c35.id,
    cg3_id = c36.id,
    headpiece_id = h22.id, 
)

r22 = Role(
    name = "Sugar Plum Fairy",
    production_id = 1,
    level_id = 13,
    cg1_id = c37.id,
    headpiece_id = h23.id, 
)

r23 = Role(
    name = "Principal Spanish",
    production_id = 1,
    level_id = 13,
    cg1_id = c42.id,
    cg2_id = c44.id,
    cg3_id = c43.id,
    headpiece_id = h24.id, 
    prop_id = p10.id
)

r24 = Role(
    name = "Principal Arabian",
    production_id = 1,
    level_id = 13,
    cg1_id = c38.id,
    headpiece_id = h25.id, 
)

r25 = Role(
    name = "Principal Candy Cane",
    production_id = 1,
    level_id = 13,
    cg1_id = c39.id,
    headpiece_id = h26.id, 
)

r26 = Role(
    name = "Principal Chinese Tea",
    production_id = 1,
    level_id = 13,
    cg1_id = c40.id,
    headpiece_id = h27.id, 
    prop_id = p9.id
)

r27 = Role(
    name = "Principal Marzipan",
    production_id = 1,
    level_id = 13,
    cg1_id = c41.id,
    headpiece_id = h29.id, 
)

r28 = Role(
    name = "Dew Drop Fairy",
    production_id = 1,
    level_id = 13,
    cg1_id = c45.id,
    headpiece_id = h28.id, 
)

r29 = Role(
    name = "Petals",
    production_id = 1,
    level_id = 13,
    cg1_id = c46.id,
    headpiece_id = h30.id, 
)

db.session.add_all([r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15, r16, r17, r18, r19, r20, r21, r22, r23, r24, r25, r26, r27, r28, r29])
db.session.commit()