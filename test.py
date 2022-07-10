import json

g = {"": {}}
p = {"hmm": "appended"}
r = {5: {"": 45}}
g.update(p)
g.update(r)
print(g)
print(g[""])
