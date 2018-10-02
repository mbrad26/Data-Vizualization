import json
from pygal_maps_world.i18n import COUNTRIES
from pygal.maps.world import World
from pygal.style import RotateStyle as RS, LightColorizedStyle as LS

filename = 'gdp_json.json'
with open(filename) as f:
    gdp = json.load(f)


def get_code(c_name):
    for c, name in COUNTRIES.items():
        if name == c_name:
            return c
    return None


gdp_country = {}
for c_dict in gdp:
    if c_dict['Year'] == 2016:
        c_name = c_dict['Country Name']
        c_gdp = int(float(c_dict['Value']))
        code = get_code(c_name)
        if code:
            gdp_country[code] = c_gdp

wm_style = RS('#663399', base_style=LS)
wm = World(style=wm_style)
wm.title = "World GDP by country - 2016"
wm.add('2016', gdp_country)
wm.render_to_file('images/w_gdp_2016.svg')

