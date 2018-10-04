import requests
import pygal
from pygal.style import LightenStyle as LS

# languages = ['python', 'javascript', 'ruby', 'c', 'java', 'perl', 'haskell, go']

url = 'https://api.github.com/search/repositories?q=language:haskell&sort=stars'

r = requests.get(url)
response = r.json()

items_dict = response['items']

names = [item['name'] for item in items_dict]

plot_dicts = []
for item in items_dict:
    description = item['description']
    if not description:
        description = 'No description available.'
    plot_dict = {
        'value': item['stargazers_count'],
        'label': description,
        'xlabel': item['html_url']
        }
    plot_dicts.append(plot_dict)

my_style = LS('#336633')
my_style.title_font_size = 30
my_style.xlabel_font_size = 14
my_style.major_label_font_size = 16

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.truncate_label = 15
my_config.show_y_guides =False
my_config.width = 1200

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Best-Starred Haskell Repos on GitHub'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('images/best_starred_repos_haskell.svg')