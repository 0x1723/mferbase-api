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
	"-1": None,
	"01": "blue",
	"02": "yellow",
	"03": "green",
	"04": "orange",
	"05": "red",
	"06": "space",
	"07": "tree",
	"08": "graveyard"
}

mfer_type_dict = {
	"-1": None,
	"01": "plain mfer",
	"02": "charcoal mfer",
	"03": "zombie mfer",
	"04": "ape mfer",
	"05": "alien mfer"
}

eyes_dict = {
	"-1": None,
	"01": "3d glasses",
	"02": "alien eyes",
	"03": "eye mask",
	"04": "eye patch",
	"05": "nerd glasses",
	"06": "purple shades",
	"07": "regular eyes",
	"08": "shades",
	"09": "vr",
	"10": "zombie eyes"
}

mouth_dict = {
	"-1": None,
	"01": "flat",
	"02": "smile"
}

headphones_dict = {
	"-1": None,
	"01": "rcs",
	"02": "black headphones",
	"03": "blue headphones",
	"04": "gold headphones",
	"05": "green headphones",
	"06": "lined headphones",
	"07": "pink headphones",
	"08": "red headphones",
	"09": "white headphones"
}

smoke_dict = {
	"-1": None,
	"01": "cig black",
	"02": "cig white",
	"03": "pipe"
}

watch_dict = {
	"-1": None,
	"01": "argo black",
	"02": "argo white",
	"03": "oyster gold",
	"04": "oyster silver",
	"05": "sub bat",
	"06": "sub black",
	"07": "sub blue",
	"08": "sub cola",
	"09": "sub lantern",
	"10": "sub red",
	"11": "sub rose",
	"12": "sub turquoise"
}

beard_dict = {
	"-1": None,
	"01": "full beard",
	"02": "shadow beard"
}

hoodies_dict = {
	"-1": None,
	"01": "hoodie"
}

shirt_dict = {
	"-1": None,
	"01": "collared shirt blue",
	"02": "collared shirt green",
	"03": "collared shirt pink",
	"04": "collared shirt turquoise",
	"05": "collared shirt white",
	"06": "collared shirt yellow",
	"07": "hoodie down blue",
	"08": "hoodie down gray",
	"09": "hoodie down green",
	"10": "hoodie down pink",
	"11": "hoodie down red",
	"12": "hoodie down white",
	"13": "gold chain",
	"14": "silver chain"
}

long_hair_dict = {
	"-1": None,
	"01": "long hair black",
	"02": "long hair yellow"
}

hats_under_dict = {
	"-1": None,
	"01": "bandana blue",
    "02": "bandana dark gray",
    "03": "bandana red",
    "04": "beanie monochrome",
    "05": "beanie",
    "06": "cap monochrome",
    "07": "cap purple",
    "08": "headband blue/green",
    "09": "headband blue/red",
    "10": "headband blue/white",
	"11": "headband green/white",
	"12": "headband pink/white",
	"13": "knit atlanta",
	"14": "knit baltimore",
	"15": "knit buffalo",
	"16": "knit chicago",
	"17": "knit cleveland",
	"18": "knit dallas",
	"19": "knit kc",
	"20": "knit las vegas",
	"21": "knit miami",
	"22": "knit new york",
	"23": "knit pittsburgh",
	"24": "knit san fran"
}

hats_over_dict = {
	"-1": None,
	"01": "cowboy hat",
	"02": "pilot helmet",
	"03": "tophat"
}

short_hair_dict = {
	"-1": None,
	"01" : "messy black",
	"02" : "messy purple",
	"03" : "messy red",
	"04" : "messy yellow",
	"05" : "mohawk black",
	"06" : "mohawk blue",
	"07" : "mohawk green",
	"08" : "mohawk pink",
	"09" : "mohawk purple",
	"10" : "mohawk red",
	"11" : "mohawk yellow"
}

@app.route('/<column>/<regex("([0-9]|-)[0-9]"):background><regex("([0-9]|-)[0-9]"):mfer_type><regex("([0-9]|-)[0-9]"):eyes><regex("([0-9]|-)[0-9]"):mouth><regex("([0-9]|-)[0-9]"):headphones><regex("([0-9]|-)[0-9]"):smoke><regex("([0-9]|-)[0-9]"):watch><regex("([0-9]|-)[0-9]"):beard><regex("([0-9]|-)[0-9]"):hoodies><regex("([0-9]|-)[0-9]"):shirt><regex("([0-9]|-)[0-9]"):long_hair><regex("([0-9]|-)[0-9]"):hats_under><regex("([0-9]|-)[0-9]"):hats_over><regex("([0-9]|-)[0-9]"):short_hair>', methods = ['GET'])
def list(column, background, mfer_type, eyes, mouth, headphones, smoke, watch, beard, hoodies, shirt, long_hair, hats_under, hats_over, short_hair):
    if hoodies == "01":
    	hats_over_dict[hats_over] = 'hoodie'
    condition = ""
    if shirt and shirt in ["13", "14"]:
    	condition = f"and chain = '{shirt_dict[shirt]}'"
    elif shirt and shirt not in ["13", "14"]:
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
