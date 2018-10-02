import csv
from pygal_maps_world.i18n import COUNTRIES
from pygal.maps.world import World
from pygal.style import RotateStyle as RS, LightColorizedStyle as LS


def get_code(country):
    for code, name in COUNTRIES.items():
        if name == country:
            return code
    return None


file_name = 'API_NY.GDP.PCAP.KD.ZG_DS2_en_csv_v2_10134495.csv'
with open(file_name) as f:
    reader = csv.reader(f)
    next(reader)
    next(reader)
    next(reader)
    next(reader)
    for index, name in enumerate(next(reader)):
        print(index, name)
    country_gdp = {}
    for row in reader:
        try:
            country = row[0]
            year = float(row[61])
            code = get_code(country)
            if code:
                country_gdp[code] = year
        except ValueError:
            pass

wm_style = RS('#993366')
wm = World(style=wm_style)
wm.title = 'World GDP per capita increase'
wm.add('2017', country_gdp)
wm.render_to_file('images/gdp_growth.svg')
