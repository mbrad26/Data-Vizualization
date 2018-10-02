import json
from pygal.maps.world import World
from pygal.style import RotateStyle as RS, LightColorizedStyle as LS
from country_codes import get_country_code

filename = 'population_data.json'

with open(filename) as f:
    pop_data = json.load(f)

cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population

pop_1, pop_2, pop_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        pop_1[cc] = pop
    elif pop < 1000000000:
        pop_2[cc] = pop
    else:
        pop_3[cc] = pop

wm_style = RS('#336699', base_style=LS)
wm = World(style=wm_style)
wm.title = 'World Population in 2010, by Country'
wm.add('0-10m', pop_1)
wm.add('10m-1b', pop_2)
wm.add('>1b', pop_3)
wm.render_to_file('images/world_population_2010.svg')

