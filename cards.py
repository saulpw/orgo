#!/usr/bin/python

import string

svg = file("card-template.svg").read()

molecules = {
1:{
'name1':"WATER",
'name2':"oxane",
'name3':"oxidane",
'type':"",
'mass':18,
'state':"liquid",
'formula':"H2O",
'flavor':"From a drop of water a logician could infer the possibility of an Atlantic or a Niagara without having seen or heard of one or the other. -- Arthur Conan Doyle",
'nfpa_blue':0,
'nfpa_red':0,
'nfpa_yellow':0,
'nfpa_extra':"",
},

3:{
'name1':"METHANE",
'name2':"marsh gas",
'name3':"natural gas (80%)",
'type':"alkane",
'state':"gas",
'mass':16,
'pKa':"56",
'pKb':"",
'formula':"CH4",
'flavor':"The United Nations has declared the methane from cow emissions the greatest threat to the climate, forests, and wildlife.",
'nfpa_blue':1,
'nfpa_red':4,
'nfpa_yellow':0,
'nfpa_extra':"",
},
5:{
'name1':"ETHANE",
'name2':"natural gas (5%)",
'name3':"ethyl hydride",
'type':"alkane",
'state':"gas",
'mass':30,
'pKa':"50",
'pKb':"-36",
'formula':"C2H6",
'flavor':"",
'nfpa_blue':1,
'nfpa_red':4,
'nfpa_yellow':0,
'nfpa_extra':"",
},
13:{
'name1':"OXYGEN",
'name2':"air (21%)",
'name3':"",
'type':"gas",
'pKa':"",
'state':"gas",
'mass':32,
'formula':"O2",
'flavor':"Among the notable things about fire is that it also requires oxygen to burn - exactly like its enemy, life. Thereby are life and flames so often compared. -- Otto Weininger",
'nfpa_blue':0,
'nfpa_red':0,
'nfpa_yellow':0,
'nfpa_extra':"OX",
},
10:{
'name1':"CARBON DIOXIDE",
'name2':"air (1%)",
'name3':"spiritus sylvestre",
'type':"",
'pKa':"",
'state':"gas",
'mass':44,
'formula':"CO2",
'flavor':"As a scientist, my attention became totally focused on global warming some 15 years ago by the elegant and powerful measurements of carbon dioxide trapped in ice cores taken as much as 2 miles deep from the great East Antarctica ice sheet.  -- John Olver",
'nfpa_blue':2,
'nfpa_red':0,
'nfpa_yellow':0,
'nfpa_extra':"",
},
16:{
'name1':"ETHYLENE",
'name2':"",
'name3':"",
'type':"alkene",
'pKa':"",
'mass':28,
'formula':"C2H4",
'flavor':"Ethylene...why can't you be true?",
'nfpa_blue':3,
'nfpa_red':4,
'nfpa_yellow':2,
'nfpa_extra':"",
},
7:{
'name1':"HYDROGEN PEROXIDE",
'name2':"",
'name3':"",
'type':"",
'pKa':"11.75",
'state':"liquid",
'mass':34,
'formula':"H2O2",
'flavor':"Bleach, disinfectant, rocket propellant",
'nfpa_blue':3,
'nfpa_red':0,
'nfpa_yellow':2,
'nfpa_extra':"OX",
},
9:{
'name1':"METHANOL",
'name2':"wood alcohol",
'name3':"methyl alcohol",
'type':"alcohol",
'pKa':"",
'mass':32,
'state':"liquid",
'formula':"CH3OH",
'flavor':"Beware of bad moonshine: two shots blind you, three shots kill you.",
'nfpa_blue':1,
'nfpa_red':3,
'nfpa_yellow':0,
'nfpa_extra':"",
},
11:{
'name1':"ETHANOL",
'name2':"grain alcohol",
'name3':"ethyl alcohol",
'type':"alcohol",
'pKa':"",
'mass':46,
'state':"liquid",
'formula':"C2H5OH",
'flavor':"Shaken, not stirred.",
'nfpa_blue':2,
'nfpa_red':3,
'nfpa_yellow':0,
'nfpa_extra':"",
},
20:{
'name1':"PROPANOL",
'name2':"1-propyl alcohol",
'name3':"fusel oil",
'type':"alcohol",
'pKa':"16",
'pKb':"-2",
'mass':60,
'state':"liquid",
'formula':"C3H7OH",
'flavor':"A hot, spicy flavor detected as a vinous or fusel aroma and by a warming, prickling sensation in the mouth and throat.",
'nfpa_blue':1,
'nfpa_red':3,
'nfpa_yellow':0,
'nfpa_extra':"",
},
21:{
'name1':"ISOPROPYL ALCOHOL",
'name2':"rubbing alcohol",
'name3':"2-propanol",
'type':"alcohol",
'pKa':"16",
'pKb':"",
'mass':60,
'state':"liquid",
'formula':"C3H7OH",
'flavor':"",
'nfpa_blue':1,
'nfpa_red':3,
'nfpa_yellow':0,
'nfpa_extra':"",
},

17:{
'name1':"ETHYLENE GLYCOL",
'name2':"",
'name3':"",
'type':"alcohol",
'pKa':"",
'state':"liquid",
'mass':62,
'formula':"C2H6O2",
'flavor':"It was the mechanic, in the garage, with the antifreeze.",
'nfpa_blue':2,
'nfpa_red':1,
'nfpa_yellow':1,
'nfpa_extra':"",
},
23:{
'name1':"GLYCEROL",
'name2':"glycerine",
'name3':"",
'type':"alcohol",
'pKa':"",
'state':"liquid",
'mass':92,
'formula':"C3H8O3",
'flavor':"Topical pure glycerine is an effective treatment for psoriasis, burns, bites, cuts, rashes, bedsores, and calluses.",
'nfpa_blue':1,
'nfpa_red':1,
'nfpa_yellow':0,
'nfpa_extra':"",
},

15:{
'name1':"FORMALDEHYDE",
'name2':"methanal",
'name3':"formalin",
'type':"aldehyde",
'pKa':"",
'state':"liquid",
'mass':30,
'formula':"CH2O",
'flavor':"Formaldehyde mixed with blood causes the grey discoloration known as 'embalmer's grey'.",
'nfpa_blue':3,
'nfpa_red':4,
'nfpa_yellow':0,
'nfpa_extra':"",
},
6:{
'name1':"ACETALDEHYDE",
'name2':"ethyl aldehyde",
'name3':"ethanal",
'type':"aldehyde",
'pKa':"",
'state':"liquid",
'mass':44,
'formula':"C2H4O",
'flavor':"Description: Distinctive, straw-like, somewhat acrid character; sherry-like.  Prevention: Minimize exposure of finished wines to air.",
'nfpa_blue':2,
'nfpa_red':4,
'nfpa_yellow':2,
'nfpa_extra':"",
},
18:{
'name1':"ACETONE",
'name2':"",
'name3':"",
'type':"ketone",
'pKa':"24.2",
'pKb':"-10.2",
'state':"liquid",
'mass':58,
'formula':"(CH3)2CO",
'flavor':"In a pinch, diabetic urine could be used to remove nail polish.",
'nfpa_blue':1,
'nfpa_red':3,
'nfpa_yellow':0,
'nfpa_extra':"",
},
19:{
'name1':"PROPANE",
'name2':"cooking gas",
'name3':"liquified petroleum gas",
'type':"alkane",
'state':"gas",
'mass':44,
'formula':"C3H8",
'flavor':"Taste the meat, not the heat.",
'nfpa_blue':1,
'nfpa_red':4,
'nfpa_yellow':0,
'nfpa_extra':"",
},

4:{
'name1':"FORMIC ACID",
'name2':"methanoic acid",
'name3':"",
'type':"acid",
'state':"liquid",
'pKa':"3.77",
'mass':46,
'formula':"HCOOH",
'flavor':"pismire (n.)  an archaic or dialect word for an ant.  (literally: urinating ant, from the odour of formic acid characteristic of an ant hill)",
'nfpa_blue':3,
'nfpa_red':2,
'nfpa_yellow':1,
'nfpa_extra':"",
},
12:{
'name1':"ACETIC ACID",
'name2':"vinegar (10%)",
'name3':"",
'type':"acid",
'pKa':"",
'state':"liquid",
'mass':60,
'formula':"CH3COOH",
'flavor':"The best wine doth make the sharpest vinegar. -- John Lyly",
'nfpa_blue':3,
'nfpa_red':2,
'nfpa_yellow':1,
'nfpa_extra':"",
},
24:{
'name1':"PYRUVIC ACID",
'name2':"",
'name3':"",
'state':"liquid",
'type':"acid",
'pKa':"",
'mass':88,
'formula':"CH3COCOOH",
'flavor':"",
'nfpa_blue':3,
'nfpa_red':2,
'nfpa_yellow':0,
'nfpa_extra':"",
},
22:{
'name1':"LACTIC ACID",
'name2':"milk acid",
'name3':"",
'state':"liquid",
'type':"acid",
'pKa':"3.86",
'mass':90,
'formula':"C3H6O3",
'flavor':"Responsible for dental cavities, curdled milk, and sourdough flavor.",
'nfpa_blue':3,
'nfpa_red':0,
'nfpa_yellow':0,
'nfpa_extra':"",
},
32:{
'name1':"MALIC ACID",
'name2':"",
'name3':"",
'state':"liquid",
'type':"acid",
'pKa':"3.4, 5.2",
'mass':134,
'formula':"C4H6O5",
'flavor':"A sour taste like green apples can ruin a good wine.",
'nfpa_blue':2,
'nfpa_red':1,
'nfpa_yellow':0,
'nfpa_extra':"",
},
31:{
'name1':"OXALOACETIC ACID",
'name2':"",
'name3':"",
'state':"liquid",
'type':"acid",
'pKa':"",
'mass':132,
'formula':"C4H4O5",
'flavor':"",
'nfpa_blue':3,
'nfpa_red':0,
'nfpa_yellow':0,
'nfpa_extra':"",
},
28:{
'name1':"ANILINE",
'name2':"phenylamine",
'name3':"aminobenzene",
'type':"aromatic",
'pKa':"",
'pKb':"9.3",
'state':"liquid",
'mass':93,
'formula':"C6H5NH2",
'flavor':"The Baden Aniline and Soda Factory (BASF) was founded to manufacture commercial dyes from Aniline.",
'nfpa_blue':3,
'nfpa_red':2,
'nfpa_yellow':0,
'nfpa_extra':"",
},

29:{
'name1':"SALICYLIC ACID",
'name2':"2-hydroxybenzoic acid",
'name3':"",
'type':"analgesic",
'pKa':"3.5",
'state':"solid",
'mass':180,
'formula':"C9H8O4",
'flavor':"Ever seen a willow tree with acne?",
'nfpa_blue':2,
'nfpa_red':1,
'nfpa_yellow':0,
'nfpa_extra':"",
},
30:{
'name1':"ASPIRIN",
'name2':"acetylsalicylic acid",
'name3':"",
'type':"analgesic",
'pKa':"3.5",
'state':"solid",
'mass':180,
'formula':"C9H8O4",
'flavor':"",
'nfpa_blue':2,
'nfpa_red':1,
'nfpa_yellow':0,
'nfpa_extra':"",
},
25:{
'name1':"BENZENE",
'name2':"",
'name3':"",
'type':"aromatic",
'pKa':"",
'state':"liquid",
'mass':78,
'formula':"C6H6",
'flavor':"And I am a snake head eating the head on the opposite side -- They Might Be Giants",
'nfpa_blue':2,
'nfpa_red':3,
'nfpa_yellow':0,
'nfpa_extra':"",
},
26:{
'name1':"TOLUENE",
'name2':"methylbenzene",
'name3':"tolulol",
'type':"aromatic",
'pKa':"",
'state':"liquid",
'mass':92,
'formula':"C6H5CH3",
'flavor':"Because of concerns over the damaging health effects that toluene could pose to nail salon workers, the EU banned its use in cosmetics in 2004.",
'nfpa_blue':2,
'nfpa_red':3,
'nfpa_yellow':0,
'nfpa_extra':"",
},
27:{
'name1':"PHENOL",
'name2':"carbolic acid",
'name3':"phenic acid",
'type':"acid",
'pKa':"9.95",
'state':"solid",
'mass':94,
'formula':"C6H5OH",
'flavor':"Joseph Lister instructed his surgeons to wear clean gloves and wash their hands and instruments with 5% carbolic acid solutions.",
'nfpa_blue':3,
'nfpa_red':2,
'nfpa_yellow':0,
'nfpa_extra':"COR",
},

14:{
'name1':"NITROGEN",
'name2':"air (80%)",
'name3':"",
'type':"",
'pKa':"",
'state':"gas",
'mass':28,
'formula':"N2",
'flavor':"All we are is a lot of talking nitrogen.  -- Arthur Miller",
'nfpa_blue':0,
'nfpa_red':0,
'nfpa_yellow':0,
'nfpa_extra':"",
},
8:{
'name1':"HYDRAZINE",
'name2':"diamine",
'name3':"diazane",
'type':"",
'pKa':"8.10",
'pKb':"5.90",
'state':"liquid",
'mass':32,
'formula':"N2H4",
'flavor':"Hydrazine was first used as a rocket fuel during World War II for the the first rocket-powered fighter plane under the code name B-Stoff.",
'nfpa_blue':4,
'nfpa_red':4,
'nfpa_yellow':3,
'nfpa_extra':"",
},
2:{
'name1':"AMMONIA",
'name2':"azane",
'name3':"hydrogen nitride",
'type':"",
'pKa':"32.5",
'pKb':"4.75",
'state':"liquid",
'mass':17,
'formula':"NH3",
'flavor':"Spirit of Hartshorn.--This volatile liquor often affords immediate relief in cases of lowness of spirits, fainting, and hysteric fits.  It may be rubbed over the temples, and applied to the nostrils.",
'nfpa_blue':3,
'nfpa_red':1,
'nfpa_yellow':0,
'nfpa_extra':"",
},
33:{
'name1':"HYDROGEN CYANIDE",
'name2':"formonitrile",
'name3':"prussic acid",
'type':"",
'pKa':"9.2",
'state':"liquid",
'mass':27,
'formula':"HCN",
'flavor':"Bitter almonds, Prussian blue, and suicide capsules",
'nfpa_blue':4,
'nfpa_red':4,
'nfpa_yellow':1,
'nfpa_extra':"",
},
34:{
'name1':"NITRIC ACID",
'name2':"aqua fortis",
'name3':"spirit of niter",
'type':"acid",
'pKa':"-1.4",
'mass':63,
'state':"liquid",
'formula':"HNO3",
'flavor':"Gold and silver, equally resisting the action of fire and lead, must therefore be separated by other means.  Parting by nitric acid is most convenient, consequently most used; indeed, it is the only one employed by goldsmiths.",
'nfpa_blue':4,
'nfpa_red':0,
'nfpa_yellow':0,
'nfpa_extra':"OX",
},
35:{
'name1':"UREA",
'name2':"carbamide",
'name3':"",
'type':"",
'pKa':"",
'state':"liquid",
'mass':60,
'formula':"CO(NH2)2",
'flavor':"I must tell you that I can make urea without the use of kidneys, either man or dog. Ammonium cyanate is urea. -- Friedrich Wohler",
'nfpa_blue':1,
'nfpa_red':0,
'nfpa_yellow':0,
'nfpa_extra':"",
},
36:{
'name1':"NITROGLYCERIN",
'name2':"glyceryl trinitrate",
'name3':"",
'type':"nitrate",
'pKa':"",
'state':"liquid",
'mass':227,
'formula':"C3H5N3O9",
'flavor':"Three parts dynamite, with a nitroglycerin cap. It's perfect for small homes, carports and toolsheds. -- Uncle Fester",
'nfpa_blue':3,
'nfpa_red':3,
'nfpa_yellow':4,
'nfpa_extra':"",
},
37:{
'name1':"GLYCINE",
'name2':"aminoacetic acid",
'name3':"",
'type':"amino acid",
'pKa':"2.35,9.78",
'state':"liquid",
'mass':75,
'formula':"NH2CH2COOH",
'flavor':"G-G-anything makes G-Gly-glycine, oil water left right, any way it's all right!",
'nfpa_blue':0,
'nfpa_red':0,
'nfpa_yellow':0,
'nfpa_extra':"",
},
38:{
'name1':"ACETYLENE",
'name2':"welding gas",
'name3':"",
'type':"alkyne",
'mass':26,
'formula':"C2H2",
'flavor':"",
'nfpa_blue':1,
'nfpa_red':4,
'nfpa_yellow':3,
'nfpa_extra':"",
},
39:{
'name1':"BIPHENYL",
'name2':"",
'name3':"",
'type':"",
'pKa':"",
'state':"",
'mass':0,
'formula':"",
'flavor':"",
'nfpa_blue':0,
'nfpa_red':0,
'nfpa_yellow':0,
'nfpa_extra':"",
},
40:{
'name1':"ACETAMINOPHEN",
'name2':"paracetamol",
'name3':"",
'type':"analgesic",
'pKa':"",
'state':"solid",
'mass':151,
'formula':"C8H9NO2",
'flavor':"",
'nfpa_blue':0,
'nfpa_red':1,
'nfpa_yellow':0,
'nfpa_extra':"",
},
41:{
'name1':"TRINITROTOLUENE",
'name2':"TNT",
'name3':"",
'type':"explosive",
'pKa':"",
'state':"solid",
'mass':227,
'formula':"C6H2(NO2)3CH3",
'flavor':"",
'nfpa_blue':2,
'nfpa_red':4,
'nfpa_yellow':4,
'nfpa_extra':"",
},
42:{
'name1':"ISOCYANIC ACID",
'name2':"",
'name3':"",
'type':"",
'pKa':"",
'state':"",
'mass':43,
'formula':"HNCO",
'flavor':"",
'nfpa_blue':3,
'nfpa_red':2,
'nfpa_yellow':1,
'nfpa_extra':"",
},
}

g_fp = None
nSheets = 0
nCardsPerSheet=18
nCardsPerRow=6

def out(s):
    global g_fp, nSheets
    if g_fp is None:
        nSheets += 1
        g_fp = file("mol%s.svg" % nSheets, "w")
        out(file("card-header.svg").read())
        out("""<g
                inkscape:label="Layer 1"
                inkscape:groupmode="layer"
                id="layer1">""")

    g_fp.write(s)
#"""
f = string.Formatter()
nCards=0
for i in molecules.keys():
    m = molecules[i]
    dy = [ ]
    subscript = False
    for x in m["formula"]:
        if x.isdigit():
            if not subscript:
                dy.append("4")
                subscript = True
            else:
                dy.append("0")
        else:
            if not subscript:
                dy.append("0")
            else:
                dy.append("-4")
                subscript = False

    m["formula_dy"] = " ".join(dy)
    m["id"] = "g%s" % nCards
    m["x"] = (nCards % nCardsPerRow) * 230
    m["y"] = (nCards / nCardsPerRow) * 320
    if m["flavor"] == "":
        m["flavor"] = "_______"

    out(f.vformat(svg, [], m))
    nCards += 1

    if nCards % nCardsPerSheet == 0:
        out("</g></svg>")
        g_fp = None
        nCards = 0

out("</g></svg>")
g_fp = None
#"""

#print "name,othername,formula,mass,type,flavor"
#for m in molecules:
#    print ",".join([ ("%s" % x) for x in [ m["name1"], m["name2"], m["formula"], str(m["mass"]), m["type"], m[""]] ])

