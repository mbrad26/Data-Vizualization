import requests
import pygal
from pygal.style import LightenStyle as LS

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

r = requests.get(url)
print(r.status_code)

response = r.json()
print(response.keys())

items_dicts = response['items']

# names = [item['name'] for item in items_dicts]
# stars = [item['stargazers_count'] for item in items_dicts]

names, plot_dicts = [], []
for item in items_dicts:
    name = item['name']
    names.append(name)
    description = item['description']
    if not description:
        description = 'No description available.'

    plot_dict = {
        'value': item['stargazers_count'],
        'label': description,
        'xlink': item['html_url']
    }
    plot_dicts.append(plot_dict)

my_style = LS('#669966')
my_style.title_font_size = 30
my_style.label_font_size = 14
my_style.major_label_font_size = 16

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_y_guides = False
my_config.show_legend = False
my_config.truncate_label = 15
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python-Repos on GitHub'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('py_repo_github.svg')
