#! /usr/bin/env python3

from jinja2 import Environment, FileSystemLoader
import yaml


env = Environment( loader = FileSystemLoader("."))
template = env.get_template('template.j2')

with open("data.yaml","rb") as fh:
    data = yaml.safe_load(fh)

data = sorted(data, key=lambda x : x["name"].lower())

with open("dist/index.html", 'w') as fh:
    fh.write(template.render(data = data))

print("Done")
