from pygal.maps.world import World

wm = World()
wm.title = 'North, Central and South America'
wm.add('North America', {'ca': 34126000, 'mx': 113423000, 'us': 309349000})

wm.render_to_file('images/americas.svg')