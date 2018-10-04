import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print(f'Status code: {r.status_code}')
response_dict = r.json()
print(response_dict.keys())

repo_items = response_dict['items']
print(f'Repositories returned: {len(repo_items)}')


name, plot_dicts = [], []
for repo_item in repo_items:
    name.append(repo_item['name'])
    description = repo_item['description']
    if not description:
        description = 'No description provided.'
    plot_dict = {
        'value': repo_item['stargazers_count'], 'label': description,
        'xlink': repo_item['html_url']
        }
    plot_dicts.append(plot_dict)

# name, stars,  = [], []
# for repo_item in repo_items:
#     name.append(repo_item['name'])
#     stars.append(repo_item['stargazers_count'])


my_style = LS('#333366', base_style=LCS)
my_style.title_font_size = 30
my_style.label_font_size = 14
my_style.major_label_font_size = 18

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = name

chart.add('', plot_dicts)
chart.render_to_file('py_repos_github.svg')
