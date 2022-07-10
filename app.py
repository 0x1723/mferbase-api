import sqlite3
from flask import Flask, jsonify, request
from flask_api import status
from werkzeug.routing import BaseConverter
  
app = Flask(__name__)

class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]

app.url_map.converters['regex'] = RegexConverter

background_dict = {
	"01": None,
	"02": "blue",
	"03": "yellow",
	"04": "green",
	"05": "orange",
	"06": "red",
	"07": "space",
	"08": "tree",
	"09": "graveyard"
}

mfer_type_dict = {
	"01": None,
	"02": "plain mfer",
	"03": "charcoal mfer",
	"04": "zombie mfer",
	"05": "ape mfer",
	"06": "alien mfer"
}

eyes_dict = {
	"01": None,
	"02": "3d glasses",
	"03": "alien eyes",
	"04": "eye mask",
	"05": "eye patch",
	"06": "nerd glasses",
	"07": "purple shades",
	"08": "regular eyes",
	"09": "shades",
	"10": "vr",
	"11": "zombie eyes"
}

mouth_dict = {
	"01": None,
	"02": "flat",
	"03": "smile"
}

headphones_dict = {
	"01": None,
	"02": "rcs",
	"03": "black headphones",
	"04": "blue headphones",
	"05": "gold headphones",
	"06": "green headphones",
	"07": "lined headphones",
	"08": "pink headphones",
	"09": "red headphones",
	"10": "white headphones"
}

smoke_dict = {
	"01": None,
	"02": "cig black",
	"03": "cig white",
	"04": "pipe"
}

watch_dict = {
	"01": None,
	"02": "argo black",
	"03": "argo white",
	"04": "oyster gold",
	"05": "oyster silver",
	"06": "sub bat",
	"07": "sub black",
	"08": "sub blue",
	"09": "sub cola",
	"10": "sub lantern",
	"11": "sub red",
	"12": "sub rose",
	"13": "sub turquoise"
}

beard_dict = {
	"01": None,
	"02": "full beard",
	"03": "shadow beard"
}

hoodies_dict = {
	"01": None,
	"02": "hoodie"
}

shirt_dict = {
	"01": None,
	"02": "collared shirt blue",
	"03": "collared shirt green",
	"04": "collared shirt pink",
	"05": "collared shirt turquoise",
	"06": "collared shirt white",
	"07": "collared shirt yellow",
	"08": "hoodie down blue",
	"09": "hoodie down gray",
	"10": "hoodie down green",
	"11": "hoodie down pink",
	"12": "hoodie down red",
	"13": "hoodie down white",
	"14": "gold chain",
	"15": "silver chain"
}

long_hair_dict = {
	"01": None,
	"02": "long hair black",
	"03": "long hair yellow"
}

hats_under_dict = {
	"01": None,
	"02": "bandana blue",
    "03": "bandana dark gray",
    "04": "bandana red",
    "05": "beanie monochrome",
    "06": "beanie",
    "07": "cap monochrome",
    "08": "cap purple",
    "09": "headband blue/green",
    "10": "headband blue/red",
    "11": "headband blue/white",
	"12": "headband green/white",
	"13": "headband pink/white",
	"14": "knit atlanta",
	"15": "knit baltimore",
	"16": "knit buffalo",
	"17": "knit chicago",
	"18": "knit cleveland",
	"19": "knit dallas",
	"20": "knit kc",
	"21": "knit las vegas",
	"22": "knit miami",
	"23": "knit new york",
	"24": "knit pittsburgh",
	"25": "knit san fran"
}

hats_over_dict = {
	"01": None,
	"02": "cowboy hat",
	"03": "pilot helmet",
	"04": "tophat"
}

short_hair_dict = {
	"01": None,
	"02" : "messy black",
	"03" : "messy purple",
	"04" : "messy red",
	"05" : "messy yellow",
	"06" : "mohawk black",
	"07" : "mohawk blue",
	"08" : "mohawk green",
	"09" : "mohawk pink",
	"10" : "mohawk purple",
	"11" : "mohawk red",
	"12" : "mohawk yellow"
}

@app.route('/<column>/<regex("([0-9]|-)[0-9]"):background><regex("([0-9]|-)[0-9]"):mfer_type><regex("([0-9]|-)[0-9]"):eyes><regex("([0-9]|-)[0-9]"):mouth><regex("([0-9]|-)[0-9]"):headphones><regex("([0-9]|-)[0-9]"):smoke><regex("([0-9]|-)[0-9]"):watch><regex("([0-9]|-)[0-9]"):beard><regex("([0-9]|-)[0-9]"):hoodies><regex("([0-9]|-)[0-9]"):shirt><regex("([0-9]|-)[0-9]"):long_hair><regex("([0-9]|-)[0-9]"):hats_under><regex("([0-9]|-)[0-9]"):hats_over><regex("([0-9]|-)[0-9]"):short_hair>', methods = ['GET'])
def list(column, background, mfer_type, eyes, mouth, headphones, smoke, watch, beard, hoodies, shirt, long_hair, hats_under, hats_over, short_hair):
    if hoodies == "02":
    	hats_over_dict[hats_over] = 'hoodie'
    condition = ""
    if shirt in ["14", "15"]:
    	condition = f"and chain = '{shirt_dict[shirt]}'"
    elif shirt in ["02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13"]:
    	condition = f"and shirt = '{shirt_dict[shirt]}'"
    con = sqlite3.connect("mferbase.db")
    con.row_factory = sqlite3.Row
   
    cur = con.cursor()
    query = f"""select * from metadata 
where background {' = "'+background_dict[background]+'"' if background_dict[background] else "is null"}
and type {' = "'+mfer_type_dict[mfer_type]+'"' if mfer_type_dict[mfer_type] else "is null"}
and eyes {' = "'+eyes_dict[eyes]+'"' if eyes_dict[eyes] else "is null"}
and mouth {' = "'+mouth_dict[mouth]+'"' if mouth_dict[mouth] else "is null"}
and headphones {' = "'+headphones_dict[headphones]+'"' if headphones_dict[headphones] else "is null"}
and smoke {' = "'+smoke_dict[smoke]+'"' if smoke_dict[smoke] else "is null"}
and `4:20 watch` {' = "'+watch_dict[watch]+'"' if watch_dict[watch] else "is null"}
and beard {' = "'+beard_dict[beard]+'"' if beard_dict[beard] else "is null"}
and `long hair` {' = "'+long_hair_dict[long_hair]+'"' if long_hair_dict[long_hair] else "is null"}
and `hat over headphones` {' = "'+hats_over_dict[hats_over]+'"' if hats_over_dict[hats_over] else "is null"}
and `hat under headphones` {' = "'+hats_under_dict[hats_under]+'"' if hats_under_dict[hats_under] else "is null"}
and `short hair` {' = "'+short_hair_dict[short_hair]+'"' if short_hair_dict[short_hair] else "is null"}
{condition}
"""
    print(query)
    cur.execute(query)
   
    rows = cur.fetchall()
    if len(rows) > 1:
    	content = {'Wrong query': 'the query should return only one result'}
    	return content, status.HTTP_400_BAD_REQUEST
    if len(rows) == 0:
    	return jsonify({})
    return jsonify({
		column : rows[0][column]
	})

if __name__ == "__main__":
    app.run(debug=True, port=80)
