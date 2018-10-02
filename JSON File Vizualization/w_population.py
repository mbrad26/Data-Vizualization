import json
from pygal_maps_world.i18n import COUNTRIES
from pygal.maps.world import World
from pygal.style import RotateStyle as RS, LightColorizedStyle as LS

filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)


def get_code(country_name):
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    return None


cc_population = {}
for dict in pop_data:
    if dict['Year'] == '2010':
        country_name = dict['Country Name']
        population = int(float(dict['Value']))
        print(f'{country_name}: {population}')
        code = get_code(country_name)
        if code:
            cc_population[code] = population

pop1, pop2, pop3, pop4, pop5, pop6 = {}, {}, {}, {}, {}, {}
for code, pop in cc_population.items():
    if pop < 10000000:
        pop1[code] = pop
    elif pop < 50000000:
        pop2[code] = pop
    elif pop < 100000000:
        pop3[code] = pop
    elif pop < 150000000:
        pop4[code] = pop
    elif pop < 500000000:
        pop5[code] = pop
    else:
        pop6[code] = pop

wm_style = RS('#336699')
wm = World(style=wm_style)
wm.title = 'World population for 2010 by Country'
wm.add('2010', cc_population)
wm.render_to_file('images/w_pop_2010.svg')

wm_style = RS('#336699', base_style=LS)
wm = World(style=wm_style)
wm.title = 'WP - 2010 - per groups'
wm.add('<10m', pop1)
wm.add('10m-50m', pop2)
wm.add('50m-100m', pop3)
wm.add('100m-150m', pop4)
wm.add('150m-500m', pop5)
wm.add('>1b', pop6)
wm.render_to_file('images/wp_2010_groups.svg')
